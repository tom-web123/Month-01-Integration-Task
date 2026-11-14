import geopandas as gpd
from shapely.validation import explain_validity

boundary = gpd.read_file('tabata_boundary.gpkg', layer='tabata_boundary')

geom = boundary.geometry.iloc[0]
print('features:', len(boundary))
print('geometry type:', geom.geom_type)
print('valid:', geom.is_valid)
print('why:', explain_validity(geom))
print('empty:', geom.is_empty)




