# Project Brief

## Spatial Question
Which residential buildings in Tabata Ward, Ilala Municipality, Dar es Salaam are located more than 300 metres from the nearest paved road, and what does this mean for their access to schools and health facilities?

## Study Area
Tabata Ward, Ilala Municipality, Dar es Salaam Region, Tanzania (4.39 km²). The ward boundary was pulled from OpenStreetMap and saved as `tabata_boundary.gpkg` (one MultiPolygon, EPSG:32737). Its `Subward` value is "Tabata", so it still needs checking that this outline covers the whole ward and not one subward.

## Datasets

| Dataset | Purpose | Source |
|---|---|---|
| Tabata ward boundary (`tabata_boundary.gpkg`) | Define and clip the study area | https://www.openstreetmap.org/ |
| Roads (`roads.gpkg`, `highway=*`) | Find paved roads from the `surface` tag (asphalt, concrete, paved) | https://www.openstreetmap.org/ (via QuickOSM); also https://export.hotosm.org/v3/ |
| Buildings (`buildings.gpkg`) | Select residential buildings (`building=residential`) and find hospitals (`building=hospital`) | https://export.hotosm.org/v3/ |
| Amenities (`amenity.gpkg`) | Locate schools (16 points) | https://www.openstreetmap.org/ (via QuickOSM) |
| Buffered roads (`buffered_roads.gpkg`) | Draw the roads on the Week 4 map | Made from `roads.gpkg` in QGIS |

## Method Summary
1. Keep all layers in EPSG:32737 (WGS 84 / UTM zone 37S) so distances are in metres, and check they sit inside the Tabata boundary.
2. Select paved roads: `surface` is asphalt, concrete or paved (cycleways left out).
3. Select residential buildings: `building` is residential.
4. Measure the distance from each residential building to the nearest paved road, and mark the ones more than 300 m away.
5. Check which of those buildings lie within 300 m of the ward edge, because a paved road just outside the ward is not in the data and could be closer.
6. Measure the distance from each residential building to the nearest school and the nearest health facility, and compare the buildings more than 300 m from a paved road with the rest.
7. Make a map and write up the result in `month-1-summary.md`.

## Repository Contents
- `README.md` - the short answer, and links to every deliverable.
- `week-1-project-brief/project-brief.md` - this file.
- `week-2-data-notes/data-notes.md` - what was downloaded.
- `week-3-prepared-data/` - data preparation note, quality checks and the five input layers in one file (`data/tabata_analysis.gpkg`).
- `week-4-analysis/` - the map image and `month-1-summary.md`.
- `results/` - the list of buildings over 300 m and the distances layer.
