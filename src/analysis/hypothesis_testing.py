import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
from typing import Tuple, Dict, List

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load and preprocess the insurance data.
    
    Args:
        file_path (str): Path to the data file
        
    Returns:
        pd.DataFrame: Processed dataframe
    """
    # Read the data with the correct separator
    df = pd.read_csv(file_path, sep='|')
    return df

def calculate_risk_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate risk metrics (Claim Frequency and Claim Severity) for the dataset.
    
    Args:
        df (pd.DataFrame): Input dataframe
        
    Returns:
        pd.DataFrame: Dataframe with calculated metrics
    """
    # Calculate claim frequency (proportion of policies with claims)
    df['has_claim'] = df['TotalClaims'] > 0
    
    # Calculate claim severity (average claim amount when claim occurs)
    df['claim_severity'] = df.apply(
        lambda x: x['TotalClaims'] if x['has_claim'] else 0, 
        axis=1
    )
    
    # Calculate margin
    df['margin'] = df['TotalPremium'] - df['TotalClaims']
    
    return df

def test_provincial_risk_differences(df: pd.DataFrame) -> Tuple[float, float, pd.DataFrame]:
    """
    Test hypothesis: There are no risk differences across provinces
    
    Args:
        df (pd.DataFrame): Processed dataframe with risk metrics
        
    Returns:
        Tuple[float, float, pd.DataFrame]: p-value, test statistic, and summary statistics
    """
    # Group by province and calculate metrics
    provincial_stats = df.groupby('Province').agg({
        'has_claim': ['mean', 'count'],
        'claim_severity': ['mean', 'std']
    })
    
    # Perform ANOVA test for claim frequency
    provinces = df['Province'].unique()
    claim_freq_groups = [df[df['Province'] == p]['has_claim'] for p in provinces]
    f_stat, p_value = stats.f_oneway(*claim_freq_groups)
    
    return p_value, f_stat, provincial_stats

def test_zipcode_risk_differences(df: pd.DataFrame) -> Tuple[float, float, pd.DataFrame]:
    """
    Test hypothesis: There are no risk differences between zip codes
    
    Args:
        df (pd.DataFrame): Processed dataframe with risk metrics
        
    Returns:
        Tuple[float, float, pd.DataFrame]: p-value, test statistic, and summary statistics
    """
    # Group by postal code and calculate metrics
    zip_stats = df.groupby('PostalCode').agg({
        'has_claim': ['mean', 'count'],
        'claim_severity': ['mean', 'std']
    })
    
    # Perform ANOVA test for claim frequency
    zipcodes = df['PostalCode'].unique()
    claim_freq_groups = [df[df['PostalCode'] == z]['has_claim'] for z in zipcodes]
    f_stat, p_value = stats.f_oneway(*claim_freq_groups)
    
    return p_value, f_stat, zip_stats

def test_zipcode_margin_differences(df: pd.DataFrame) -> Tuple[float, float, pd.DataFrame]:
    """
    Test hypothesis: There are no significant margin differences between zip codes
    
    Args:
        df (pd.DataFrame): Processed dataframe with risk metrics
        
    Returns:
        Tuple[float, float, pd.DataFrame]: p-value, test statistic, and summary statistics
    """
    # Group by postal code and calculate margin statistics
    zip_margin_stats = df.groupby('PostalCode')['margin'].agg(['mean', 'std', 'count'])
    
    # Perform ANOVA test for margins
    zipcodes = df['PostalCode'].unique()
    margin_groups = [df[df['PostalCode'] == z]['margin'] for z in zipcodes]
    f_stat, p_value = stats.f_oneway(*margin_groups)
    
    return p_value, f_stat, zip_margin_stats

def test_gender_risk_differences(df: pd.DataFrame) -> Tuple[float, float, pd.DataFrame]:
    """
    Test hypothesis: There are no significant risk differences between Women and Men
    
    Args:
        df (pd.DataFrame): Processed dataframe with risk metrics
        
    Returns:
        Tuple[float, float, pd.DataFrame]: p-value, test statistic, and summary statistics
    """
    # Group by gender and calculate metrics
    gender_stats = df.groupby('Gender').agg({
        'has_claim': ['mean', 'count'],
        'claim_severity': ['mean', 'std']
    })
    
    # Perform t-test for claim frequency
    male_claims = df[df['Gender'] == 'M']['has_claim']
    female_claims = df[df['Gender'] == 'F']['has_claim']
    t_stat, p_value = stats.ttest_ind(male_claims, female_claims)
    
    return p_value, t_stat, gender_stats

def run_all_hypothesis_tests(df: pd.DataFrame) -> Dict:
    """
    Run all hypothesis tests and return results
    
    Args:
        df (pd.DataFrame): Processed dataframe with risk metrics
        
    Returns:
        Dict: Dictionary containing all test results
    """
    results = {
        'provincial_risk': test_provincial_risk_differences(df),
        'zipcode_risk': test_zipcode_risk_differences(df),
        'zipcode_margin': test_zipcode_margin_differences(df),
        'gender_risk': test_gender_risk_differences(df)
    }
    
    return results

def interpret_results(results: Dict) -> Dict:
    """
    Interpret the statistical test results and provide business recommendations
    
    Args:
        results (Dict): Dictionary containing all test results
        
    Returns:
        Dict: Dictionary containing interpretations and recommendations
    """
    interpretations = {}
    alpha = 0.05  # significance level
    
    for test_name, (p_value, stat, stats_df) in results.items():
        interpretation = {
            'p_value': p_value,
            'test_statistic': stat,
            'reject_null': p_value < alpha,
            'summary_stats': stats_df.to_dict() if isinstance(stats_df, pd.DataFrame) else stats_df
        }
        
        # Add business interpretation
        if p_value < alpha:
            interpretation['business_implication'] = f"Reject null hypothesis for {test_name}. "
            interpretation['business_implication'] += "There is statistically significant evidence of differences. "
            interpretation['business_implication'] += "Consider adjusting pricing or risk assessment strategies accordingly."
        else:
            interpretation['business_implication'] = f"Fail to reject null hypothesis for {test_name}. "
            interpretation['business_implication'] += "No statistically significant evidence of differences found. "
            interpretation['business_implication'] += "Current pricing and risk assessment strategies may be appropriate."
            
        interpretations[test_name] = interpretation
    
    return interpretations

if __name__ == "__main__":
    # Load and process data
    df = load_data("../../data/MachineLearningRating_v3.txt")
    df = calculate_risk_metrics(df)
    
    # Run all hypothesis tests
    results = run_all_hypothesis_tests(df)
    
    # Interpret results
    interpretations = interpret_results(results)
    
    # Print results
    for test_name, interpretation in interpretations.items():
        print(f"\n{test_name.upper()} TEST RESULTS:")
        print(f"P-value: {interpretation['p_value']:.4f}")
        print(f"Test Statistic: {interpretation['test_statistic']:.4f}")
        print(f"Decision: {'Reject' if interpretation['reject_null'] else 'Fail to reject'} null hypothesis")
        print(f"Business Implication: {interpretation['business_implication']}") 