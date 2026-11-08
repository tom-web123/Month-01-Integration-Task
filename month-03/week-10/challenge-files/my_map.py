import geopandas as gpd
import matplotlib.pyplot as plt

tabata_boundary = gpd.read_file('tabata_boundary.gpkg', layer='tabata_boundary')
wards = gpd.read_file('month-03/week-10/challenge-files/wards.gpkg', layer='wards')
wards = wards.to_crs(tabata_boundary.crs)

fig, ax = plt.subplots(figsize=(7, 8))
tabata_boundary.plot(ax=ax, color='#D4B23A', edgecolor='#222222', linewidth=1)
wards.plot(ax=ax, color='#5F6B73', edgecolor='#222222', markersize=30, zorder=3)
ax.set_title('Tabata ward map')

ax.set_axis_off()
fig.savefig('month-03/week-10/challenge-files/Tabata_ward_map.png', dpi=150, bbox_inches='tight')

print('map saved')


