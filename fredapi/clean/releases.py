import json, os
import pandas as pd

# JSON to Pandas DataFrame for releases requests. 

def _releases(data):
    """
    Extracts release metadata from the 'releases' key in a FRED JSON response.

    Parameters:
        data (dict): Raw JSON response containing a 'releases' key

    Returns:
        pd.DataFrame: Cleaned DataFrame with selected release metadata fields
    """

    fields = ["id", "realtime_start", "realtime_end", "name", "press_release", "link"]
    df = pd.DataFrame(data["releases"])[fields]

    date_fields = ["realtime_start", "realtime_end"]
    for col in date_fields:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    return df

def releases_dates(data):
    """
    Extracts release date metadata from the 'release_dates' key in a FRED JSON response.

    Parameters:
        data (dict): Raw JSON response containing a 'release_dates' key

    Returns:
        pd.DataFrame: Cleaned DataFrame with selected release date fields
    """

    fields = ["release_id", "release_name", "date"]
    df = pd.DataFrame(data["release_dates"])[fields]

    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    return df

def release(data):
    """
    Extracts single release metadata from the 'releases' key in a FRED JSON response.

    Parameters:
        data (dict): Raw JSON response containing a 'releases' key

    Returns:
        pd.DataFrame: Cleaned DataFrame with selected release metadata fields
    """

    fields = ["id", "realtime_start", "realtime_end", "name", "press_release", "link"]
    df = pd.DataFrame(data["releases"])[fields]

    date_fields = ["realtime_start", "realtime_end"]
    for col in date_fields:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    return df

def release_dates(data):
    """
    Extracts release dates from the 'release_dates' key in a FRED JSON response.

    Parameters:
        data (dict): Raw JSON response containing a 'release_dates' key

    Returns:
        pd.DataFrame: Cleaned DataFrame with release IDs and corresponding dates
    """

    fields = ["release_id", "date"]
    df = pd.DataFrame(data["release_dates"])[fields]

    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    return df

def release_series(data):
    """
    Extracts series metadata from the 'seriess' key in a FRED JSON response related to a release.

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

def release_sources(data):
    """
    Extracts source metadata from the 'sources' key in a FRED JSON response related to a release.

    Parameters:
        data (dict): Raw JSON response containing a 'sources' key

    Returns:
        pd.DataFrame: Cleaned DataFrame with selected source metadata fields
    """

    fields = ["id", "realtime_start", "realtime_end", "name", "link"]
    df = pd.DataFrame(data["sources"])[fields]

    date_fields = ["realtime_start", "realtime_end"]
    for col in date_fields:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    return df

def release_tags(data):
    """
    Extracts tag metadata from the 'tags' key in a FRED JSON response related to a release.

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


def release_related_tags(data):
    """
    Extracts related tag metadata from the 'tags' key in a FRED JSON response related to a release.

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

def release_tables(data):
    """
    Extracts table structure metadata from a FRED JSON response related to a release table hierarchy.

    Parameters:
        data (dict): Raw JSON response containing table metadata

    Returns:
        pd.DataFrame: Flattened DataFrame containing table elements with hierarchical information
    """

    def flatten_elements(elements, parent=None):
        rows = []
        for elem in elements.values():
            row = {
                "element_id": elem.get("element_id"),
                "release_id": elem.get("release_id"),
                "series_id": elem.get("series_id"),
                "parent_id": elem.get("parent_id"),
                "line": elem.get("line"),
                "type": elem.get("type"),
                "name": elem.get("name"),
                "level": elem.get("level")
            }
            rows.append(row)
            if "children" in elem and isinstance(elem["children"], list):
                for child in elem["children"]:
                    rows.append({
                        "element_id": child.get("element_id"),
                        "release_id": child.get("release_id"),
                        "series_id": child.get("series_id"),
                        "parent_id": child.get("parent_id"),
                        "line": child.get("line"),
                        "type": child.get("type"),
                        "name": child.get("name"),
                        "level": child.get("level")
                    })
        return rows

    root_elements = data.get("elements", {})
    flat_data = flatten_elements(root_elements)
    df = pd.DataFrame(flat_data)
    return df