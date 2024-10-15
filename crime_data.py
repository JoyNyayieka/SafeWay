import math

# Haversine function to calculate the distance between two lat/lon points
def haversine(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    R = 6371  # Radius of the earth in kilometers

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    distance = R * c  # Distance in kilometers
    return distance

# Function to calculate crime severity for a road segment based on proximity to crime hotspots
def calculate_severity(midpoint, crime_data, max_distance_km=1):
    total_severity = 0
    for crime in crime_data:
        crime_coord = (crime['Latitude'], crime['Longitude'])
        distance = haversine(midpoint, crime_coord)
        
        # Check if the crime hotspot is within the specified max distance
        if distance <= max_distance_km:
            severity = crime['Severity']  # Use the crime severity from the dataset
            proximity_factor = (max_distance_km - distance) / max_distance_km  # Closer crimes have higher impact
            total_severity += severity * proximity_factor  # Adjust severity based on proximity

    return total_severity

# Function to assign crime severity to road segments
def assign_crime_severity(graph, crime_data):
    for u, v, key, data in graph.edges(keys=True, data=True):
        # Calculate the midpoint of the road segment
        midpoint = ((graph.nodes[u]['y'] + graph.nodes[v]['y']) / 2, 
                     (graph.nodes[u]['x'] + graph.nodes[v]['x']) / 2)
        
        # Calculate the crime severity for the road segment based on proximity to hotspots
        severity = calculate_severity(midpoint, crime_data)
        
        # Assign the calculated crime severity to the road segment
        data['crime_severity'] = severity
    
    return graph
