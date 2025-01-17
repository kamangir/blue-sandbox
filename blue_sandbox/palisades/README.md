# 🧑🏽‍🚒 `palisades`: Post-disaster Land Cover Classification

🧑🏽‍🚒 `palisades` is going to to segment post-disaster multispectral acquisitions from [Maxar Open Data](https://github.com/kamangir/blue-geo/tree/main/blue_geo/catalog/maxar_open_data) into land cover classes such as burned, fuel, and water, first using [pixel-based algo](https://xgboost.readthedocs.io/en/stable/), and then a [SemSeg](https://github.com/kamangir/roofAI).

```mermaid
graph LR
    palisades_ingest["palisades<br>ingest -<br>&lt;query-object-name&gt;|target=&lt;target&gt;<br>&lt;ingest-object-name&gt;"]

    target["🎯 target"]:::folder
    query_object["📂 query object"]:::folder
    ingest_object["📂 query object"]:::folder

    target --> palisades_ingest
    query_object --> palisades_ingest
    palisades_ingest --> query_object
    palisades_ingest --> ingest_object

    classDef folder fill:#999,stroke:#333,stroke-width:2px;
```

## Status 🔥

🔥
