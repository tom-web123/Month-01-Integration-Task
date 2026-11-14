import geopandas as gpd
tabata_boundary = gpd.read_file('tabata_boundary.gpkg', layer='tabata_boundary')
buildings = gpd.read_file('week-3-prepared-data/data/buildings.gpkg', layer='buildings')



tabata_boundary['area_km2']= tabata_boundary.area / 1000000
reach = buildings[['geometry']].copy()
reach['geometry'] = reach.buffer(2000)
reach = reach.dissolve()

uncovered = gpd.overlay(tabata_boundary, reach, how='difference')
uncovered['uncovered_km2'] = uncovered.area / 1000000
total_km2 = tabata_boundary['area_km2'].sum()
uncovered_km2 = uncovered['uncovered_km2'].sum()  
uncovered_pct = uncovered_km2 / total_km2 * 100

print('Tabata area (km2):', round(total_km2, 2))
print('Uncovered (km2):', round(uncovered_km2, 2))


