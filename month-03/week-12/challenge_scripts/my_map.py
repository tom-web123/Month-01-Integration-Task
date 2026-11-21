import rasterio
import matplotlib.pyplot as plt

with rasterio.open('Tabata DEM.tif') as src:
    Dem = src.read(1, masked=True)

fig, ax = plt.subplots(figsize=(7, 8))
image = ax.imshow(Dem, cmap='terrain', vmin=float(Dem.min()), vmax=float(Dem.max()))
fig.colorbar(image, ax=ax, label='Elevation (m)')
ax.set_title('Tabata DEM')

ax.set_axis_off()
fig.savefig('month-03/week-12/challenge_scripts/tabata_dem_map.png', dpi=150, bbox_inches='tight')

print('Saved tabata_dem_map')