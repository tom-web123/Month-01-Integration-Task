import geopandas as gpd

boundary = gpd.read_file('tabata_boundary.gpkg', layer='tabata_boundary')
buildings = gpd.read_file('week-3-prepared-data/data/buildings.gpkg', layer='buildings')

print('CRS:', boundary.crs)
print('CRS:', buildings.crs)



