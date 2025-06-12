"""
eda.py
Module for exploratory data analysis (EDA) functions.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def describe_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return descriptive statistics for numerical columns.
    Args:
        df (pd.DataFrame): Input data.
    Returns:
        pd.DataFrame: Descriptive statistics.
    """
    return df.describe()

def plot_distributions(df: pd.DataFrame, columns: list):
    """
    Plot histograms for numerical columns and bar charts for categorical columns.
    Args:
        df (pd.DataFrame): Input data.
        columns (list): List of columns to plot.
    """
    for col in columns:
        plt.figure(figsize=(6, 4))
        if pd.api.types.is_numeric_dtype(df[col]):
            sns.histplot(df[col].dropna(), kde=True)
            plt.title(f'Histogram of {col}')
        else:
            df[col].value_counts().plot(kind='bar')
            plt.title(f'Bar chart of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()

def plot_correlations(df: pd.DataFrame, columns: list):
    """
    Plot a correlation matrix heatmap for selected numerical columns.
    Args:
        df (pd.DataFrame): Input data.
        columns (list): List of numerical columns.
    """
    corr = df[columns].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.show()

def detect_outliers(df: pd.DataFrame, columns: list):
    """
    Plot boxplots to detect outliers in numerical columns.
    Args:
        df (pd.DataFrame): Input data.
        columns (list): List of numerical columns.
    """
    for col in columns:
        plt.figure(figsize=(6, 4))
        sns.boxplot(x=df[col])
        plt.title(f'Boxplot of {col}')
        plt.xlabel(col)
        plt.tight_layout()
        plt.show() 