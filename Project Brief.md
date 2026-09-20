# My Project Brief

## Question

**Which wards in Owerri North are more than 5 km from a health facility?**

## Why It Matters

Access to healthcare depends partly on how close people are to health facilities. Identifying wards in Owerri North that are more than 5 km from a health facility can reveal areas where residents may face longer travel distances when seeking medical care.

This information can support healthcare planning, facility placement, and better allocation of health resources.

## Data Needed

* GRID3 health facilities
* GRID3 ward boundaries
* OSM roads

## Data Sources

### Nigeria State Boundaries

[GRID3 NGA – Operational State Boundaries (December 2020)](https://data.grid3.org/datasets/GRID3::grid3-nga-operational-state-boundaries-/about)

### Nigeria LGA Boundaries

[GRID3 NGA – Operational LGA Boundaries (December 2020)](https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about)

### Nigeria Ward Boundaries

[GRID3 NGA – Operational Wards v1.0 (December 2020)](https://data.grid3.org/datasets/GRID3::grid3-nga-operational-wards-v1-0/about)

### Health Facilities

[GRID3 NGA – Health Facilities v2.0 (November 2024)](https://data.grid3.org/datasets/GRID3::grid3-nga-health-facilities-v2-0/about)

### Roads

Road data for the study area will be extracted using the **QuickOSM plugin in QGIS**.

## What I Will Build

I will build an interactive web map of **Owerri North LGA** that identifies and highlights wards located more than **5 km from existing health facilities**.

The map will:

* Highlight wards that are more than 5 km from a health facility.
* Show the locations of health facilities.
* Use road data to support distance-based analysis.
* Provide an interactive view of healthcare accessibility across Owerri North.
* Be updated periodically as new roads or health facilities are added.
