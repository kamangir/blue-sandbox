# Satellite imagery damage assessment workflow

🌐 `@damage` is a work in progress on [Satellite imagery damage assessment workflow](https://github.com/microsoft/building-damage-assessment/blob/main/SATELLITE_WORKFLOW.md).

---

purpose: ... given post-disaster imagery ... to identify whether each known building footprint ... is damaged, and to what extent ... approach: ... fine-tune a pre-trained semantic segmentation model on a small amount of labeled data collected in the AOI itself ... model ... then ... generates per-pixel prediction over the entire imagery, which can then be summarized at the building level

🔥

TODO: add the rest of the md 🔥


```mermaid
graph LR
    ingest["@damage<br>ingest -<br>&lt;dataset-object-name&gt;"]
    label["@damage<br>label -<br>&lt;dataset-object-name&gt;"]
    train["@damage<br>train -<br>&lt;dataset-object-name&gt;&lt;model-object-name&gt;"]
    predict["@damage<br>predict -<br>&lt;dataset-object-name&gt;&lt;model-object-name&gt;&lt;prediction-object-name&gt;"]
    summarize["@damage<br>summarize -<br>&lt;prediction-object-name&gt;"]

    dataset["dataset"]:::folder
    model["model"]:::folder
    prediction["prediction"]:::folder

    ingest --> dataset

    dataset --> label
    label --> dataset

    dataset -> train
    train -> model

    dataset -> predict
    model -> predict
    predict -> prediction

    prediction -> summarize
    summarize -> prediction

    classDef folder fill:#999,stroke:#333,stroke-width:2px;
```

