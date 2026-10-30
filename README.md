# Tabata Ward Road Accessibility

**Which residential buildings in Tabata Ward, Ilala Municipality, Dar es Salaam are located more than 300 metres from the nearest paved road, and what does this mean for their access to schools and health facilities?**

## The answer in short

**Which buildings?**
- **5,652 of 9,884 residential buildings (57.2%) are more than 300 m from the nearest paved road.** The furthest being 1,150 m away.
- **1,250 of them are certain. The other 4,402 need a check:** They are within 300 m of the ward edge, and the road data stops at the edge, so a paved road just outside Tabata might be closer. They are marked in the list.
- "Paved" means the OpenStreetMap road tag says asphalt, concrete or paved. Only 7.3 km of the 84.3 km of mapped roads and paths are paved.

**What does it mean for access?**
- **Health facilities:** the distance is about the same as for the other buildings, but 686 of these buildings are more than 1 km from a health facility. The data has only 8 hospital footprints, so treat this with care.
- **Schools:** these buildings are not further from a school than the others.

## Start here:

| Week | What it is | Link |
|---|---|---|
| 1 | Project brief | [week-1-project-brief/project-brief.md](week-1-project-brief/project-brief.md) |
| 2 | Data notes | [week-2-data-notes/data-notes.md](week-2-data-notes/data-notes.md) |
| 3 | Data preparation | [week-3-prepared-data/data-preparation-note.md](week-3-prepared-data/data-preparation-note.md) |
| 3 | Data | [week-3-prepared-data/data/tabata_analysis.gpkg](week-3-prepared-data/data) |
| 4 | Map image | [week-4-analysis/tabata-road-accessibility-map.png](week-4-analysis/tabata-road-accessibility-map.png) |
| 4 | Month 1 summary (the analysis and result) | [week-4-analysis/month-1-summary.md](week-4-analysis/month-1-summary.md) |


## Folder layout

```
tabata-road-accessibility/
├── README.md
├── week-1-project-brief/
│   └── project-brief.md
├── week-2-data-notes/
│   └── data-notes.md
├── week-3-prepared-data/
│   ├── data-preparation-note.md
│   └── data/tabata_analysis.gpkg  (all five input layers in one file)
├── week-4-analysis/
│   ├── tabata-road-accessibility-map.png
│   └── month-1-summary.md
```






## Month 2: Development environment and early Python
| Week | What I did | Link |
|---|---|---|
| 5 | Set up Python, VS Code and the terminal. `hello.py` prints a message. | [hello.py](geoclean/week_05/hello.py) · [screenshot](geoclean/week_05/screenshots/week5.png) |
| 6 | Set up the project with uv and added pandas. `check.py` prints the pandas version. | [pyproject.toml](pyproject.toml) · [uv.lock](uv.lock) · [check.py](check.py) · [screenshot](geoclean/week_05/screenshots/week6.png) |
| 7 | `analyse.py` reads `wards.csv`, converts each area and labels each ward large or small. | [wards.csv](wards.csv) · [analyse.py](analyse.py) · [screenshot](geoclean/week_05/screenshots/week7.png) |
| 8 | `inspect_data.py` reads my tabata_wards.csv data | [tabata_wards.csv](Tabata_wards.csv) · [inspect_data.py](inspect_data.py) · [screenshot](geoclean/week_05/screenshots/week_08.png) |
| 9 | summary.py and Capstone: `capstone.py` summarises `area_m2` and `building_levels` of my Month 1 buildings. | [summary.py](summary.py) · [capstone.py](capstone.py)  [screenshot](geoclean/week_05/screenshots/screenshots/week_09.png) |

`tabata_buildings.csv` comes from the `buildings` layer in `week-3-prepared-data/data/tabata_analysis.gpkg`, filtered to `building = residential`. `area_m2` is the footprint area in EPSG:32737 (metres).

## Month 2 reflection
1. The idea that finally clicked this month was breaking one long script into small functions: when I split my repeated code into read_rows, clean_values and summarise, my copy-paste bug (appending to the wrong list) disappeared because each job lived in only one place
2. Easy ways of debugging my errors
3. What is still fuzzy is how Python handles scope and file lifetime, such as why rows has to be created inside the with block, and when I need .items() with parentheses versus without.












