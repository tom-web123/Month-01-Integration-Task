import rasterio

with rasterio.open('Tabata DEM.tif') as src:
    print('width x height:', src.width, 'x', src.height)
    print('Bands:', src.count)
    print('Data type:', src.dtypes)
    print('CRS:', src.crs)
    print('Pixel size:', src.res)
    print('Bounds:', src.bounds)
    print('Nodata:', src.nodata)
    print('Transform:')
    print(src.transform)