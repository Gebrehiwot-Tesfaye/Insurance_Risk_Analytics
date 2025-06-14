# Insurance Risk Analytics

This project analyzes historical car insurance claim data for AlphaCare Insurance Solutions (ACIS) to optimize marketing strategy and identify low-risk clients.

## Project Structure

```
Insurance_Risk_Analytics/
├── data/                      # Data directory
│   └── MachineLearningRating_v3.txt  # Historical insurance data
├── notebooks/                 # Jupyter notebooks
│   ├── eda_visualization.ipynb    # EDA and visualization analysis
│   └── modeling.ipynb            # Predictive modeling
├── src/                      # Source code
│   ├── data_loader.py        # Data loading and preprocessing
│   ├── eda.py               # Exploratory data analysis functions
│   ├── modeling.py          # Modeling functions
│   └── utils.py             # Utility functions
├── requirements.txt          # Project dependencies
└── README.md                # Project documentation
```

## Setup

1. Create and activate virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run notebooks in `notebooks/` for analysis and visualization.

## Data Version Control (DVC) Setup

1. Install DVC:

   ```bash
   pip install dvc
   ```

2. Initialize DVC:

   ```bash
   dvc init
   ```

3. Set up local storage:

   ```bash
   mkdir dvc_storage
   dvc remote add -d localstorage ./dvc_storage
   ```

4. Add data to DVC:

   ```bash
   dvc add data/MachineLearningRating_v3.txt
   ```

5. Commit DVC changes:

   ```bash
   git add .dvc/config data/MachineLearningRating_v3.txt.dvc
   git commit -m "Add data file to DVC tracking"
   ```

6. Push data to storage:
   ```bash
   dvc push
   ```

## Analysis Components

1. **Exploratory Data Analysis (EDA)**

   - Data quality assessment
   - Univariate and bivariate analysis
   - Geographic and temporal analysis
   - Outlier detection

2. **Statistical Analysis**

   - Loss ratio analysis
   - A/B testing
   - Correlation analysis

3. **Predictive Modeling**
   - Claims prediction
   - Premium optimization
   - Feature importance

## Key Metrics

- Loss Ratio (TotalClaims/TotalPremium)
- Claim Frequency
- Average Premium
- Risk Profiles

## Deliverables

- EDA and visualization notebooks
- Statistical analysis reports
- Predictive models
- Recommendations for marketing strategy
