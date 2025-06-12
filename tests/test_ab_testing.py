import pandas as pd
from src import ab_testing

def test_t_test_by_group():
    data = {'Group': ['A', 'A', 'B', 'B'], 'Value': [1, 2, 3, 4]}
    df = pd.DataFrame(data)
    results = ab_testing.t_test_by_group(df, 'Group', 'Value')
    assert ('A', 'B') in results
    assert 't_stat' in results[('A', 'B')]
    assert 'p_value' in results[('A', 'B')]

def test_chi2_test_by_group():
    data = {'Group': ['A', 'A', 'B', 'B'], 'Cat': ['X', 'Y', 'X', 'Y']}
    df = pd.DataFrame(data)
    chi2, p, dof, expected = ab_testing.chi2_test_by_group(df, 'Group', 'Cat')
    assert isinstance(chi2, float)
    assert isinstance(p, float) 