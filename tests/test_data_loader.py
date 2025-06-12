import pytest
import pandas as pd
from src import data_loader

def test_load_data():
    # Test loading a small sample file
    df = data_loader.load_data('data/MachineLearningRating_v3.txt')
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_clean_data():
    # Test cleaning a small DataFrame
    data = {'A': [1, None, 3], 'TransactionMonth': ['2020-01', '2020-02', None]}
    df = pd.DataFrame(data)
    cleaned = data_loader.clean_data(df)
    assert cleaned['A'].isnull().sum() == 0
    assert pd.api.types.is_datetime64_any_dtype(cleaned['TransactionMonth']) 