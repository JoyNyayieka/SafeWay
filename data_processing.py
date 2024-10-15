import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def load_crime_data(file_path):
    df = pd.read_csv(file_path)
    crime_data = df.to_dict(orient='records')  # Convert the DataFrame to a list of dictionaries
    return crime_data

def preprocess_crime_data(data_path):
    # Load dataset
    dataset = load_crime_data(data_path)  # Use the load function here

    # Normalize crime severity if you have a 'Severity' column
    scaler = MinMaxScaler()

    # Convert the list of dictionaries back to a DataFrame for normalization
    df = pd.DataFrame(dataset)
    
    # Check if 'Severity' column exists for normalization
    if 'Severity' in df.columns:
        df['normalized_severity'] = scaler.fit_transform(df[['Severity']])
    
    # Convert back to a list of dictionaries
    processed_data = df.to_dict(orient='records')
    
    # Return the processed dataset
    return processed_data

# Example usage (uncomment when you want to test)
#processed_data = preprocess_crime_data('Nairobi_Crime_Hotspots.csv')
