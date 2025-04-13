import json 
# FRED API Parameter Dictionaries

## --- CATEGORIES ---

category = {
    "request_type" : "category",
    "category_id": 0  # (Optional) integer, e.g. 0 (default: root category)
}

category_children = {
    "request_type" : "category/children",
    "category_id": 0,                      # (Optional) integer, default: 0
    "realtime_start": None,               # (Optional) string, default: None, e.g. "2020-01-01"
    "realtime_end": None                  # (Optional) string, default: None, e.g. "2025-01-01"
}

category_related = {
    "request_type" : "category/related",
    "category_id": None,                  # (Required) integer, e.g. 95
    "realtime_start": None,              # (Optional) string, default: None
    "realtime_end": None                 # (Optional) string, default: None
}

category_series = {
    "request_type" : "category/series",
    "category_id": None,                 # (Required) integer, e.g. 95
    "realtime_start": None,             # (Optional) string, default: None
    "realtime_end": None,               # (Optional) string, default: None
    "limit": 1000,                      # (Optional) integer, default: 1000
    "offset": 0,                        # (Optional) integer, default: 0
    "order_by": "series_id",            # (Optional) string, default: "series_id"
    "sort_order": "asc",                # (Optional) string, default: "asc"
    "filter_variable": None,            # (Optional) string, default: None
    "filter_value": None,               # (Optional) string, default: None
    "tag_names": None,                  # (Optional) string, default: None
    "exclude_tag_names": None           # (Optional) string, default: None
}

category_tags = {
    "request_type" : "category/tags",
    "category_id": None,                # (Required) integer, e.g. 32145
    "realtime_start": None,            # (Optional) string, default: None
    "realtime_end": None,              # (Optional) string, default: None
    "tag_names": None,                 # (Optional) string, default: None
    "tag_group_id": None,              # (Optional) string, default: None
    "search_text": None,               # (Optional) string, default: None
    "limit": 1000,                     # (Optional) integer, default: 1000
    "offset": 0,                       # (Optional) integer, default: 0
    "order_by": "series_count",        # (Optional) string, default: "series_count"
    "sort_order": "asc"                # (Optional) string, default: "asc"
}

category_related_tags = {
    "request_type" : "category/related_tags",
    "category_id": None,              # (Required) integer
    "realtime_start": None,           # (Optional) string, default: None
    "realtime_end": None,             # (Optional) string, default: None
    "tag_names": None,                # (Required) string
    "exclude_tag_names": None,        # (Optional) string, default: None
    "tag_group_id": None,             # (Optional) string, default: None
    "search_text": None,              # (Optional) string, default: None
    "limit": 1000,                    # (Optional) integer, default: 1000
    "offset": 0,                      # (Optional) integer, default: 0
    "order_by": "series_count",       # (Optional) string, default: "series_count"
    "sort_order": "asc"               # (Optional) string, default: "asc"
}


## --- RELEASES ---

releases = {
    "request_type" : "releases",
    "realtime_start": None,           # (Optional) string, default: None
    "realtime_end": None,             # (Optional) string, default: None
    "limit": 1000,                    # (Optional) integer, default: 1000
    "offset": 0,                      # (Optional) integer, default: 0
    "order_by": "release_id",         # (Optional) string, default: "release_id"
    "sort_order": "asc"               # (Optional) string, default: "asc"
}

releases_dates = {
    "request_type" : "releases/dates",
    "realtime_start": None,                          # (Optional) string, default: None
    "realtime_end": None,                            # (Optional) string, default: None
    "limit": 1000,                                   # (Optional) integer, default: 1000
    "offset": 0,                                     # (Optional) integer, default: 0
    "order_by": "release_date",                      # (Optional) string, default: "release_date"
    "sort_order": "desc",                            # (Optional) string, default: "desc"
    "include_release_dates_with_no_data": "false"    # (Optional) string, default: "false"
}

