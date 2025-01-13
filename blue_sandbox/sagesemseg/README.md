# 🌀 `sagesemseg`: SemSeg on SageMaker

🌀 `sagesemseg` is A SemSeg (Semantic Segmenter) trained and deployed on AWS Sagemaker, based on [Amazon SageMaker Semantic Segmentation Algorithm](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/semantic_segmentation_pascalvoc/semantic_segmentation_pascalvoc.ipynb).


```mermaid
graph LR
    train["sagesemseg<br>train<br>[deploy]<br>&lt;dataset-object-name&gt;<br>&lt;model-object-name&gt;"]
    deploy["sagesemseg<br>deploy -<br>&lt;model-object-name&gt;"]
    predict["sagesemseg<br>predict<br>[deploy]<br>&lt;model-object-name&gt;&lt;dataset-object-name&gt;&lt;prediction-object-name&gt;"]

    dataset["dataset"]:::folder
    model["model"]:::folder
    prediction["prediction"]:::folder

    dataset --> train
    train --> model

    model --> deploy

    model --> predict
    dataset --> predict
    predict --> prediction
```

## Status 🔥

[train](../../notebooks/sagesemseg/semantic_segmentation_pascalvoc-v9-train.ipynb), [deploy](../../notebooks/sagesemseg/semantic_segmentation_pascalvoc-v11-deploy.ipynb), and [predict](../../notebooks/sagesemseg/semantic_segmentation_pascalvoc-v11-predict.ipynb) are done through notebooks.

Two completed jobs to deploy,

- `$SAGESEMSEG_COMPLETED_JOB_pascal_voc_v1_debug_v2`
- `$SAGESEMSEG_COMPLETED_JOB_pascal_voc_v1_full_v2` ⭐️  larger dataset, use for dev.

`$SAGESEMSEG_COMPLETED_JOB_<object-name>` is trained on `<object-name>`.

🔥

## future 🚧

```bash
@conda activate sagemaker

@select roofAI-sagemaker-dataset-AIRS-1000-v4

roofAI dataset ingest \
    source=AIRS,target=sagemaker,upload . \
    --test_count 0 \
    --train_count 1000 \
    --val_count 200

@select roofAI-sagemaker-semseg-AIRS-1000-v4

sagesemseg train - .. . \
    --instance_type ml.g4dn.2xlarge
```
