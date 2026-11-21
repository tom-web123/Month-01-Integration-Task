import rasterio
import geopandas as gpd
import numpy as np
from rasterio.mask import mask

with rasterio.open('Tabata DEM.tif') as src:
    wards = gpd.read_file('tabata_boundary.gpkg', layer='tabata_boundary').to_crs(src.crs)
    means, mins, maxs, counts = [], [], [], []
    for geom in wards.geometry:
        cells, _ = mask(src, [geom], crop=True, filled=False)
        means.append(float(cells.mean()))
        mins.append(float(cells.min()))
        maxs.append(float(cells.max()))
        counts.append(int(cells.count()))

wards['mean_elevation_m'] = np.round(means, 1)
wards['min_elevation_m'] = np.round(mins, 1)
wards['max_elevation_m'] = np.round(maxs, 1)
wards['n_cells'] = counts

columns = ['Ward', 'mean_elevation_m', 'min_elevation_m', 'max_elevation_m', 'n_cells']
print(wards[columns])

wards[columns].to_csv('month-03/week-12/challenge_scripts/zonal_stats.csv', index=False)
print('Saved zonal_stats.csv')