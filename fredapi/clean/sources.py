import json, os
import pandas as pd

# JSON to Pandas DataFrame for source requests. 

def _sources(data):
    """
    Extracts metadata for all sources from the 'sources' key in a FRED JSON response.

    Parameters:
        data (dict): Raw JSON response containing a 'sources' key

    Returns:
        pd.DataFrame: Cleaned DataFrame with source ID, name, link, and date fields
    """

    fields = ["id", "realtime_start", "realtime_end", "name", "link"]
    df = pd.DataFrame(data["sources"])[fields]

    df["realtime_start"] = pd.to_datetime(df["realtime_start"], errors="coerce")
    df["realtime_end"] = pd.to_datetime(df["realtime_end"], errors="coerce")

    return df

def source(data):
    """
    Extracts metadata for a single source from the 'sources' key in a FRED JSON response.

    Parameters:
        data (dict): Raw JSON response containing a single-source 'sources' key

    Returns:
        pd.DataFrame: Cleaned DataFrame with source ID, name, link, and date fields
    """

    fields = ["id", "realtime_start", "realtime_end", "name", "link"]
    df = pd.DataFrame(data["sources"])[fields]

    df["realtime_start"] = pd.to_datetime(df["realtime_start"], errors="coerce")
    df["realtime_end"] = pd.to_datetime(df["realtime_end"], errors="coerce")

    return df

def source_releases(data):
    """
    Extracts release metadata from the 'releases' key in a FRED JSON response related to a source.

    Parameters:
        data (dict): Raw JSON response containing a 'releases' key

    Returns:
        pd.DataFrame: Cleaned DataFrame with selected release metadata fields
    """

    fields = ["id", "realtime_start", "realtime_end", "name", "press_release", "link"]
    df = pd.DataFrame(data["releases"])[fields]

    df["realtime_start"] = pd.to_datetime(df["realtime_start"], errors="coerce")
    df["realtime_end"] = pd.to_datetime(df["realtime_end"], errors="coerce")

    return df