import requests
import pandas as pd
import time
import json, os

from dotenv import load_dotenv
from .build_request import FredRequest
from .request_types import FRED_ENDPOINTS
import fredapi.utils as ut 

class Fred:
    max_results_per_request = 1000
    max_results_per_observation_request = 2000

    def __init__(self, api_key=None, proxies=None):

        load_dotenv()
        self.api_key = os.getenv("FRED_API_KEY")

        if not proxies:
            http_proxy = os.getenv('HTTP_PROXY')
            https_proxy = os.getenv('HTTPS_PROXY')
            if http_proxy or https_proxy:
                proxies = {}
                if http_proxy:
                    proxies['http'] = http_proxy
                if https_proxy:
                    proxies['https'] = https_proxy

        self.proxies = proxies or {}

    def get_data(self, url):
        """
        Helper function to make an API request and retrieve the json output. 
        Parameters: 
            -url: string, built in FredRequest 
        Returns: 
            -data: raw json output
        """
        url += '&api_key=' + self.api_key + '&file_type=json'
        df = {}
        try:
            if self.proxies is None:
                response = requests.get(url)
                data = response.json()
                # print(json.dumps(data, indent=4)) # Debug for viewing raw output 
                print(f"JSON data fetched...")
                return data
            elif self.proxies is not None:
                response = requests.get(url, self.proxies)
                data = response.json()
                # print(json.dumps(data, indent=4)) # Debug for viewing raw output 
                return data
        except requests.exceptions.HTTPError as e:
            try:
                error_data = response.json()
                raise ValueError(f"API Error: {error_data.get('message', str(e))}")
            except Exception:
                raise ValueError(f"HTTP Error occurred: {e}")
    
    def make_request(self, parameters : dict, chunk=False):
        """
        Function to make a FRED request
        Parameters:
            parameters : dict
                -unique to each type of FRED request
                -See parameters.py to see how each request is structured. 
        Returns:
            -df: Pandas DataFrame
        """
        # Create a FredRequest object 
        freq = FredRequest(parameters)
        print(f"FredRequest object built for: {parameters['request_type']}")
        # Raw JSON is passed to FRED_ENDPOINTS at key 'request_type' where data is cleaned 
        try:
            request_type = parameters.get("request_type")
            if not request_type or request_type not in FRED_ENDPOINTS:
                raise ValueError(f"Invalid or missing request_type: {request_type}")

            raw_data = self.get_data(freq.get_batch())
            return FRED_ENDPOINTS[request_type](raw_data)

        except Exception as e:
            print(f"[ERROR] FRED request failed: {e}")
            return None

