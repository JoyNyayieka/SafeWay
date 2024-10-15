from flask import Flask, request, jsonify, render_template
import osmnx as ox
from routing import find_optimal_route
from crime_data import assign_crime_severity
from visualize import visualize_route
from data_processing import preprocess_crime_data
#from traffic import assign_traffic_data

# Create an instance of the Flask class
app = Flask(__name__)

# Define the home route for the web application
@app.route('/')
def home():

    # Load your road network
    graph = ox.graph_from_place('Nairobi, Kenya', network_type='drive')

    # Load preprocessed crime data 
    crime_data = preprocess_crime_data('Nairobi_Crime_Hotspots.csv')  
    graph = assign_crime_severity(graph, crime_data)

    # Assign crime severity and traffic data
    #graph = assign_crime_severity(graph, crime_data)
    #graph = assign_traffic_data(graph, api_key='replace this with API key')

    # Provide coordinates for start and end points (example coordinates)
    start_lat = -1.2921  # Example start latitude (Nairobi)
    start_lon = 36.8219  # Example start longitude (Nairobi)
    end_lat = -1.3000    # Example end latitude (Nairobi)
    end_lon = 36.8200    # Example end longitude (Nairobi)

    print("Calculating optimal route...")
    optimal_route = find_optimal_route(graph, start_lat, start_lon, end_lat, end_lon)
    print("Optimal Route:", optimal_route)

    if optimal_route:
        # Get route coordinates (implement this function in routing.py)
        route_coords = [(graph.nodes[node]['y'], graph.nodes[node]['x']) for node in optimal_route]

        # Create and save the map
        map_filename = visualize_route(route_coords)

        # Render the map in the template
        return render_template('map.html', map_html=map_filename)
    else:
        return 'No route found. Please try again.'

if __name__ == "__main__":
    app.run(debug=True)



