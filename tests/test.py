from fredapi import run
 
 # Test everything with required arguments only 

# Categories
def test_categories():
    print(run.run_category()) # Passed
    print(run.run_category_children(category_id=13)) # Passed
    print(run.run_category_related(category_id=32073)) # Passed
    print(run.run_category_series(category_id=125)) # Passed
    print(run.run_category_tags(category_id=125)) # Passed
    print(run.run_category_related_tags(category_id=125, tag_names='services quarterly')) # Passed

# Releases
def test_releases():
    print(run.run_releases()) # Passed
    print(run.run_releases_dates()) # Passed
    print(run.run_release(release_id=53)) # Passed
    print(run.run_release_dates(release_id=53)) # Passed
    print(run.run_release_series(release_id=53)) # Passed
    print(run.run_release_sources(release_id=53)) # Passed
    print(run.run_release_tags(release_id=53)) # Passed
    print(run.run_release_related_tags(release_id=53, tag_names='quarterly nation')) # Passed
    print(run.run_release_tables(release_id=53)) # Passed 

# Series
def test_series():
    print(run.run_series(series_id='GNPCA')) # Passed
    print(run.run_series_categories(series_id='GNPCA')) # Passed
    print(run.run_series_observations(series_id='GNPCA')) # Passed
    print(run.run_series_release(series_id='GNPCA')) # Passed
    print(run.run_series_search(search_text='Slovenia Food Women')) # Passed
    print(run.run_series_search_tags(series_search_text='money stock')) # Passed
    print(run.run_series_search_related_tags(tag_names='nation nsa mortgage', series_search_text='interest rates')) # Passed
    print(run.run_series_tags(series_id='GNPCA')) # Passed
    print(run.run_series_updates()) # Passed
    print(run.run_series_vintagedates(series_id='GNPCA')) # Passed

# Sources
def test_sources():
    print(run.run_sources()) # Passed
    print(run.run_source(source_id=18)) # Passed
    print(run.run_source_releases(source_id=18)) # Passed

# Tags
def test_tags():
    print(run.run_tags()) # Passed
    print(run.run_related_tags(tag_names='nsa mortgage nation')) # Passed 
    print(run.run_tags_series(tag_names='nsa mortgage nation')) # Passed

# Run tests 
def test():
    # As of 04/13/2025 - All requests passed basic tests with minimal arguments. 
    test_categories() # Categories test with minimal arguments PASSED (04/13/2025)
    test_releases() # Releases test with minimal arguments PASSED (04/13/2025)
    test_series() # Series test with minimal arguments PASSED (04/13/2025)
    test_sources() # Sources test with minimal arguments PASSED (04/13/2025)
    test_tags() # Tags test with minimal arguments PASSED (04/13/2025)

test()