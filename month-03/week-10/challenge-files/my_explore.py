import pandas as pd
build = pd.read_csv('tabata_buildings.csv')

print(build.head())
print('shape:', build.shape)
print('columns:', list(build.columns))
print(build.dtypes)
print(build['building'].describe())
