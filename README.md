
## Getting started

1. Clone this repository, cd into it. 

2. With Anaconda3 installed (link to conda) run: 
    conda create -n fredapi
    conda activate fredapi

3. Install the package in development mode 
    pip install -e .

4. Verify the install 
    python 
    from fredapi import run

5. Set environment variables
    cp .env.example .env

6. Go take a minute to read run.py, this is the entrypoint to all FRED requests. 

## Usage 

Run a simple test: 
    <pre>
    ```python  
    from fredapi import run  
    print(run.run_series_updates())  
    ```</pre>

This will print the first and last 5 rows of the most recently updated series 
This doesn't however, retreive the observed values that were updated to the series. 

To do this we can take note of the id (series_id) and date: 
    <pre>```python  
    from fredapi import run  
    df = run.run_series_updates()  
    for row in df.loc[:,['id', 'title, 'last_updated']].itertuples(index=False):  
        print(f"{row.title}:\n{run.run_series_observations(series_id=row.id, observation_start=row.last_updated)}") ```</pre>
        
Will effortlessly fetch and print the series title and observations from that series. (I recommend adding a delay.)
Likely you will find it easier to create a batch file to collect data from instead of the CLI. 
Take a look at test/test.py to see usage examples of every possible FRED endpoint. 
Following this, you'll want to peek at fredapi/parameters.py to see what types of arguments can be made for each endpoint.


## In progress 
Currently, all endpoints make successful requests with required only parameters. 
Except for series/observations - which cleans datetime objects
All functions can and will break when passed: 
    -Obscure arguments: like an extremely unpopular category id, discontinued series id, search text with certain symbols 

Issues with string formatting are next up on the boilerplate.

Automated filesave: 
    -In /data_pipeline (currently obsolete) DataFrames and parameters passed here to automate the organization, naming, and saving of datasets. 
    -Maybe xlsx, likely csv. 

MatplotLib: 
    -Graphing, matching, statarb, etc. 


## License

This project is licensed under the [CC BY-NC 4.0 License](https://creativecommons.org/licenses/by-nc/4.0/).