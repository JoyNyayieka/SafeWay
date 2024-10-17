import networkx as nx
import osmnx as ox

# Weight function combining distance, crime severity, and traffic
def weight_function(u, v, d):
    distance = d.get('length', 1)  # Road segment length (default to 1 if missing)
    severity = d.get('crime_severity', 0)  # Crime severity (default to 0 if missing)
    traffic = d.get('traffic_factor', 1)  # Traffic factor (default to 1 if missing)

    # Compute total weight
    weight = distance + (severity * 0.5) + (traffic * 0.3)
    return weight

# Main function to find optimal route
def find_optimal_route(graph, start_lat, start_lon, end_lat, end_lon):
    # Find the nearest graph nodes for start and end locations
    origin = ox.nearest_nodes(graph, start_lon, start_lat)
    destination = ox.nearest_nodes(graph, end_lon, end_lat)
    
    try:
        # Attempt to find the optimal route using the shortest path with the custom weight function
        optimal_route = nx.shortest_path(graph, origin, destination, weight=weight_function)
        return optimal_route
    
    except nx.NetworkXNoPath:
        # If no path is found, handle the exception and try alternative logic
        print(f"No path found between nodes {origin} and {destination}. Trying alternative...")

        # Check if the graph is connected
        if not nx.is_connected(graph):
            print("Graph is not fully connected.")
            
            # Find the largest connected component and route within it
            largest_component = max(nx.connected_components(graph), key=len)
            subgraph = graph.subgraph(largest_component).copy()
            
            # Check if origin and destination are in the same component
            if origin in largest_component and destination in largest_component:
                try:
                    # Try to find the path in the largest connected component
                    optimal_route = nx.shortest_path(subgraph, origin, destination, weight=weight_function)
                    return optimal_route
                except nx.NetworkXNoPath:
                    print(f"Still no path between nodes {origin} and {destination} even in the largest component.")
            else:
                print(f"Origin or destination not in the same connected component.")
        
        # If no path is found, return None
        return None
