import googlemaps

# Function to get traffic data from Google Maps API
def get_traffic_data(origin, destination, api_key):
    gmaps = googlemaps.Client(key=api_key)
    
    # Fetch real-time traffic data
    result = gmaps.distance_matrix(
        origins=[origin],
        destinations=[destination],
        mode="driving",
        departure_time="now",  # Real-time data
        traffic_model="pessimistic"
    )
    
    # Extract travel time considering traffic, or fallback to normal time
    try:
        travel_time_in_traffic = result['rows'][0]['elements'][0]['duration_in_traffic']['value']  # Seconds
    except KeyError:
        travel_time_in_traffic = result['rows'][0]['elements'][0]['duration']['value']  # Fallback

    return travel_time_in_traffic

# Assign traffic data to road network graph
def assign_traffic_data(graph, api_key):
    for u, v, key, data in graph.edges(keys=True, data=True):
        origin = (graph.nodes[u]['y'], graph.nodes[u]['x'])
        destination = (graph.nodes[v]['y'], graph.nodes[v]['x'])
        travel_time = get_traffic_data(origin, destination, api_key)
        data['traffic_factor'] = travel_time
    return graph
