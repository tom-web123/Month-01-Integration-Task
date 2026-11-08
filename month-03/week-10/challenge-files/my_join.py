import pandas as pd
import geopandas as gpd

tabata = pd.read_csv('Tabata_wards.csv')
wards = pd.read_csv('wards.csv')


def clean_name(name):
    return name.strip().upper().replace('-','')

wards['join_key']= wards['ward'].apply(clean_name)
tabata['join_key']= tabata['ward'].apply(clean_name)

joined= wards.merge(tabata, on='join_key', how='left', suffixes=('', '_tabata'))
matched= joined.loc[joined['population'].notna(), 'ward'].nunique()

print('matched after cleaning:', matched, 'of', len(wards))
print(joined[['ward', 'subward', 'population']])