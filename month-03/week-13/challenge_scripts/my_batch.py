#Docstring
'''Convert every csv of Tabata subward points in a folder into a Geopackage of points

Run from the root of your repository:
    uv run month-03/week-13/challenge_scripts/my_batch.py
'''
#Imports
import logging
import time
from pathlib import Path
import geopandas as gpd
import pandas as pd

#settings(constant)
INPUT_FOLDER = Path('month-03/week-13/challenge_scripts/my_batch_input')
OUTPUT_FOLDER = Path('month-03/week-13/challenge_scripts/my_batch_output')
SUMMARY_FILE= Path('month-03/week-13/challenge_scripts/my_batch_summary.csv')
LOG_FILE = Path('month-03/week-13/challenge_scripts/my_batch_run.log')
WORKING_CRS = 'EPSG:32737'
OVERWRITE = False


# Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()],
)
logging.getLogger("pyogrio").setLevel(logging.WARNING)


# csv_to_point
def csv_to_points(csv_path):
    table = pd.read_csv(csv_path)
    missing ={'latitude', 'longitude'} - set(table.columns)
    if missing:
        raise ValueError(f'missing columns: {sorted(missing)}')
    # rows with no coordinates cannot become points
    complete = table.dropna(subset=['latitude', 'longitude'])
    if len(complete) < len(table):
        logging.warning('%s : dropped %d row(s) with no coordinates',
                        csv_path.name, len(table) - len(complete))
    points = gpd.GeoDataFrame(
        complete, 
        geometry= gpd.points_from_xy(complete['longitude'], complete['latitude']),
        crs= 'EPSG:4326'
    )
    return points.to_crs(WORKING_CRS)


def process_one(csv_path):
    out_path = OUTPUT_FOLDER / f'{csv_path.stem}.gpkg'
    if out_path.exists() and not OVERWRITE:
        logging.info('Skipping %s, output already exists', csv_path.name)
        return {'file': csv_path.name, 'status': 'skipped', 'points': None}
    points = csv_to_points(csv_path)
    points.to_file(out_path, layer='subwards')
    logging.info('Converted %s : %d points', csv_path.name, len(points))
    return {'file': csv_path.name, 'status': 'done', 'points': len(points)}


def main():
    start = time.perf_counter()
    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)
    results = []
    for csv_path in sorted(INPUT_FOLDER.glob('*.csv')):
        try:
            results.append(process_one(csv_path))
        except Exception as error:
            logging.error('failed on %s : %s', csv_path.name, error)
            results.append(
                {'file': csv_path.name, 'status': 'failed', 'points': None}
            )
    if not results:
        logging.warning('No csv files found in %s', INPUT_FOLDER)
        return
    summary = pd.DataFrame(results)
    summary['points'] = summary['points'].astype('Int64')
    summary.to_csv(SUMMARY_FILE, index=False)
    elapsed = time.perf_counter() - start
    logging.info('Finished %d files in %.1f seconds', len(results), elapsed)
    print(summary)


if __name__=='__main__':
    main()



