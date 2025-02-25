## Livability Score
This project aims to predict property risk based on multiple environmental and infrastructure factors using machine learning techniques.

1. Project Overview
Real estate risks, such as crime rate, power outages, air quality, and neighborhood reviews, play a crucial role in determining property values and insurance policies. This project uses machine learning models to assess and predict the risk of a given property.

2. Dataset
The dataset used is train.csv, loaded from Google Drive. It contains various features related to property attributes, neighborhood safety, and environmental conditions.

Features in the Dataset
Property_Type - Categorical (House, Apartment, etc.)
Property_Area - Numeric (Square feet)
Number_of_Windows - Numeric
Number_of_Doors - Numeric
Furnishing - Categorical (Furnished/Unfurnished)
Frequency_of_Powercuts - Numeric (Number of outages)
Power_Backup - Categorical (Yes/No)
Water_Supply - Categorical (Regular/Sporadic)
Traffic_Density_Score - Numeric (Traffic intensity in the area)
Crime_Rate - Categorical (Low, Medium, High)
Dust_and_Noise - Numeric (Air and sound pollution levels)
Air_Quality_Index - Numeric (AQI Score)
Neighborhood_Review - Numeric (User review score)
Risk_Label (Target Variable) - Binary (0: Low risk, 1: High risk)
3. Data Preprocessing
Handling Missing Values
SimpleImputer from sklearn.impute is used to replace missing values:
Mean imputation for numerical features.
Most frequent value imputation for categorical features.
Feature Engineering
Categorical variables are converted into numerical values using one-hot encoding.
Standardization is applied to numeric features.
4. Model Training
Train-test split: 80% training, 20% testing.
Machine Learning Models Used:
Decision Trees
Random Forest
Logistic Regression
Gradient Boosting
Evaluation Metrics:
Accuracy
Precision, Recall, F1-score
ROC Curve & AUC Score
5. Installation & Setup
Prerequisites
Python 3.x
Jupyter Notebook
Google Colab (if using cloud-based execution)
Required Libraries
Install dependencies using:

sh
Copy
Edit
pip install numpy pandas matplotlib seaborn scikit-learn
6. Running the Notebook
Open Mini_Project_Final_py.ipynb in Jupyter Notebook or Google Colab.
Ensure the dataset (train.csv) is accessible from Google Drive.
Run all the cells to preprocess data, train models, and analyze results.
7. Results & Visualizations
Feature Importance: Identifies the most critical factors affecting property risk.
Confusion Matrix: Shows model performance in classifying risks.
Accuracy Scores: Compares different ML models.
Risk Distribution Plots: Visualizes data trends.
8. Future Improvements
Add deep learning models (e.g., ANN) for better accuracy.
Use real-time data from APIs to enhance predictions.
Deploy as a web-based application for user-friendly risk assessment.