release = {
    "request_type" : "release",
    "release_id": None,           # (Required) integer
    "realtime_start": None,       # (Optional) string, default: None
    "realtime_end": None          # (Optional) string, default: None
}

release_dates = {
    "request_type" : "release/dates",
    "release_id": None,                             # (Required) integer
    "realtime_start": None,                         # (Optional) string, default: None
    "realtime_end": None,                           # (Optional) string, default: None
    "limit": 10000,                                 # (Optional) integer, default: 10000
    "offset": 0,                                    # (Optional) integer, default: 0
    "sort_order": "asc",                            # (Optional) string, default: "asc"
    "include_release_dates_with_no_data": "false"   # (Optional) string, default: "false"
}

release_series = {
    "request_type" : "release/series",
    "release_id": None,              # (Required) integer
    "realtime_start": None,          # (Optional) string, default: None
    "realtime_end": None,            # (Optional) string, default: None
    "limit": 1000,                   # (Optional) integer, default: 1000
    "offset": 0,                     # (Optional) integer, default: 0
    "order_by": "series_id",         # (Optional) string, default: "series_id"
    "sort_order": "asc",             # (Optional) string, default: "asc"
    "filter_variable": None,         # (Optional) string, default: None
    "filter_value": None,            # (Optional) string, default: None
    "tag_names": None,               # (Optional) string, default: None
    "exclude_tag_names": None        # (Optional) string, default: None
}

release_sources = {
    "request_type" : "release/sources",
    "release_id": None,             # (Required) integer
    "realtime_start": None,         # (Optional) string, default: None
    "realtime_end": None            # (Optional) string, default: None
}

release_tags = {
    "request_type" : "release/tags",
    "release_id": None,             # (Required) integer
    "realtime_start": None,         # (Optional) string, default: None
    "realtime_end": None,           # (Optional) string, default: None
    "tag_names": None,              # (Optional) string, default: None
    "tag_group_id": None,           # (Optional) string, default: None
    "search_text": None,            # (Optional) string, default: None
    "limit": 1000,                  # (Optional) integer, default: 1000
    "offset": 0,                    # (Optional) integer, default: 0
    "order_by": "series_count",     # (Optional) string, default: "series_count"
    "sort_order": "asc"             # (Optional) string, default: "asc"
}

release_related_tags = {
    "request_type" : "release/related_tags",
    "release_id": None,             # (Required) integer
    "realtime_start": None,         # (Optional) string, default: None
    "realtime_end": None,           # (Optional) string, default: None
    "tag_names": None,              # (Required) string
    "exclude_tag_names": None,      # (Optional) string, default: None
    "tag_group_id": None,           # (Optional) string, default: None
    "search_text": None,            # (Optional) string, default: None
    "limit": 1000,                  # (Optional) integer, default: 1000
    "offset": 0,                    # (Optional) integer, default: 0
    "order_by": "series_count",     # (Optional) string, default: "series_count"
    "sort_order": "asc"             # (Optional) string, default: "asc"
}

release_tables = {
    "request_type" : "release/tables",
    "release_id": None,                        # (Required) integer
    "element_id": None,                        # (Optional) integer, default: None
    "include_observation_values": "false",     # (Optional) string, default: "false"
    "observation_date": None                   # (Optional) string, default: None
}


# -----SERIES----- 
series = {
    "request_type" : "series",
    'series_id': None,  # required, e.g. 'GDP'
    'realtime_start': None,  # optional, default: today's date, e.g. '2023-01-01'
    'realtime_end': None,  # optional, default: today's date, e.g. '2024-01-01'
}

series_categories = {
    "request_type" : "series/categories",
    'series_id': None,  # required, e.g. 'GDP'
    'realtime_start': None,  # optional, default: today's date, e.g. '2023-01-01'
    'realtime_end': None,  # optional, default: today's date, e.g. '2024-01-01'
}

