import json, os
import pandas as pd

# JSON to Pandas DataFrame for series requests. 

def _series(data):
    """
    Helper function to clean data 

    Parameters
    ----------
        data: Raw JSON output 

    Returns: Pandas DataFrame
    """
    print("Cleaning series info...")
    fields = [
        "id", "realtime_start", "realtime_end", "title", "observation_start",
        "observation_end", "frequency", "frequency_short", "units", "units_short",
        "seasonal_adjustment", "seasonal_adjustment_short", "last_updated", 
        "popularity", "notes"
    ]

    df = pd.DataFrame(data["seriess"])[fields]

    date_cols = [
        "realtime_start", "realtime_end", "observation_start",
        "observation_end", "last_updated"
    ]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    if "popularity" in df.columns:
        df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce")
    
    print(f"...Complete")
    return df

def series_categories(data):
    """
    Extracts category metadata from the 'categories' key in a FRED JSON response.

    Parameters:
        data (dict): Raw JSON response containing a 'categories' key

    Returns:
        pd.DataFrame: Cleaned DataFrame with category ID, name, and parent ID
    """
    print("Cleaning series/categories info...")
    fields = ["id", "name", "parent_id"]
    df = pd.DataFrame(data["categories"])[fields]
    print("...Complete")
    return df

def series_observations(data): 
    """
    Extracts observation data from the 'observations' key in a raw JSON response

    """
    print("Cleaning observation data...")
    fields = ["realtime_start", "realtime_end", "date", "value"]
    df = pd.DataFrame(data["observations"])[fields]

    date_fields = ["realtime_start","realtime_end", "date"]
    for col in date_fields:
        df[col] = pd.to_datetime(df[col], errors="coerce")
    print("...Complete")
    return df

def series_release(data):
    """
    Extracts release metadata from the 'releases' key in a FRED JSON response.

    Parameters:
        data (dict): Raw JSON response containing a 'releases' key

    Returns:
        pd.DataFrame: Cleaned DataFrame with selected release metadata fields
    """
    print("Cleaning series/release info...")

    fields = ["id", "realtime_start", "realtime_end", "name", "press_release", "link"]
    df = pd.DataFrame(data["releases"])[fields]

    date_fields = ["realtime_start", "realtime_end"]
    for col in date_fields:
        df[col] = pd.to_datetime(df[col], errors="coerce")
    print("Series/release info cleaned...")
    return df

def series_search(data):
    """
    Extracts series metadata from the 'seriess' key in a FRED JSON response.

    Parameters:
        data (dict): Raw JSON response containing a 'seriess' key

    Returns:
        pd.DataFrame: Cleaned DataFrame with selected series metadata fields
    """
    print("Cleaning series/search results...")
    fields = [
        "id", "realtime_start", "realtime_end", "title", "observation_start", "observation_end",
        "frequency", "frequency_short", "units", "units_short", "seasonal_adjustment",
        "seasonal_adjustment_short", "last_updated", "popularity", "group_popularity", "notes"
    ]
    # print(json.dumps(data, indent=4)

    if data is not None and data['seriess']:
        df = pd.DataFrame(data["seriess"])[fields]
    else: 
        df = pd.DataFrame([['end']], columns=["value"], index=["row1"])
        return df 

    # print(df.head())

    date_fields = ["realtime_start", "realtime_end", "observation_start", "observation_end", "last_updated"]
    for col in date_fields:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    numeric_fields = ["popularity", "group_popularity"]
    for col in numeric_fields:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    print("...Complete")
    return df

def series_search_tags(data):
    """
    Extracts tag metadata from the 'tags' key in a FRED JSON response.

    Parameters:
        data (dict): Raw JSON response containing a 'tags' key

    Returns:
        pd.DataFrame: Cleaned DataFrame with selected tag metadata fields
    """
    print("Cleaning series/search_tags results...")
    fields = ["name", "group_id", "notes", "created", "popularity", "series_count"]
    df = pd.DataFrame(data["tags"])[fields]

    df["created"] = pd.to_datetime(df["created"], errors="coerce")
    df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce")
    df["series_count"] = pd.to_numeric(df["series_count"], errors="coerce")

    print("...Complete")
    return df

def series_search_related_tags(data):
    """
    Extracts related tag metadata from the 'tags' key in a FRED JSON response.

    Parameters:
        data (dict): Raw JSON response containing a 'tags' key

    Returns:
        pd.DataFrame: Cleaned DataFrame with selected related tag metadata fields
    """
    print("Cleaning series/search/related_tags results...")
    fields = ["name", "group_id", "notes", "created", "popularity", "series_count"]
    df = pd.DataFrame(data["tags"])[fields]

    df["created"] = pd.to_datetime(df["created"], errors="coerce")
    df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce")
    df["series_count"] = pd.to_numeric(df["series_count"], errors="coerce")

    return df

def series_tags(data):
    """
    Extracts tag metadata for a specific series from the 'tags' key in a FRED JSON response.

    Parameters:
        data (dict): Raw JSON response containing a 'tags' key

    Returns:
        pd.DataFrame: Cleaned DataFrame with selected tag metadata fields
    """
    print("Cleaning series/tags info...")
    fields = ["name", "group_id", "notes", "created", "popularity", "series_count"]
    df = pd.DataFrame(data["tags"])[fields]

    df["created"] = pd.to_datetime(df["created"], errors="coerce")
    df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce")
    df["series_count"] = pd.to_numeric(df["series_count"], errors="coerce")

    print("...Complete")
    return df

def series_updates(data):
    """
    Extracts recently updated series metadata from the 'seriess' key in a FRED JSON response.

    Parameters:
        data (dict): Raw JSON response containing a 'seriess' key

    Returns:
        pd.DataFrame: Cleaned DataFrame with selected series metadata fields
    """
    print("Cleaning series/updates data...")
    fields = [
        "id", "realtime_start", "realtime_end", "title", "observation_start", "observation_end",
        "frequency", "frequency_short", "units", "units_short", "seasonal_adjustment",
        "seasonal_adjustment_short", "last_updated", "popularity"
    ]

    df = pd.DataFrame(data["seriess"])[fields]

    date_fields = ["realtime_start", "realtime_end", "observation_start", "observation_end", "last_updated"]
    for col in date_fields:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce")

    return df

def series_vintagedates(data):
    """
    Extracts vintage dates from the 'vintage_dates' key in a FRED JSON response.

    Parameters:
        data (dict): Raw JSON response containing a 'vintage_dates' key

    Returns:
        pd.DataFrame: Cleaned DataFrame with a single datetime column of vintage dates
    """
    print("Cleaning series/vintagedates data...")
    df = pd.DataFrame({"vintage_date": pd.to_datetime(data["vintage_dates"], errors="coerce")})
    print("...Complete")
    return df

