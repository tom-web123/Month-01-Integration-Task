# Month 1 Summary

## Question

Which residential buildings in Tabata Ward (Ilala Municipality, Dar es Salaam) are more than 300 metres from the
nearest paved road, and what does this mean for their access to schools and health facilities?

## Operation

Measured the distance from every residential building (`building = residential`, 9,884 buildings, all inside the
ward boundary) to the nearest paved road, then marked the buildings more than 300 m away. Paved roads are the
`roads.gpkg` lines with `surface` = asphalt, concrete or paved (39 segments, cycleways left out). I did the
calculation outside QGIS with a script; in QGIS the same job is done with **Join attributes by nearest**
(Processing Toolbox → Vector general). All layers were put in EPSG:32737 (WGS 84 / UTM zone 37S), so distances are
in metres; `amenity.gpkg` was in EPSG:4326 and had to be reprojected.

I chose it because the question asks for a list of individual buildings and a distance for each one. A count in a
polygon or a single 300 m buffer would give a number or a shape, not the list. Distance is measured from the
nearest edge of each building, so "more than 300 m" means no part of the building is within 300 m. The same
measure gave the distance to the nearest school (16 school points in `amenity.gpkg`) and the nearest health
facility (8 `building = hospital` footprints).

## Expected

About half of the buildings. The earlier road-network result showed 52% of the mapped road network more than 300 m
from a paved road, so I expected a similar share for buildings, and I expected those buildings to be farther from
schools and health facilities than the rest.

## Got

* 5,652 of 9,884 residential buildings (57.2%) are more than 300 m from a paved road; 4,232 are within 300 m.
  The 5,652 are listed in `results/residential-buildings-over-300m-from-paved-road.csv` (the `results` folder at the top of the repository).
* They are a median 579 m from a paved road; the farthest is 1,150 m. Where they are: all 1,334 buildings in the
  north-western lobe, about 8 in 10 in the south-central part (2,198 of 2,635), and none in the north-east along
  Nelson Mandela Road.
* Only 1,250 of the 5,652 are certain. The other 4,402 are within 300 m of the ward edge, and the road data stops at
  the edge, so a paved road just outside Tabata could be closer to them. They are marked in the CSV.
* Health facilities: far buildings have a median 490 m to the nearest one, against 510 m for the rest. 2,729 of
  them (48.3%) are more than 500 m away and 686 (12.1%) are more than 1 km away, against 10.1% of the rest.
* Schools: far buildings have a median 237 m to the nearest school, against 281 m for the rest. 1,282 (22.7%) are
  more than 500 m away and 83 (1.5%) are more than 1 km away, against 7.6% of the rest.
* 98% of the far buildings are within 50 m of a mapped road or footpath that is not paved (median 8 m), so a trip to
  a school or clinic starts on an unpaved road or footpath. Only 7.3 km of the 84.3 km of mapped roads and paths
  are paved. That is likely to make real travel harder than the straight-line distances show, but I did not
  measure travel time or travel distance.
* Checks:
  * 4,232 + 5,652 = 9,884, so every residential building is counted once.
  * The split is clean: the nearest far building is 300.04 m away and the farthest near one is 299.91 m.
  * 0 invalid geometries and 0 buildings without a distance.
  * The count changes if I change the rules: counting compacted roads as paved gives 2,732 (28%); measuring from
    the building centre gives 5,724; adding the 631 mixed-use buildings gives 5,963 of 10,515.

## What surprised me

* **The ward edge matters a lot.** 71.8% of all buildings are within 300 m of the boundary, because the ward is
  narrow, so most of the far buildings cannot be confirmed without roads from outside the ward.
* **Far buildings are not farther from schools or health facilities.** I expected them to be, but the health
  distances are almost the same for both groups and the far buildings are closer to schools. The difference is the
  road surface on the way, not the distance.
* **Health facilities are very thin in the data.** 8 hospital footprints (several of them repeats of the same
  facility) and 16 schools, so both results rest on few points.

## What I still need

* Roads from outside the ward. Pull the roads again with a 300 m margin around Tabata, then re-measure the 4,402
  buildings near the ward edge.
* Clinics and pharmacies. They appear on the map but are not in `amenity.gpkg` (16 schools only), so health access
  uses the 8 hospital footprints.
* Travel distance along roads and paths, instead of straight-line distance, to show how much the unpaved surface
  really adds.
* A confirmed full ward boundary. The boundary's `Subward` value is "Tabata", which may mean one subward's polygon
  is standing in for the whole ward, and its `ringId` and `distance` (300) columns look like buffer-tool output.
* A decision on the 5,472 buildings tagged only "yes" (type unknown), which are not counted as residential.
* A map layer showing the 5,652 buildings. The current map shows all roads, and its legend says "Buffered roads
  (300m)" although the buffer is about 15 m.

## Sources

* Amenity points and roads: OpenStreetMap (https://www.openstreetmap.org/), QuickOSM; roads also from HOTOSM
  (https://export.hotosm.org/v3/)
* Buildings: HOTOSM (https://export.hotosm.org/v3/)
* Ward boundary: HCMGIS plugin in QGIS
* Results: `results/residential-buildings-distances.gpkg` (all 9,884 residential buildings with their distances) and
  `results/residential-buildings-over-300m-from-paved-road.csv` (the 5,652 buildings over 300 m)
