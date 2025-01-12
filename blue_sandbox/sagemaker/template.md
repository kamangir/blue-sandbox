# SageMaker

Based on [Amazon SageMaker Semantic Segmentation Algorithm](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/semantic_segmentation_pascalvoc/semantic_segmentation_pascalvoc.ipynb).

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

wip 🔥