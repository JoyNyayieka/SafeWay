import folium

# Function to visualize route on a map
def visualize_route(graph, route):
    start = graph.nodes[route[0]]
    route_map = folium.Map(location=[start['y'], start['x']], zoom_start=12)

    for u, v in zip(route[:-1], route[1:]):
        start_point = (graph.nodes[u]['y'], graph.nodes[u]['x'])
        end_point = (graph.nodes[v]['y'], graph.nodes[v]['x'])
        folium.PolyLine([start_point, end_point], color="blue", weight=2.5).add_to(route_map)

    route_map.save('optimal_route_map.html')