series_observations = {
    "request_type" : "series/observations",
    'series_id': None,  # required, e.g. 'GDP'
    'realtime_start': None,  # optional, default: today's date, e.g. '2023-01-01'
    'realtime_end': None,  # optional, default: today's date, e.g. '2024-01-01'
    'limit': None,  # optional, default: 100000, e.g. 5000
    'offset': None,  # optional, default: 0, e.g. 100
    'sort_order': None,  # optional, default: 'asc', values: 'asc', 'desc'
    'observation_start': None,  # optional, default: '1776-07-04', e.g. '2000-01-01'
    'observation_end': None,  # optional, default: '9999-12-31', e.g. '2023-01-01'
    'units': None,  # optional, default: 'lin', e.g. 'chg', 'pch', 'log'
    'frequency': None,  # optional, default: no value, e.g. 'm', 'q', 'a'
    'aggregation_method': None,  # optional, default: 'avg', values: 'avg', 'sum', 'eop'
    'output_type': None,  # optional, default: 1, values: 1, 2, 3, 4
    'vintage_dates': None,  # optional, e.g. '2000-01-01,2005-02-24'
}

series_release = {
    "request_type" : "series/release",
    'series_id': None,  # required, e.g. 'GDP'
    'realtime_start': None,  # optional, default: today's date
    'realtime_end': None,  # optional, default: today's date
}

series_search = {
    "request_type" : "series/search",
    'search_text': None,  # required, e.g. 'Real GDP'
    'search_type': None,  # optional, default: 'full_text', values: 'full_text', 'series_id'
    'realtime_start': None,  # optional, default: today's date
    'realtime_end': None,  # optional, default: today's date
    'limit': None,  # optional, default: 1000
    'offset': None,  # optional, default: 0
    'order_by': None,  # optional, default varies, e.g. 'popularity', 'title'
    'sort_order': None,  # optional, default varies, values: 'asc', 'desc'
    'filter_variable': None,  # optional, e.g. 'units'
    'filter_value': None,  # optional, e.g. 'Index 2012=100'
    'tag_names': None,  # optional, e.g. 'usa;gdp'
    'exclude_tag_names': None,  # optional, must be used with tag_names, e.g. 'discontinued'
}

series_search_tags = {
    "request_type" : "series/search/tags",
    'series_search_text': None,  # required, e.g. 'money stock'
    'realtime_start': None,  # optional, default: today's date
    'realtime_end': None,  # optional, default: today's date
    'tag_names': None,  # optional, e.g. 'm1;m2'
    'tag_group_id': None,  # optional, e.g. 'gen', 'geo'
    'tag_search_text': None,  # optional, e.g. 'inflation'
    'limit': None,  # optional, default: 1000
    'offset': None,  # optional, default: 0
    'order_by': None,  # optional, default: 'series_count'
    'sort_order': None,  # optional, default: 'asc'
}

series_search_related_tags = {
    "request_type" : "series/search/related_tags",
    'series_search_text': None,  # required, e.g. 'interest rate'
    'realtime_start': None,  # optional, default: today's date
    'realtime_end': None,  # optional, default: today's date
    'tag_names': None,  # required, e.g. '30-year;frb'
    'exclude_tag_names': None,  # optional, e.g. 'discontinued;monthly'
    'tag_group_id': None,  # optional, e.g. 'src'
    'tag_search_text': None,  # optional, e.g. 'bond'
    'limit': None,  # optional, default: 1000
    'offset': None,  # optional, default: 0
    'order_by': None,  # optional, default: 'series_count'
    'sort_order': None,  # optional, default: 'asc'
}

series_tags = {
    "request_type" : "series/tags",
    'series_id': None,  # required, e.g. 'GDP'
    'realtime_start': None,  # optional, default: today's date
    'realtime_end': None,  # optional, default: today's date
    'order_by': None,  # optional, default: 'series_count'
    'sort_order': None,  # optional, default: 'asc'
}

