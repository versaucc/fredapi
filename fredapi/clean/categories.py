import json, os
import pandas as pd

# JSON to Pandas DataFrame for category requests. 


def category(data):
    """
    Extracts category metadata from the 'categories' key in a FRED JSON response.

    Parameters:
        data (dict): Raw JSON response containing a 'categories' key

    Returns:
        pd.DataFrame: Cleaned DataFrame with category ID, name, and parent ID
    """
    print("Cleaning category data...")
    # print(json.dumps(data, indent=4))
    fields = ["id", "name", "parent_id"]
    df = pd.DataFrame(data["categories"])
    return df

def category_children(data):
    """
    Extracts child category metadata from the 'categories' key in a FRED JSON response.

    Parameters:
        data (dict): Raw JSON response containing a 'categories' key

    Returns:
        pd.DataFrame: Cleaned DataFrame with category ID, name, and parent ID
    """

    fields = ["id", "name", "parent_id"]
    df = pd.DataFrame(data["categories"])[fields]
    return df

def category_related(data): 
    """
    Extracts related categories metadata from the 'catgories' key in a FRED JSON response. 
    
    """
    fields = ["id", "name", "parent_id"]
    df = pd.DataFrame(data["categories"])[fields]
    return df

def category_series(data):
    """
    Extracts series metadata from the 'seriess' key in a FRED JSON response related to a category.

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

    numeric_fields = ["popularity", "group_popularity"]
    for col in numeric_fields:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df

def category_tags(data):
    """
    Extracts tag metadata from the 'tags' key in a FRED JSON response related to a category.

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

def category_related_tags(data):
    """
    Extracts related tag metadata from the 'tags' key in a FRED JSON response related to a category.

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