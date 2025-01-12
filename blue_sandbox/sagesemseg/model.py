import sagemaker
import json
import time
from PIL import Image
from matplotlib import pyplot as plt
import PIL
import numpy as np
import io

from blue_options import string
from blue_options.elapsed_timer import ElapsedTimer
from blue_objects import file, path, objects, host
from blue_options.host import is_jupyter
from blue_objects.storage import instance as storage
from blueflow.sagemaker import role

from blue_sandbox.logger import logger


class ImageDeserializer(sagemaker.deserializers.BaseDeserializer):
    """Deserialize a PIL-compatible stream of Image bytes into a numpy pixel array"""

    def __init__(self, accept="image/png"):
        self.accept = accept

    @property
    def ACCEPT(self):
        return (self.accept,)

    def deserialize(self, stream, content_type):
        """Read a stream of bytes returned from an inference endpoint.
        Args:
            stream (botocore.response.StreamingBody): A stream of bytes.
            content_type (str): The MIME type of the data.
        Returns:
            mask: The numpy array of class labels per pixel
        """
        try:
            return np.array(Image.open(stream))
        finally:
            stream.close()


class SageSemSegModel:
    def __init__(
        self,
        for_training: bool = True,
    ):
        self.for_training = for_training

        self.dataset_object_name = ""
        self.dataset_metadata = {}
        self.model_object_name = ""
        self.data_channels = {}

        timer = ElapsedTimer()
        self.session = sagemaker.Session() if for_training else None
        timer.stop()

        self.estimator = None

        self.training_image = (
            sagemaker.image_uris.retrieve(
                "semantic-segmentation", self.session.boto_region_name
            )
            if for_training
            else None
        )

        self.predictor = None

        logger.info(
            "{} init took {}, image: {}".format(
                self.__class__.__name__,
                timer.elapsed_pretty(include_ms=True),
                self.training_image,
            )
        )

    def attach_to_completed_training_job(
        self,
        job_name: str,
    ):
        self.estimator = sagemaker.estimator.Estimator.attach(job_name)

    def attach_to_endpoint(
        self,
        endpoint_name: str,
    ):
        self.predictor = sagemaker.predictor.Predictor(endpoint_name)

    def train(
        self,
        dataset_object_name: str,
        model_object_name: str,
        epochs: int = 10,
        instance_type: str = "ml.p3.2xlarge",
    ) -> bool:
        if not self.for_training:
            logger.error("set for_training=True first.")
            return False

        self.dataset_object_name = dataset_object_name
        self.model_object_name = model_object_name

        if not storage.download_file(
            f"bolt/{dataset_object_name}/metadata.yaml", "object"
        ):
            return False

        metadata_filename = objects.path_of(
            object_name=dataset_object_name,
            filename="metadata.yaml",
        )
        success, self.dataset_metadata = file.load_yaml(metadata_filename)
        if not success:
            return False

        logger.info(
            "{}.train: {} -> {}".format(
                self.__class__.__name__,
                self.dataset_object_name,
                self.model_object_name,
            )
        )
        logger.info(
            "{}.metadata: {}".format(
                self.dataset_object_name,
                json.dumps(self.dataset_metadata, indent=4),
            )
        )

        self.estimator = sagemaker.estimator.Estimator(
            self.training_image,  # Container image URI
            role,  # Training job execution role with permissions to access our S3 bucket
            instance_count=1,
            instance_type=instance_type,
            volume_size=50,  # in GB
            max_run=360000,  # in seconds
            output_path=f"s3://kamangir/bolt/{model_object_name}",
            base_job_name=model_object_name,
            sagemaker_session=self.session,
        )

        num_classes = (
            21
            if "classes" not in self.dataset_metadata
            else len(self.dataset_metadata["classes"])
        )
        logger.info(f"num_classes: {num_classes}")

        self.estimator.set_hyperparameters(
            backbone="resnet-50",  # This is the encoder. Other option is resnet-101
            algorithm="fcn",  # This is the decoder. Other options are 'psp' and 'deeplab'
            use_pretrained_model="True",  # Use the pre-trained model.
            crop_size=240,  # Size of image random crop.
            num_classes=num_classes,  # Pascal has 21 classes. This is a mandatory parameter.
            epochs=epochs,  # Number of epochs to run.
            learning_rate=0.0001,
            optimizer="rmsprop",  # Other options include 'adam', 'rmsprop', 'nag', 'adagrad'.
            lr_scheduler="poly",  # Other options include 'cosine' and 'step'.
            mini_batch_size=16,  # Setup some mini batch size.
            validation_mini_batch_size=16,
            early_stopping=True,  # Turn on early stopping. If OFF, other early stopping parameters are ignored.
            early_stopping_patience=2,  # Tolerate these many epochs if the mIoU doens't increase.
            early_stopping_min_epochs=10,  # No matter what, run these many number of epochs.
            num_training_samples=self.dataset_metadata["num"][
                "train"
            ],  # num_training_samples,  # This is a mandatory parameter, 1464 in this case.
        )

        distribution = "FullyReplicated"
        self.data_channels = {
            "train": sagemaker.inputs.TrainingInput(
                self.dataset_metadata["channel"]["train"],
                distribution=distribution,
            ),
            "validation": sagemaker.inputs.TrainingInput(
                self.dataset_metadata["channel"]["validation"],
                distribution=distribution,
            ),
            "train_annotation": sagemaker.inputs.TrainingInput(
                self.dataset_metadata["channel"]["train_annotation"],
                distribution=distribution,
            ),
            "validation_annotation": sagemaker.inputs.TrainingInput(
                self.dataset_metadata["channel"]["validation_annotation"],
                distribution=distribution,
            ),
            # 'label_map': metadata["channel"]["label_map"], # label_map_channel
        }

        self.estimator.fit(self.data_channels, logs=True)

        return True

    def deploy(self, **kwargs):
        self.predictor = self.estimator.deploy(**kwargs)

        self.predict_validation()

    def predict_validation(self):
        self.predictor.deserializer = ImageDeserializer(
            accept="image/png",
        )

        self.predictor.serializer = sagemaker.serializers.IdentitySerializer(
            "image/png"
        )

        path.create(
            objects.path_of(
                object_name=self.model_object_name,
                filename="validation/",
            )
        )
        filename_raw = objects.path_of(
            object_name=self.model_object_name,
            filename="validation/test.png",
        )

        host.shell(
            f"wget -O {filename_raw} https://upload.wikimedia.org/wikipedia/commons/b/b4/R1200RT_in_Hongkong.jpg"
        )

        filename = objects.path_of(
            object_name=self.model_object_name,
            filename="validation/test_resized.jpg",
        )
        width = 800
        im = PIL.Image.open(filename_raw)
        aspect = im.size[0] / im.size[1]
        # https://stackoverflow.com/a/14351890/17619982
        im.thumbnail([width, int(width / aspect)], PIL.Image.LANCZOS)
        plt.imshow(im)
        if is_jupyter():
            plt.show()
        plt.close()

        img_byte_arr = io.BytesIO()
        im.save(img_byte_arr, format="PNG")
        imbytes = img_byte_arr.getvalue()

        # im.save(filename, "JPEG")
        # with open(filename, "rb") as imfile:
        #    imbytes = imfile.read()

        # Extension exercise: Could you write a custom serializer which takes a filename as input instead?

        start_time = time.time()
        cls_mask = self.predictor.predict(imbytes)
        elapsed_time = time.time() - start_time

        logger.info(
            "{} -> {}: {}".format(
                string.pretty_duration(elapsed_time),
                string.pretty_shape_of_matrix(cls_mask),
                np.unique(cls_mask),
            )
        )

        plt.imshow(cls_mask, cmap="jet")
        plt.savefig(
            objects.path_of(
                object_name=self.model_object_name,
                filename="validation/output.jpg",
            )
        )
        if is_jupyter():
            plt.show()

    def delete_endpoint(self):
        self.predictor.delete_endpoint()
