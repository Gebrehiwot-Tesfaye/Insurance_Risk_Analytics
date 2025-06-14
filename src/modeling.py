"""
modeling.py
Module for statistical and machine learning modeling functions.
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def fit_linear_regression(df: pd.DataFrame, features: list, target: str):
    """
    Fit a linear regression model.
    Args:
        df (pd.DataFrame): Input data.
        features (list): List of feature column names.
        target (str): Target column name.
    Returns:
        model, predictions, r2, mse
    """
    X = df[features].fillna(0)
    y = df[target]
    model = LinearRegression()
    model.fit(X, y)
    preds = model.predict(X)
    r2 = r2_score(y, preds)
    mse = mean_squared_error(y, preds)
    return model, preds, r2, mse

def fit_random_forest(df: pd.DataFrame, features: list, target: str):
    """
    Fit a random forest regressor for premium prediction.
    Args:
        df (pd.DataFrame): Input data.
        features (list): List of feature column names.
        target (str): Target column name.
    Returns:
        model, X_test, y_test, y_pred, feature_importances
    """
    X = df[features].fillna(0)
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    importances = model.feature_importances_
    return model, X_test, y_test, y_pred, importances 