# Insurance Risk Analytics

This project analyzes historical car insurance claim data for AlphaCare Insurance Solutions (ACIS) to optimize marketing strategy and identify low-risk clients for premium reduction. The analysis covers EDA, A/B testing, and predictive modeling, with modular code and clear documentation.

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

## Business Objective

Help ACIS optimize marketing and discover low-risk targets for premium reduction using historical data and analytics.

### Key Analysis Areas

1. **Exploratory Data Analysis (EDA)**

   - Data Understanding and Quality Assessment
   - Univariate and Bivariate Analysis
   - Geographic and Temporal Analysis
   - Outlier Detection
   - Creative Visualizations

2. **Statistical Analysis**

   - Loss Ratio Analysis by Province, Vehicle Type, and Gender
   - A/B Testing for Risk Differences
   - Correlation Analysis
   - Outlier Detection and Treatment

3. **Predictive Modeling**
   - Linear Regression for Total Claims Prediction
   - Machine Learning for Optimal Premium Prediction
   - Feature Importance Analysis

### Analysis Components

1. **Data Summarization**

   - Descriptive Statistics
   - Data Structure Review
   - Missing Value Analysis

2. **Univariate Analysis**

   - Distribution of Key Variables
   - Histograms and Bar Charts
   - Statistical Distributions

3. **Bivariate Analysis**

   - Correlation Analysis
   - Scatter Plots
   - Geographic Patterns

4. **Temporal Analysis**

   - Monthly Trends
   - Seasonal Patterns
   - Claim Frequency Analysis

5. **Geographic Analysis**

   - Provincial Risk Profiles
   - Regional Patterns
   - Location-based Insights

6. **Vehicle Analysis**
   - Make/Model Risk Assessment
   - Vehicle Type Analysis
   - Custom Value Analysis

### Key Metrics

1. **Financial Metrics**

   - Loss Ratio (TotalClaims/TotalPremium)
   - Average Premium
   - Average Claim Amount
   - Profit Margins

2. **Risk Metrics**
   - Claim Frequency
   - Claim Severity
   - Risk Profiles by Category

### Deliverables

1. **Analysis Notebooks**

   - EDA and Visualization
   - Statistical Testing
   - Predictive Modeling

2. **Documentation**

   - Code Documentation
   - Analysis Reports
   - Recommendations

3. **Visualizations**
   - Risk Profile Heatmaps
   - Geographic Distribution Maps
   - Temporal Trend Charts

## Key Findings

1. **Risk Analysis**

   - Provincial Risk Variations
   - Vehicle Type Risk Profiles
   - Gender-based Risk Differences

2. **Temporal Patterns**

   - Monthly Claim Trends
   - Seasonal Variations
   - Policy Growth Patterns

3. **Geographic Insights**
   - Regional Risk Clusters
   - Provincial Performance
   - Location-based Opportunities

## Recommendations

1. **Marketing Strategy**

   - Target low-risk segments
   - Adjust premiums based on risk profiles
   - Focus on high-potential regions

2. **Risk Management**

   - Implement preventive measures
   - Optimize coverage for high-risk areas
   - Develop risk mitigation strategies

3. **Product Development**
   - Customize products for different segments
   - Develop new products for underserved markets
   - Enhance existing coverage options

## Future Work

1. **Advanced Analytics**

   - Deep Learning Models
   - Real-time Risk Assessment
   - Predictive Maintenance

2. **Product Enhancement**

   - Dynamic Pricing Models
   - Personalized Coverage Options
   - Risk-based Discounts

3. **Market Expansion**
   - New Geographic Markets
   - Additional Vehicle Types
   - Enhanced Coverage Options
