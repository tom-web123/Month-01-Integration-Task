import rasterio
import geopandas as gpd
import numpy as np
from rasterio.mask import mask

with rasterio.open('data/raw/dem.tif') as src:
    wards = gpd.read_file('data/processed/wards.gpkg', layers = 'wards').to_crs(src.crs)
    means = []
    for geom in wards.geometry:
        cells, _ = mask(src, [geom], crop=True, filled=False)
        means.append(float(cells.mean()))

wards['mean_elevation_m'] = np.round(means, 1)
print(wards[['ward_name', 'mean_elevation_m']])


