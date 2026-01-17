# Near Earth Asteroid + Hazard Analysis
This project analyzes near-earth asteroids over a 7-day window using NASA's NEO API, compiling the average diameters between hazardous and non-hazardous objects

## Motivation

Near-Earth objects (NEOs) pose varying levels of risk depending on their size, velocity, and orbital characteristics. This project explores whether potentially hazardous asteroids exhibit systematically different size and velocity distributions than non-hazardous asteroids, and whether further data analysis would be required to have a suitable sample size for analysis of hazardous asteroids.

## Data Source

Data are obtained from NASA’s Near Earth Object Web Service (NeoWs) API:
https://api.nasa.gov/

The `feed` endpoint is used to retrieve close-approach data for asteroids over a specified date range.

## Methods

- Queried the NASA NEO API for a 7-day window
- Converted the nested JSON data into a flat table
- Extracted estimated diameters, velocities, and hazard classifications
- Compared diameter and velocity distributions using histogram plots

## Results

The analysis shows that the majority of near-Earth asteroids detected by NASA over these 7 days were under 100m in diameter. There is only a single potentially hazardous object detected; this perceived rarity warrants further data analysis to determine whether the characteristics of potentially hazardous objects differ from those of non-hazardous objects.

## How to Run

### Requirements
- Python 3.9+
- requests
- pandas
- matplotlib

### Install dependencies
```bash
pip install requests pandas matplotlib
