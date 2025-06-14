# Insurance Risk Analytics

This project analyzes historical car insurance claim data for AlphaCare Insurance Solutions (ACIS) to optimize marketing strategy and identify low-risk clients for premium reduction. The analysis covers EDA, A/B testing, and predictive modeling, with modular code and clear documentation.

## Project Structure

# Insurance_Risk_Analytics

Insurance_Risk_Analytics/
│
├── data/
│ └── MachieLearningRating_v3.txt # Your dataset
│
├── notebooks/
│ └── 01_eda_visualization.ipynb # EDA & visualization notebook
│ └── 02_ab_testing.ipynb # A/B testing notebook
│ └── 03_modeling.ipynb # ML modeling & interpretation
│
├── src/
│ ├── **init**.py
│ ├── data_loader.py # Data loading & cleaning functions
│ ├── eda.py # EDA logic (stats, summaries)
│ ├── ab_testing.py # A/B testing logic
│ ├── modeling.py # ML/statistical modeling logic
│ └── utils.py # Utility functions
│
├── tests/
│ └── test_data_loader.py
│ └── test_eda.py
│ └── test_ab_testing.py
│ └── test_modeling.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── LICENSE

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run notebooks in `notebooks/` for analysis and visualization.

## Business Objective

Help ACIS optimize marketing and discover low-risk targets for premium reduction using historical data and analytics.
