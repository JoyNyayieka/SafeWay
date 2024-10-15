import folium
import os

def visualize_route(route_coords):
    m = folium.Map(location=route_coords[0], zoom_start=13)
    
    # Plot the route on the map
    folium.PolyLine(route_coords, color="blue", weight=2.5, opacity=1).add_to(m)
    
    # Save the map as an HTML file
    map_filename = os.path.join('templates', 'map.html')
    m.save(map_filename)
    
    return map_filename

