import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_crime_data(data_path):

    # Load dataset
    dataset = pd.read_csv(data_path)

    # Normalize crime severity
    scaler = MinMaxScaler()
    dataset['normalized_severity'] = scaler.fit_transform(dataset[['Severity']])

    # Return the processed dataset
    return dataset

processed_data = preprocess_crime_data('Nairobi_Crime_Hotspots.csv')
