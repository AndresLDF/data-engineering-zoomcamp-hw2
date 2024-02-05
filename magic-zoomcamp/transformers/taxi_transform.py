from mage_ai.data_cleaner.transformer_actions.base import BaseAction
from mage_ai.data_cleaner.transformer_actions.constants import ActionType, Axis
from mage_ai.data_cleaner.transformer_actions.utils import build_transformer_action
from pandas import DataFrame
import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def execute_transformer_action(df: DataFrame, *args, **kwargs) -> DataFrame:
    #Passanger count and trip distance >0
    df_transformed = df[df['passenger_count']>0]
    df_transformed = df_transformed[df_transformed['trip_distance']>0]
    
    df_transformed['lpep_pickup_datetime'] = pd.to_datetime(df_transformed['lpep_pickup_datetime'])
    df_transformed['lpep_dropoff_datetime'] = pd.to_datetime(df_transformed['lpep_dropoff_datetime'])
    df_transformed['lpep_pickup_date'] = df_transformed['lpep_pickup_datetime'].dt.date
    df_transformed['lpep_dropoff_date'] = df_transformed['lpep_dropoff_datetime'].dt.date

    old_columns = df_transformed.columns
    df_transformed.columns = df_transformed.columns.str.lower().str.replace(' ', '_')

    print(f'The total number of changed columns name is: {(df_transformed.columns != old_columns).sum()}')

    return df_transformed


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output.vendorid.sum(), 'Vendor Id does not exist'
    assert (output[output['passenger_count'] == 0])['passenger_count'].sum() == 0, 'The output is undefined'
    assert (output[output['trip_distance'] == 0])['passenger_count'].sum() == 0, 'The output is undefined'


