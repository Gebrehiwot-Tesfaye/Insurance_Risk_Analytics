"""
data_loader.py
Module for loading and cleaning the insurance dataset.
"""

import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    """
    Load the insurance dataset from a .txt file.
    Args:
        filepath (str): Path to the data file.
    Returns:
        pd.DataFrame: Loaded data.
    """
    df = pd.read_csv(filepath, delimiter='\t')
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the dataset: handle missing values, correct dtypes.
    Args:
        df (pd.DataFrame): Raw data.
    Returns:
        pd.DataFrame: Cleaned data.
    """
    # Fill missing numerical values with median
    num_cols = df.select_dtypes(include='number').columns
    for col in num_cols:
        df[col].fillna(df[col].median(), inplace=True)
    # Convert date columns if present
    if 'TransactionMonth' in df.columns:
        df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'], errors='coerce')
    return df 