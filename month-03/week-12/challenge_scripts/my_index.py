import geopandas as gpd
import rasterio
from rasterio.mask import mask

boundary = gpd.read_file('tabata_boundary.gpkg', layer='tabata_boundary')

with rasterio.open('Tabata DEM.tif') as src:
    boundary = boundary.to_crs(src.crs)
    clipped, transform = mask(src, boundary.geometry, crop=True, filled=False)
    crs = src.crs
    print('Before clip:', src.width, 'x', src.height, 'pixels')

elevation = clipped[0].astype('float32')         
print('After clip:', elevation.shape[1], 'x', elevation.shape[0], 'pixels')
low = float(elevation.min())
high = float(elevation.max())
index = (high - elevation) / (high - low)

print('Elevation range:', round(low, 1), 'to', round(high, 1), 'm')
print('Mean elevation:', round(float(elevation.mean()), 1), 'm')
print('Index range:', round(float(index.min()), 3), 'to', round(float(index.max()), 3))
print('Mean index:', round(float(index.mean()), 3))


