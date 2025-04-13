import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from fredapi.fred import Fred
import json, dotenv, time
from dotenv import load_dotenv
import pandas as pd 
import logging

"""
TODO:  
    Implement 
        -category search
        -tag search 
        -release tracker (newest releases, calendar, most popular)

"""

# Setup
log_file = "data_pipeline/fetch/logs/fetch.log"
os.makedirs("logs", exist_ok=True) 

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Paths to save data: 
abs_path = './data/raw'
observation_path = 'data/raw/observation_data'
series_search_path = 'data/raw/series_search'
category_series_path = 'data/raw/categories'

load_dotenv()
api = os.getenv('FRED_API_KEY')
fred = Fred(api) # init Fred object 

def fetch_series_search(search):
    """
    Run a series search with given keywords. 
    Parameters
    ----------
        params: dictionary 
            required: request_type, search_text (spaced by "+")

    Returns
    -------
        csv_path: a path to the csv that search data was written to
        title: Search keywords cleansed of bad characters

    """
    params = { 
        'request_type' : 'series/search',
        'search_text' : search, 
        'realtime_start' : None,
        'offset' : 0
    }

    title = clean_filename(params['search_text'])

    df= fred.make_request(params)
    print("Search complete...")

    csv_path = f"{series_search_path}/{title}_series_search_data.csv"
    os.makedirs(series_search_path, exist_ok=True)

    df.to_csv(csv_path, mode='a', header=not os.path.exists(csv_path), index=False)
    return csv_path, title


def observations_from_series(file_path, name): 
    """
    Loops through a stored set of series, fetches their observations saves them in their own folder. 

    Parameters
    ----------
        file_path: the path to the csv containing the series ids you want to query

    Returns: None, appends observations to their own directory.

    """
    logging.info(f"Started observations batch: {name}")

    title = f"{name}_observation_data"
    folder = f"{observation_path}/{title}"
    os.makedirs(folder, exist_ok=True) # Make a folder for all observation data to be held

    df = pd.read_csv(file_path)
    
    for i, item in enumerate(df['id']):
        try:  
            obs_title = clean_filename(df.at[i, 'title'])
            params = {
                'request_type': 'series/observations',
                'series_id' : item, 
                'offset' : 0

            }
            #Make the request 
            data = fred.make_request(params)
            print(f"Fetched data for: {obs_title}")
            time.sleep(5) # Wait...
            csv_path = os.path.join(folder, f"{obs_title}_observation_data.csv")

            # Write it directly
            data.to_csv(csv_path, index=False)
            logging.info(f"{obs_title}Written to file: {csv_path}")

        except Exception as e: 
            print(f"[ERROR] Failed for series_id={item}: {e}")
            logging.info(f"{obs_title}Written to file: {title} FAILURE : - {e}")
            continue  # move on to the next series

# fetch_series_search()

# observations_from_series('data/raw/series_search/monetary_service_index_series_search_data.csv', 'monetary_service_index')

def large_search_batch():
    # Run multiple series searches and collect the series data. 
    from params import search_batch as sb 
    filenames = []
    for item in sb: 
        try:
            csv_path, folder_name = fetch_series_search(item)
            observations_from_series(csv_path, folder_name)
            
        except Exception as e: 
            print(f"[ERROR] failed for search={item} : {e}")
            continue
    """
        TODO: 
        Clean up fred.py 
        Clean filenames - main cause of failure
        Clean the rest of the modules - ready for publish
    """

def clean_filename(filename):
        cleaned = filename.replace(" ", "_")
        cleaned = cleaned.replace(",", "")
        cleaned= cleaned.replace(".", "")
        cleaned= cleaned.replace(":", "")
        cleaned = cleaned.replace("+", "_")
        return cleaned

fetch_series_search('Interest+rate+swaps')
