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
def run_category(**kwargs):
    params = prm.category
    params.update(kwargs)
    return fred.make_request(params)

def run_category_children(category_id, **kwargs):
    params = prm.category_children
    params['category_id'] = category_id
    params.update(kwargs)
    return fred.make_request(params)

def run_category_related(category_id, **kwargs):
    params = prm.category_related
    params['category_id'] = category_id
    params.update(kwargs)
    return fred.make_request(params)

def run_category_series(category_id, **kwargs):
    params = prm.category_series
    params['category_id'] = category_id
    params.update(kwargs)
    return fred.make_request(params)

def run_category_tags(category_id, **kwargs):
    params = prm.category_tags
    params['category_id'] = category_id
    params.update(kwargs)
    return fred.make_request(params)

def run_category_related_tags(category_id, tag_names, **kwargs):
    params = prm.category_related_tags
    params['tag_names'] = ut.clean_string(tag_names, replacement=';')
    params['category_id'] = category_id
    params.update(kwargs)
    return fred.make_request(params)

# --- Releases ---
def run_releases(**kwargs):
    params = prm.releases
    params.update(kwargs)
    return fred.make_request(params)

def run_releases_dates(**kwargs):
    params = prm.releases_dates
    params.update(kwargs)
    return fred.make_request(params)

def run_release(release_id, **kwargs):
    params = prm.release
    params['release_id'] = release_id
    params.update(kwargs)
    return fred.make_request(params)

def run_release_dates(release_id, **kwargs):
    params = prm.release_dates
    params['release_id'] = release_id
    params.update(kwargs)
    return fred.make_request(params)

def run_release_series(release_id, **kwargs):
    params = prm.release_series
    params['release_id'] = release_id
    params.update(kwargs)
    return fred.make_request(params)

def run_release_sources(release_id, **kwargs):
    params = prm.release_sources
    params['release_id'] = release_id
    params.update(kwargs)
    return fred.make_request(params)

def run_release_tags(release_id, **kwargs):
    params = prm.release_tags
    params['release_id'] = release_id
    params.update(kwargs)
    return fred.make_request(params)

def run_release_related_tags(release_id, tag_names, **kwargs):
    params = prm.release_related_tags
    params['tag_names'] = ut.clean_string(tag_names, ";")
    params['release_id'] = release_id
    params.update(kwargs)
    return fred.make_request(params)

def run_release_tables(release_id, **kwargs):
    params = prm.release_tables
    params['release_id'] = release_id
    params.update(kwargs)
    return fred.make_request(params)

# --- Series ---
def run_series(series_id, **kwargs):
    params = prm.series
    params['series_id'] = series_id
    params.update(kwargs)
    return fred.make_request(params)

def run_series_categories(series_id, **kwargs):
    params = prm.series_categories
    params['series_id'] = series_id
    params.update(kwargs)
    return fred.make_request(params)

def run_series_observations(series_id, **kwargs):
    params = prm.series_observations
    params['series_id'] = series_id
    params.update(kwargs)
    params = ut.clean_datetime_values(params)
    return fred.make_request(params)

def run_series_release(series_id, **kwargs):
    params = prm.series_release
    params['series_id'] = series_id
    params.update(kwargs)
    return fred.make_request(params)

def run_series_search(search_text, **kwargs):
    params = prm.series_search
    params['search_text'] = ut.clean_string(search_text, replacement="+")
    params.update(kwargs)
    return fred.make_request(params)

def run_series_search_tags(series_search_text, **kwargs):
    params = prm.series_search_tags
    params['series_search_text'] = ut.clean_string(series_search_text, replacement="+")
    params.update(kwargs)
    return fred.make_request(params)

def run_series_search_related_tags(tag_names, **kwargs):
    params = prm.series_search_related_tags
    params['tag_names'] = ut.clean_string(tag_names, replacement=";")
    params.update(kwargs)
    return fred.make_request(params)

def run_series_tags(series_id, **kwargs):
    params = prm.series_tags
    params['series_id'] = series_id
    params.update(kwargs)
    return fred.make_request(params)

def run_series_updates(**kwargs):
    params = prm.series_updates
    params.update(kwargs)
    return fred.make_request(params)

def run_series_vintagedates(series_id, **kwargs):
    params = prm.series_vintagedates
    params['series_id'] = series_id
    params.update(kwargs)
    return fred.make_request(params)

# --- Sources ---
def run_sources(**kwargs):
    params = prm.sources
    params.update(kwargs)
    return fred.make_request(params)

def run_source(source_id, **kwargs):
    params = prm.source
    params['source_id'] = source_id
    params.update(kwargs)
    return fred.make_request(params)

def run_source_releases(source_id, **kwargs):
    params = prm.source_releases
    params['source_id'] = source_id
    params.update(kwargs)
    return fred.make_request(params)


# --- Tags ---
def run_tags(**kwargs):
    params = prm.tags
    params.update(kwargs)
    return fred.make_request(params)


def run_related_tags(tag_names, **kwargs):
    params = prm.related_tags
    params['tag_names'] = ut.clean_string(tag_names, ";")
    params.update(kwargs)
    return fred.make_request(params)


def run_tags_series(tag_names, **kwargs):
    params = prm.tags_series
    params['tag_names'] = ut.clean_string(tag_names, ";")
    params.update(kwargs)
    return fred.make_request(params)

