import pandas as pd
from src import eda

def test_describe_data():
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)
    desc = eda.describe_data(df)
    assert 'A' in desc.columns or 'A' in desc.index
    assert 'B' in desc.columns or 'B' in desc.index 