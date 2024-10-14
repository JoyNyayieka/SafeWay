from flask import Flask, request, jsonify
import osmnx as ox
from routing import find_optimal_route
from crime_data import assign_crime_severity
#from traffic import assign_traffic_data
from visualize import visualize_route
from data_processing import preprocess_crime_data

# Create an instance of the Flask class
app = Flask(__name__)

# Load your road network
graph = ox.graph_from_place('Nairobi, Kenya', network_type='drive')

# Load preprocessed crime data 
crime_data = preprocess_crime_data('Nairobi_Crime_Hotspots.csv')  
crime_data = crime_data.to_dict(orient='records') #Convert DataFrame to a list of dictionaries

# Assign crime severity and traffic data
graph = assign_crime_severity(graph, crime_data)
#graph = assign_traffic_data(graph, api_key='replace this with API key')

# Define the home route for the web application
@app.route('/')
def home():
    return "SafeWay App Running!"

# Define a route for finding the optimal route
@app.route('/find-route', methods=['POST'])
def find_route():
    # Extract start and end points from the request
    data = request.get_json()
    start_lat = data['start_lat']
    start_lon = data['start_lon']
    end_lat = data['end_lat']
    end_lon = data['end_lon']

    # Find the optimal route
    optimal_route = find_optimal_route(graph, start_lat, start_lon, end_lat, end_lon)

    # Visualize the route
    visualize_route(graph, optimal_route)

    return jsonify({'route': optimal_route})

if __name__ == "__main__":
    app.run(debug=True)



