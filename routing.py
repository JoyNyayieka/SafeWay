import networkx as nx
import osmnx as ox
from crime_data import assign_crime_severity
from traffic import assign_traffic_data

# Weight function combining distance, crime severity, and traffic
def weight_function(u, v, d):
    distance = d.get('length', 1)  # Road segment length
    severity = d.get('crime_severity', 0)  # Crime severity
    #traffic = d.get('traffic_factor', 1)  # Travel time from Google Maps
    return distance + (severity * 0.5) + (traffic * 0.3)

# Main function to find optimal route
def find_optimal_route(graph, start_lat, start_lon, end_lat, end_lon):
    origin = ox.get_nearest_node(graph, (start_lat, start_lon))
    destination = ox.get_nearest_node(graph, (end_lat, end_lon))

    # Find the shortest path based on custom weight function
    optimal_route = nx.shortest_path(graph, origin, destination, weight=weight_function)

    return optimal_route
