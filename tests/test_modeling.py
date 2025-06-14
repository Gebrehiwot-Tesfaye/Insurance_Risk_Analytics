import pandas as pd
from src import modeling

def test_fit_linear_regression():
    data = {'X1': [1, 2, 3, 4], 'X2': [2, 3, 4, 5], 'y': [2, 4, 6, 8]}
    df = pd.DataFrame(data)
    model, preds, r2, mse = modeling.fit_linear_regression(df, ['X1', 'X2'], 'y')
    assert hasattr(model, 'predict')
    assert len(preds) == len(df)
    assert isinstance(r2, float)
    assert isinstance(mse, float)

def test_fit_random_forest():
    data = {'X1': [1, 2, 3, 4, 5], 'X2': [2, 3, 4, 5, 6], 'y': [2, 4, 6, 8, 10]}
    df = pd.DataFrame(data)
    model, X_test, y_test, y_pred, importances = modeling.fit_random_forest(df, ['X1', 'X2'], 'y')
    assert hasattr(model, 'predict')
    assert len(y_pred) == len(y_test) 