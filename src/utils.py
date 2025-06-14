"""
utils.py
Utility functions for the insurance analytics project.
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def encode_categorical(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Encode categorical columns using label encoding.
    Args:
        df (pd.DataFrame): Input data.
        columns (list): List of categorical columns to encode.
    Returns:
        pd.DataFrame: DataFrame with encoded columns.
    """
    df_copy = df.copy()
    for col in columns:
        le = LabelEncoder()
        df_copy[col] = le.fit_transform(df_copy[col].astype(str))
    return df_copy 