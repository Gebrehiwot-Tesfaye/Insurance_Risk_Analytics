"""
ab_testing.py
Module for A/B hypothesis testing functions.
"""

import pandas as pd
from scipy import stats

def t_test_by_group(df: pd.DataFrame, group_col: str, value_col: str):
    """
    Perform pairwise t-tests between groups for a given value column.
    Args:
        df (pd.DataFrame): Input data.
        group_col (str): Column to group by (e.g., 'Province', 'Gender').
        value_col (str): Value column to compare (e.g., 'TotalClaims').
    Returns:
        dict: Results of t-tests between each pair of groups.
    """
    results = {}
    groups = df[group_col].dropna().unique()
    for i, g1 in enumerate(groups):
        for g2 in groups[i+1:]:
            vals1 = df[df[group_col] == g1][value_col].dropna()
            vals2 = df[df[group_col] == g2][value_col].dropna()
            t_stat, p_val = stats.ttest_ind(vals1, vals2, equal_var=False)
            results[(g1, g2)] = {'t_stat': t_stat, 'p_value': p_val}
    return results

def chi2_test_by_group(df: pd.DataFrame, group_col: str, value_col: str):
    """
    Perform a chi-squared test for independence between a categorical group and a binary/categorical value column.
    Args:
        df (pd.DataFrame): Input data.
        group_col (str): Grouping column (e.g., 'Province', 'Gender').
        value_col (str): Categorical value column (e.g., 'StatutoryRiskType').
    Returns:
        float: Chi-squared statistic, p-value, degrees of freedom, expected frequencies.
    """
    contingency = pd.crosstab(df[group_col], df[value_col])
    chi2, p, dof, expected = stats.chi2_contingency(contingency)
    return chi2, p, dof, expected 