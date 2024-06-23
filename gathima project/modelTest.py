import pandas as pd
from joblib import load
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline, FeatureUnion
import numpy as np

class DFSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return X[self.attribute_names].values

# This is a custom transformer that adds extra attributes
class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room=True): # no *args or **kwargs
        self.add_bedrooms_per_room = add_bedrooms_per_room
        
    def fit(self, X, y=None):
        return self  # nothing else to do
    
    def transform(self, X):
        rooms_per_household = X[:, 3] / X[:, 5]
        population_per_household = X[:, 4] / X[:, 5]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, 2] / X[:, 3]
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]

    
# Load the pre-fitted full pipeline and the model
full_pipeline = load('D:\\gathima project\\full_pipeline.joblib')  # Adjust path as needed
forest_model = load('D:\\gathima project\\forest01.pkl')  # Adjust path as needed

# Features that the model expects
features = [
    'longitude', 'latitude', 'housing_median_age', 'total_rooms',
    'total_bedrooms', 'population', 'households', 'median_income', 'ocean_proximity'
]

# Collect user input for each feature
user_input = {}
for feature in features:
    if feature == 'ocean_proximity':
        print("Enter 'ocean_proximity' (options: NEAR BAY, <1H OCEAN, INLAND, NEAR OCEAN, ISLAND):")
    else:
        print(f"Enter {feature}:")
    user_input[feature] = input()

# Convert the user input into a DataFrame
input_df = pd.DataFrame([user_input])

# Ensure all numeric columns are treated as such (except 'ocean_proximity')
numeric_features = set(features) - {'ocean_proximity'}
for feature in numeric_features:
    input_df[feature] = pd.to_numeric(input_df[feature])

# Apply preprocessing to the input data using the loaded full_pipeline
input_prepared = full_pipeline.transform(input_df)

# Make a prediction with the loaded model
prediction = forest_model.predict(input_prepared)

print(f"Predicted median house value: {prediction[0]}")
