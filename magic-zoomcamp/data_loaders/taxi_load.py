import io
import pandas as pd
import requests
import gzip
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
   # Specify the year and months
    year = 2020
    months = [10, 11, 12]

    # Create a list to store the DataFrames
    data_frames = []

    # Form the file names, download, and read the CSV files
    for month in months:
        formatted_month = f"{mont}"
        file_name = f"green_tripdata_{year}-{formatted_month}.csv.gz"
        url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/{file_name}'
        
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Decompress the content
            with gzip.GzipFile(fileobj=io.BytesIO(response.content), mode='rb') as f:
                # Read the CSV file and append to the list
                data_frames.append(pd.read_csv(f, sep=','))        
        else:
            print(f"Failed to download {file_name}")

        # Concatenate the DataFrames if needed
        final_dataframe = pd.concat(data_frames, ignore_index=True)

    return final_dataframe


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
