import geopandas as gpd
import matplotlib.pyplot as plt

boundary = gpd.read_file('tabata_boundary.gpkg', layer='tabata_boundary')
buildings = gpd.read_file('week-3-prepared-data/data/buildings.gpkg', layer='buildings')

fig, ax = plt.subplots(figsize=(8, 8))
boundary.plot(ax=ax, color='#F3EBC8', edgecolor='#222222', linewidth=1.2)
buildings.plot(ax=ax, color='#9a9a9a', linewidth=0)
ax.set_title('Buildings in Tabata Ward')
ax.set_axis_off()

fig.savefig('month-03/week-11/challenge-scripts/tabata_buildings.png', dpi=150, bbox_inches='tight')
print('map saved')