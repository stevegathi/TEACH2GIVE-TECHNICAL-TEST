import pandas as pd
import numpy as np

# Function to generate random data for the model
def generate_data(num_samples=25000):
    years = np.random.randint(2000, 2025, size=num_samples)
    areas = [f"Area_{i}" for i in np.random.randint(1, 1001, size=num_samples)]
    rainfall = np.random.uniform(1000, 10000, size=num_samples)
    production = np.random.randint(100, 1001, size=num_samples)
    fertilizer = np.random.uniform(50, 800, size=num_samples)
    yield_data = np.random.uniform(1, 20, size=num_samples)

    data = {
        'Year': years,
        'Area': areas,
        'Rainfall': rainfall,
        'Production': production,
        'Fertilizer': fertilizer,
        'Yield': yield_data,
    }

    return data

# Generate data and create a DataFrame
model_data = generate_data()
df = pd.DataFrame(model_data)

# Save DataFrame to a CSV file
df.to_csv('model_data.csv', index=False)

# Display the DataFrame
print(df.head())
print(df.shape)
