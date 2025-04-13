from datetime import datetime, timedelta, date
import pandas as pd 
from urllib.parse import urlencode
import fredapi.utils as ut


# Example parameters passed to request.py: 
# Parameters should be built and passed in a way that can be seamlessly encoded into a URL 


class FredRequest: 
    base_url = "https://api.stlouisfed.org/fred"
    
    def __init__(self, params: dict, chunk=False):
        self.chunk = False
        self.params = params
        
    def get_params(self): 
        return self.params

    def build_url(self, parameters): 
        """
        Builds the URL for a given FRED request. 

        Parameters:
            parameters: dict 
        Returns: 
            url_str: string
        """
        try: 
            req_type = parameters['request_type']
            parameters['request_type'] = None # Avoid encoding this into the URL 

            clean_params = {k: v for k, v in parameters.items() if v is not None}

            query = urlencode(clean_params)
            clean_query = query.replace("%2B", "+")
            base = self.base_url

            # Complete URL - minus user api key and filetype. 
            url_str = f"{base}/{req_type}?{clean_query}"
            print(url_str + ' ...Built')
            parameters['request_type'] = req_type
            return url_str
        except Exception as e: 
            print(f"[ERROR] building URL: {e}")
            return None

    def clean_params(self) -> dict:
        """
        Helper function to clean parameters of a FredRequest object 
        Ignores "None" and converts datetime to string. 
        """
        params = self.params
        cleaned = {}
        for k, v in params.items():
            if v is None:
                continue
            if isinstance(v, (datetime, pd.Timestamp)):
                cleaned[k] = v.strftime("%Y-%m-%d")
            else:
                cleaned[k] = v
        return cleaned

    def get_batch(self):
        """
        Retrieves a URL or batch of URLs for a FRED request 
        """
        return self.build_url(self.params)




