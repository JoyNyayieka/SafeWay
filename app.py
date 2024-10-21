from flask import Flask, request, jsonify, render_template
import osmnx as ox
from routing import find_optimal_route
from crime_data import assign_crime_severity
from visualize import visualize_route
from data_processing import preprocess_crime_data
import requests

# Create an instance of the Flask class
app = Flask(__name__)

# Function to geocode location using OpenWeather's Geocoding API
def geocode_location(location_name):
    api_key = "b1dace1373c6b5962f74725173816a3e"  # API key
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={location_name}&limit=1&appid={api_key}"
    
    response = requests.get(url)
    data = response.json()
    
    print(f"Geocoding API response for {location_name}: {data}")  # Debug geocoding response
    
    if len(data) > 0:
        lat = data[0]['lat']
        lon = data[0]['lon']
        return lat, lon
    else:
        raise ValueError(f"Geocoding failed for location: {location_name}")

# Define the home route for the web application
@app.route('/')
def home():
    return render_template('index.html')  # Render an HTML form for user input

# Define a route to handle form submission and find the route
@app.route('/find_route', methods=['POST'])
def find_route():
    start_location = request.form['start_location']
    end_location = request.form['end_location']

    try:
        # Geocode the start and end locations
        start_lat, start_lon = geocode_location(start_location)
        end_lat, end_lon = geocode_location(end_location)

        print(f"Start coordinates: {start_lat}, {start_lon}")
        print(f"End coordinates: {end_lat}, {end_lon}")

        # Load your road network
        try:
            graph = ox.graph_from_place('Nairobi, Kenya', network_type='drive')
            print(f"Graph loaded. Nodes: {len(graph.nodes)}, Edges: {len(graph.edges)}")
        except Exception as e:
            print(f"Error loading road network: {e}")
            return "Error loading road network. Please try again."

        # Load preprocessed crime data 
        crime_data = preprocess_crime_data('Nairobi_Crime_Hotspots.csv')  
        graph = assign_crime_severity(graph, crime_data)

        print("Calculating optimal route...")
        optimal_route = find_optimal_route(graph, start_lat, start_lon, end_lat, end_lon)
        print("Optimal Route:", optimal_route)

        if optimal_route:
            # Get route coordinates
            route_coords = [(graph.nodes[node]['y'], graph.nodes[node]['x']) for node in optimal_route]

            # Create and save the map
            map_filename = visualize_route(route_coords)

            # Render the map in the template
            return render_template('map.html', map_html=map_filename)
        else:
            return 'No route found. Please try again.'
    except ValueError as e:
        print(f"Error: {e}")
        return str(e)  # Return the error message

if __name__ == "__main__":
    app.run(debug=True)
