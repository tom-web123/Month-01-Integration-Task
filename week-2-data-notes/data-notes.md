# Data Note 

Tabata Ward Road Accessibility

All datasets were pulled from OpenStreetMap using the QuickOSM plugin in QGIS, clipped to Tabata Ward, and saved as GeoPackage (`.gpkg`) files. Feature counts and column contents below were read directly from each `.gpkg`.

---

## 1. Ward boundary — `tabata_boundary.gpkg`

- **Source:** OpenStreetMap: https://www.openstreetmap.org/
- **Feature count:** 1
- **Geometry type:** MultiPolygon
- **CRS:** EPSG:32737 (UTM Zone 37S)
- **Key columns:** `Municipal`, `Ward`, `Subward`, `Feature`, `Latitude`, `Longitude` (also `ringId` = 1 and `distance` = 300)
- **Attribute values:** Municipal = Ilala, Ward = Tabata, Subward = Tabata, Feature = Siren
- **Gaps/notes:** Single-feature layer as expected for a ward boundary — no missing values. The `Subward` value ("Tabata") suggests this may be one subward's polygon standing in for the whole ward, or a dissolved boundary labeled after its central subward — worth double-checking against the ward's full extent (Tabata Ward has multiple subwards/mitaa: Mandela, Matumbi, Msimbazi, Mtambani, Tenge, Kisiwani, etc.) before treating this as the definitive ward outline. The `ringId` and `distance` (300) columns look like output from a QGIS multi-ring buffer tool, so also check the outline was not buffered. It is 4.39 km² and the buildings stop about 30 m inside it, so it does not look enlarged by 300 m.

## 2. Road network — `roads.gpkg`

- **Source:** OpenStreetMap (via QuickOSM, `highway=*`) — https://www.openstreetmap.org/
- **Feature count:** 564
- **Geometry type:** MultiLineString
- **CRS:** EPSG:32737 (UTM Zone 37S)
- **Key columns:** `highway` (road type), `name`, `surface`, `smoothness`, `width`, `ward_name`
- **Highway type breakdown:** footway (284), residential (175), service (33), unclassified (31), primary (12), tertiary (9), secondary (9), pedestrian (5), path (3), cycleway (3)
- **Surface breakdown:** unpaved (498), asphalt (34), compacted (24), concrete (6), paved (2) — only ~7% of segments have a hard-paved surface
- **Gaps/notes:** `name` is missing for 405 of 564 segments (72%) — most unnamed roads are footways/service roads, which is expected. `ward_name` is filled for 554 records ("Tabata", plus one typo, "Br. Tabata") and missing for 10 — it is not needed for the analysis. Week 4 uses `buffered_roads.gpkg`, which holds these same 564 segments as polygons, buffered by about 15 m around each road centreline. `surface` has good coverage, which is what the accessibility analysis depends on most.

## 3. Buildings — `buildings.gpkg`

- **Source:** HotOSM — https://export.hotosm.org/v3/ 
- **Feature count:** 16,879
- **Geometry type:** MultiPolygon
- **CRS:** EPSG:32737 (UTM Zone 37S)
- **Key columns:** `building` (building type), `name`, `amenity`, `addr_street`, `addr_housenumber`, `building_levels`, `building_material`, `health_facility_type`
- **Building type breakdown:** residential (9,884), yes/unspecified (5,472), commercial+residential mixed-use (631), commercial (602), school (168), public (34), place of worship (34), industrial (32), hospital (8), utility (7), office (7)
- **Gaps/notes:** This is a very wide, sparsely-filled attribute table (78 columns total, many carried over from a broader export template — e.g. `power`, `waterway`, `railway`, `military` are 100% null and irrelevant to buildings). Columns that matter for this project are mostly well-populated: `building` type is filled in for all 16,879 records. `addr_street` is missing for ~35% of buildings and `addr_housenumber` for 99.9% (only 15 are filled) — expected in informally-planned areas. `building_levels` and `building_material` are filled for about 11,000 records (65%) and missing for about 5,900 (35%) — useful if you want a vulnerability layer later, but not complete enough to use as a primary variable yet.

## 4. Amenities (schools) — `amenity.gpkg`

- **Source:** OpenStreetMap (via QuickOSM, `amenity=*`) —  https://www.openstreetmap.org/
- **Feature count:** 16
- **Geometry type:** Point
- **CRS:** EPSG:4326 (WGS 84, longitude/latitude) — reprojected to EPSG:32737 for the analysis
- **Key columns:** `amenity`, `name`, `name:en`, `isced:level`, `operator`, `addr:ward`, `addr:subward`, `religion`, `condition`
- **Attribute values:** all 16 features are tagged `amenity = school` — no health facilities (hospitals/clinics) came through this query. (Hospitals do appear separately, tagged as `building = hospital`, in `buildings.gpkg` — 8 features.)
- **Gaps/notes:** `name` is present for 14 of 16 schools; more detailed attributes (`isced:level`, `religion`, `operator`) are missing for most records, which is normal for OSM school POIs and not a problem for a distance-based analysis. Because no clinics/hospitals came through the amenity query, health-facility accessibility will need to draw on the 8 `building=hospital` records instead — worth flagging as a real coverage gap since it means the "health facilities" side of the question rests on very few points.


