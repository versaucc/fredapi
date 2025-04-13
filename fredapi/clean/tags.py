import json, os
import pandas as pd

# JSON to Pandas DataFrame for tags requests. 

def _tags(data):
    """
    Extracts tag metadata from the 'tags' key in a FRED JSON response.

    Parameters:
        data (dict): Raw JSON response containing a 'tags' key

    Returns:
        pd.DataFrame: Cleaned DataFrame with selected tag metadata fields
    """
    fields = ["name", "group_id", "notes", "created", "popularity", "series_count"]
    df = pd.DataFrame(data["tags"])[fields]

    df["created"] = pd.to_datetime(df["created"], errors="coerce")
    df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce")
    df["series_count"] = pd.to_numeric(df["series_count"], errors="coerce")

    return df

def related_tags(data):
    """
    Extracts related tag metadata from the 'tags' key in a FRED JSON response.

    Parameters:
        data (dict): Raw JSON response containing a 'tags' key

    Returns:
        pd.DataFrame: Cleaned DataFrame with selected related tag metadata fields
    """
    fields = ["name", "group_id", "notes", "created", "popularity", "series_count"]
    df = pd.DataFrame(data["tags"])[fields]

    df["created"] = pd.to_datetime(df["created"], errors="coerce")
    df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce")
    df["series_count"] = pd.to_numeric(df["series_count"], errors="coerce")

    return df

def tags_series(data):
    """
    Extracts series metadata from the 'seriess' key in a FRED JSON response related to a tag.

    Parameters:
        data (dict): Raw JSON response containing a 'seriess' key

    Returns:
        pd.DataFrame: Cleaned DataFrame with selected series metadata fields
    """
    fields = [
        "id", "realtime_start", "realtime_end", "title", "observation_start", "observation_end",
        "frequency", "frequency_short", "units", "units_short", "seasonal_adjustment",
        "seasonal_adjustment_short", "last_updated", "popularity", "group_popularity", "notes"
    ]

    df = pd.DataFrame(data["seriess"])[fields]

    date_fields = ["realtime_start", "realtime_end", "observation_start", "observation_end", "last_updated"]
    for col in date_fields:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce")
    df["group_popularity"] = pd.to_numeric(df["group_popularity"], errors="coerce")

    return df