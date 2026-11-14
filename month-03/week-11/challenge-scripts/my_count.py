import geopandas as gpd
boundary = gpd.read_file('tabata_boundary.gpkg', layer='tabata_boundary')
buildings = gpd.read_file('week-3-prepared-data/data/buildings.gpkg', layer='buildings')
amenity = gpd.read_file('week-3-prepared-data/data/amenity.gpkg', layer='amenity')

print('Number of buildings:', len(buildings))
print('Number of amenities:', len(amenity))



