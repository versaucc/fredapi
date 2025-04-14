from .fred import Fred
from . import parameters as prm
from . import utils as ut
import json, os 
import pandas as pd

"""
Run functions for each request type.
Handling parameters for each
"""

fred = Fred() # init Fred object 

# --- Categories ---

# Get a category from a category ID, if no args defaults to category 0
def run_category(**kwargs):
    params = prm.category
    params.update(kwargs)
    return fred.make_request(params)

# Get the child categories for a specified parent category.
def run_category_children(category_id, **kwargs):
    params = prm.category_children
    params['category_id'] = category_id
    params.update(kwargs)
    return fred.make_request(params)

# Get the related categories for a category.
def run_category_related(category_id, **kwargs):
    params = prm.category_related
    params['category_id'] = category_id
    params.update(kwargs)
    return fred.make_request(params)

# Get the series in a category.
def run_category_series(category_id, **kwargs):
    params = prm.category_series
    params['category_id'] = category_id
    params.update(kwargs)
    return fred.make_request(params)

# Get the tags for a category.
def run_category_tags(category_id, **kwargs):
    params = prm.category_tags
    params['category_id'] = category_id
    params.update(kwargs)
    return fred.make_request(params)

# Get the related tags for a category.
def run_category_related_tags(category_id, tag_names, **kwargs):
    params = prm.category_related_tags
    params['tag_names'] = ut.clean_string(tag_names, replacement=';')
    params['category_id'] = category_id
    params.update(kwargs)
    return fred.make_request(params)

# --- Releases ---

# Get all releases of economic data
def run_releases(**kwargs):
    params = prm.releases
    params.update(kwargs)
    return fred.make_request(params)

# Get release dates for all releases of economic data.
def run_releases_dates(**kwargs):
    params = prm.releases_dates
    params.update(kwargs)
    return fred.make_request(params)

# Get a release of economic data.
def run_release(release_id, **kwargs):
    params = prm.release
    params['release_id'] = release_id
    params.update(kwargs)
    return fred.make_request(params)

# Get release dates for a release of economic data.
def run_release_dates(release_id, **kwargs):
    params = prm.release_dates
    params['release_id'] = release_id
    params.update(kwargs)
    return fred.make_request(params)

# Get the series on a release of economic data.
def run_release_series(release_id, **kwargs):
    params = prm.release_series
    params['release_id'] = release_id
    params.update(kwargs)
    return fred.make_request(params)

# Get the sources for a release of economic data.
def run_release_sources(release_id, **kwargs):
    params = prm.release_sources
    params['release_id'] = release_id
    params.update(kwargs)
    return fred.make_request(params)

#  Get the tags for a release
def run_release_tags(release_id, **kwargs):
    params = prm.release_tags
    params['release_id'] = release_id
    params.update(kwargs)
    return fred.make_request(params)

# Get the related tags for a release.
def run_release_related_tags(release_id, tag_names, **kwargs):
    params = prm.release_related_tags
    params['tag_names'] = ut.clean_string(tag_names, ";")
    params['release_id'] = release_id
    params.update(kwargs)
    return fred.make_request(params)

# Get the release tables for a given release
def run_release_tables(release_id, **kwargs):
    params = prm.release_tables
    params['release_id'] = release_id
    params.update(kwargs)
    return fred.make_request(params)

# --- Series ---

# Get an economic data series.
def run_series(series_id, **kwargs):
    params = prm.series
    params['series_id'] = series_id
    params.update(kwargs)
    return fred.make_request(params)

# Get the categories for an economic data series.
def run_series_categories(series_id, **kwargs):
    params = prm.series_categories
    params['series_id'] = series_id
    params.update(kwargs)
    return fred.make_request(params)

# Get the observations or data values for an economic data series
def run_series_observations(series_id, **kwargs):
    params = prm.series_observations
    params['series_id'] = series_id
    params.update(kwargs)
    params = ut.clean_datetime_values(params)
    return fred.make_request(params)

# Get the release for an economic data series.
def run_series_release(series_id, **kwargs):
    params = prm.series_release
    params['series_id'] = series_id
    params.update(kwargs)
    return fred.make_request(params)

# Get economic data series that match keywords.
def run_series_search(search_text, **kwargs):
    params = prm.series_search
    params['search_text'] = ut.clean_string(search_text, replacement="+")
    params.update(kwargs)
    return fred.make_request(params)

#  Get the tags for a series search.
def run_series_search_tags(series_search_text, **kwargs):
    params = prm.series_search_tags
    params['series_search_text'] = ut.clean_string(series_search_text, replacement="+")
    params.update(kwargs)
    return fred.make_request(params)

# Get the related tags for a series search.
def run_series_search_related_tags(tag_names, **kwargs):
    params = prm.series_search_related_tags
    params['tag_names'] = ut.clean_string(tag_names, replacement=";")
    params.update(kwargs)
    return fred.make_request(params)

# Get the tags for an economic data series.
def run_series_tags(series_id, **kwargs):
    params = prm.series_tags
    params['series_id'] = series_id
    params.update(kwargs)
    return fred.make_request(params)

# Get economic data series sorted by when observations were updated on the FRED® server.
def run_series_updates(**kwargs):
    params = prm.series_updates
    params.update(kwargs)
    return fred.make_request(params)

# Get the dates in history when a series' data values were revised or new data values were released.
def run_series_vintagedates(series_id, **kwargs):
    params = prm.series_vintagedates
    params['series_id'] = series_id
    params.update(kwargs)
    return fred.make_request(params)

# --- Sources ---

# Get all sources of economic data.
def run_sources(**kwargs):
    params = prm.sources
    params.update(kwargs)
    return fred.make_request(params)

# Get a source of economic data.
def run_source(source_id, **kwargs):
    params = prm.source
    params['source_id'] = source_id
    params.update(kwargs)
    return fred.make_request(params)

# Get the releases for a source.
def run_source_releases(source_id, **kwargs):
    params = prm.source_releases
    params['source_id'] = source_id
    params.update(kwargs)
    return fred.make_request(params)


# --- Tags ---

# Get all tags, search for tags, or get tags by name.
def run_tags(**kwargs):
    params = prm.tags
    params.update(kwargs)
    return fred.make_request(params)

# Get the related tags for one or more tags.
def run_related_tags(tag_names, **kwargs):
    params = prm.related_tags
    params['tag_names'] = ut.clean_string(tag_names, ";")
    params.update(kwargs)
    return fred.make_request(params)

# Get the series matching tags.
def run_tags_series(tag_names, **kwargs):
    params = prm.tags_series
    params['tag_names'] = ut.clean_string(tag_names, ";")
    params.update(kwargs)
    return fred.make_request(params)


# ----- MAPS ------
"""
The FRED® Maps API is a web service that allows developers to write programs and build applications to harvest data 
and shape files of series available on the maps found in the FRED website hosted by the Economic Research Division of 
the Federal Reserve Bank of St. Louis. Not all series that are in FRED have geographical data.
"""

# Returns shape files from FRED in GeoJSON format (i.e. shape=bea)
def run_shape_files(shape):
    return None 

# This request returns the meta information needed to make requests for FRED data. Minimum and maximum date are also supplied for the data range available.
def run_series_group_meta(series_id): 
    return None

# This request returns a cross section of regional data for a specified release date. If no date is specified, the most recent data available are returned.
def run_series_regional_data(series_id):
    return None 