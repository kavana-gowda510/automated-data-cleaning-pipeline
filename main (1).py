import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# load dataset
data = pd.read_csv("student_data.csv")

print("Dataset Loaded")

# ---------------------------
# Missing Value Check
# ---------------------------

print("\nMissing Values:")
print(data.isnull().sum())

# ---------------------------
# KNN Imputation
# ---------------------------

numeric_data = data.select_dtypes(include=['int64','float64'])

imputer = KNNImputer(n_neighbors=3)
data[numeric_data.columns] = imputer.fit_transform(numeric_data)

print("\nMissing values handled using KNN Imputer")

# ---------------------------
# Outlier Detection
# ---------------------------

iso = IsolationForest(contamination=0.05)

outliers = iso.fit_predict(data[numeric_data.columns])

data = data[outliers == 1]

print("\nOutliers removed using Isolation Forest")

# ---------------------------
# Feature Scaling
# ---------------------------

scaler = StandardScaler()

data[numeric_data.columns] = scaler.fit_transform(data[numeric_data.columns])

print("\nData scaled using StandardScaler")

# ---------------------------
# Save Clean Dataset
# ---------------------------

data.to_csv("clean_data.csv", index=False)

print("\nClean dataset saved as clean_data.csv")