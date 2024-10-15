import networkx as nx
import osmnx as ox
from crime_data import assign_crime_severity
from traffic import assign_traffic_data

# Weight function combining distance, crime severity, and traffic
def weight_function(u, v, d):
    distance = d.get('length', 1)  # Road segment length
    severity = d.get('crime_severity', 0)  # Crime severity
    #traffic = d.get('traffic_factor', 1)  # Travel time from Google Maps
    #return distance + (severity * 0.5) + (traffic * 0.3)

# Main function to find optimal route
def find_optimal_route(graph, start_lat, start_lon, end_lat, end_lon):
    origin = ox.nearest_nodes(graph, start_lon, start_lat)
    destination = ox.nearest_nodes(graph, end_lon, end_lat)
    
    try:
        # Attempt to find the optimal route using the shortest path
        optimal_route = nx.shortest_path(graph, origin, destination, weight='weight_function')
        return optimal_route
    
    except nx.NetworkXNoPath:
        # If no path is found, handle the exception and try alternative logic
        print(f"No path found between nodes {origin} and {destination}. Trying alternative...")

        # Check if graph is connected
        if not nx.is_connected(graph):
            print("Graph is not fully connected.")
            
            # Find connected components and try to route within the largest component
            largest_component = max(nx.connected_components(graph), key=len)
            subgraph = graph.subgraph(largest_component).copy()
            
            # Check if origin and destination are in the same component
            if origin in largest_component and destination in largest_component:
                try:
                    # Try to find the path in the subgraph (largest connected component)
                    optimal_route = nx.shortest_path(subgraph, origin, destination, weight='weight_function')
                    return optimal_route
                except nx.NetworkXNoPath:
                    print(f"Still no path between nodes {origin} and {destination} even in the largest component.")
            else:
                print(f"Origin or destination not in the same connected component.")
        
        # If no alternative path is found, return an error message or handle accordingly
        return None
