import pandas as pd
import geopandas as gpd

table= pd.read_csv('point_wards.csv')
print(table.head(3))

wards = gpd.GeoDataFrame(
    table, 
    geometry= gpd.points_from_xy(table['longitude'], table['latitude']),
    crs= 'EPSG:4326'
)

print(wards.head(3))
print(wards.crs)

wards.to_file('month-03/week-10/challenge-files/wards.gpkg', layer='wards')
print('Saved', len(wards), 'wards')

