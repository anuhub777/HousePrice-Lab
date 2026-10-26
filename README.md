
# HousePrice-Lab

An end-to-end Machine Learning project focused on predicting house sale prices using Python, data analysis, and regression models.

## Objective

Build a reliable house price prediction system while exploring the complete machine learning workflow, from exploratory data analysis (EDA) and preprocessing to model training, evaluation, and optimization.

## Dataset

- **Dataset:** Ames Housing
- **Samples:** 1,460 houses
- **Features:** 79 input features after excluding the target and ID columns
- **Target variable:** `SalePrice`

The dataset contains numerical and categorical features describing house characteristics, quality, location, and amenities.

## Tech Stack

- Python
- NumPy
- Pandas
- Matplotlib and Seaborn
- Scikit-learn
- Jupyter Notebook
- Git and GitHub

## Work Completed

### 1. Exploratory Data Analysis
- Examined dataset structure, data types, and missing values.
- Analyzed the distribution of house sale prices.
- Studied relationships between sale prices and features such as overall quality and living area.
- Investigated feature correlations and potential outliers.

### 2. Data Preprocessing
- Split the data into training and testing sets.
- Imputed missing numerical values using the median.
- Handled missing categorical values.
- Applied standard scaling to numerical features.
- Applied one-hot encoding to categorical features.
- Used Scikit-learn pipelines and a `ColumnTransformer`.

### 3. Regression and Model Evaluation
- Implemented a Linear Regression baseline.
- Investigated unstable predictions and large errors.
- Applied Ridge Regression to reduce the impact of large coefficients.
- Used cross-validation and `GridSearchCV` to tune the regularization parameter.

## Current Best Model

**Model:** Ridge Regression

| Metric | Result |
|---|---:|
| Best alpha from cross-validation | 10 |
| Cross-validation MAE | $18,172.75 |
| Test MAE | $19,178.84 |
| Test RMSE | $30,524.61 |
| Test R² | 0.8785 |

These results are from the current train/test split and modeling pipeline. They may vary with different splits, preprocessing choices, or model configurations.

## Concepts Practiced

- Exploratory Data Analysis
- Missing-value imputation
- Categorical encoding
- Feature scaling
- Linear and Ridge Regression
- Regularization
- MAE, MSE, RMSE, and R²
- Cross-validation and hyperparameter tuning
- Prevention of data leakage using pipelines

## Roadmap

- [ ] Improve feature engineering and feature selection
- [ ] Compare Decision Tree and Random Forest models
- [ ] Evaluate KNN and other suitable algorithms
- [ ] Experiment with neural networks
- [ ] Explore unsupervised learning and house-price patterns
- [ ] Build an interactive prediction interface using Streamlit
- [ ] Document final model comparisons and limitations

## ▶️ Getting Started

Clone the repository:

```bash
git clone https://github.com/anuhub777/HousePrice-Lab.git
cd HousePrice-Lab
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Place the dataset in the `data/` directory before running the notebooks. Follow the dataset's original source and licensing terms.

## Author

**Anubhav Verma**

- GitHub: [anuhub777](https://github.com/anuhub777)
- LinkedIn: [Anubhav Verma](https://www.linkedin.com/in/verma-anubhav)