series_updates = {
    "request_type" : "series/updates",
    'realtime_start': None,  # optional, default: today's date
    'realtime_end': None,  # optional, default: today's date
    'limit': None,  # optional, default: 1000
    'offset': None,  # optional, default: 0
    'filter_value': None,  # optional, default: 'all', values: 'macro', 'regional', 'all'
    'start_time': None,  # optional, format: 'YYYYMMDDHmm', e.g. '202303021420'
    'end_time': None,  # optional, format: 'YYYYMMDDHmm', e.g. '202303021500'
}

series_vintagedates = {
    "request_type" : "series/vintagedates",
    'series_id': None,  # required, e.g. 'GDP'
    'realtime_start': None,  # optional, default: '1776-07-04'
    'realtime_end': None,  # optional, default: '9999-12-31'
    'limit': None,  # optional, default: 10000
    'offset': None,  # optional, default: 0
    'sort_order': None,  # optional, default: 'asc'
}

#-----SOURCES-----
sources = {
    "request_type" : "sources",
    'realtime_start': None,  # optional, default: today's date, e.g. '2023-01-01'
    'realtime_end': None,  # optional, default: today's date, e.g. '2023-12-31'
    'limit': None,  # optional, default: 1000, integer between 1 and 1000
    'offset': None,  # optional, default: 0, non-negative integer
    'order_by': None,  # optional, default: 'source_id', e.g. 'name', 'realtime_start'
    'sort_order': None,  # optional, default: 'asc', values: 'asc', 'desc'
}

source = {
    "request_type" : "source",
    'source_id': None,  # required, integer, e.g. 18
    'realtime_start': None,  # optional, default: today's date
    'realtime_end': None,  # optional, default: today's date
}

source_releases = {
    "request_type" : "source/releases",
    'source_id': None,  # required, integer, e.g. 18
    'realtime_start': None,  # optional, default: today's date
    'realtime_end': None,  # optional, default: today's date
    'limit': None,  # optional, default: 1000
    'offset': None,  # optional, default: 0
    'order_by': None,  # optional, default: 'release_id', e.g. 'name', 'press_release'
    'sort_order': None,  # optional, default: 'asc'
}

# ----TAGS-----
tags = {
    "request_type" : "tags",
    'realtime_start': None,  # optional, default: today's date
    'realtime_end': None,  # optional, default: today's date
    'tag_names': None,  # optional, e.g. 'gdp;oecd'
    'tag_group_id': None,  # optional, e.g. 'geo', 'src', 'seas'
    'search_text': None,  # optional, e.g. 'inflation'
    'limit': None,  # optional, default: 1000
    'offset': None,  # optional, default: 0
    'order_by': None,  # optional, default: 'series_count'
    'sort_order': None,  # optional, default: 'asc'
}

related_tags = {
    "request_type" : "related_tags",
    'realtime_start': None,  # optional, default: today's date
    'realtime_end': None,  # optional, default: today's date
    'tag_names': None,  # required, e.g. 'monetary+aggregates;weekly'
    'exclude_tag_names': None,  # optional, e.g. 'discontinued;currency'
    'tag_group_id': None,  # optional, e.g. 'geo', 'gen', 'src'
    'search_text': None,  # optional, e.g. 'growth'
    'limit': None,  # optional, default: 1000
    'offset': None,  # optional, default: 0
    'order_by': None,  # optional, default: 'series_count'
    'sort_order': None,  # optional, default: 'asc'
}

tags_series = {
    "request_type" : "tags/series",
    'tag_names': None,  # required, e.g. 'slovenia;food'
    'exclude_tag_names': None,  # optional, e.g. 'alcohol;quarterly'
    'realtime_start': None,  # optional, default: today's date
    'realtime_end': None,  # optional, default: today's date
    'limit': None,  # optional, default: 1000
    'offset': None,  # optional, default: 0
    'order_by': None,  # optional, default: 'series_id'
    'sort_order': None,  # optional, default: 'asc'
}