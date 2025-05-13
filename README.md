## SafeWay - A Safety-Aware Rerouting Software
SafeWay is a web-based application designed to assist e-hailing drivers by optimizing routes not only based on time and distance but also safety. The system incorporates a crime severity model that factors in crime hotspots, providing a safer route when navigating through Nairobi.

### Features
- Safety-Aware Routing that incorporates crime data to determine safer routes for drivers.
- Haversine Distance Calculation calculating distances between two geographical points (latitude/longitude) to evaluate proximity to crime hotspots.
- Dynamic Input allowing users to input their start and end locations, and outputs the safest route based on historical crime data.
- Visualization that generates and displays the route on an interactive map.

### Project Structure
├── app.py                # Main application file
├── crime_data.py          # Script to calculate crime severity and proximity
├── data_processing.py     # Preprocessing of crime data and normalization
├── visualize.py           # Functions to visualize the route on a map
├── templates/
  └── map.html           # HTML template for displaying the map
├── requirements.txt       # Required Python libraries
├── README.md         

### Technologies Used
+ Python: Backend language.
+ Flask: Web framework to handle routing and HTTP requests.
+ Pandas: For data manipulation and preprocessing.
+ Folium: For map generation and visualization.
+ Geopy: Geocoding addresses to coordinates.
+ Haversine Formula: Used to calculate distances between two geographical points.
+ Scikit-learn: For normalizing the crime severity data.

### Requirements
You can install all the required libraries by running:
``` pip install -r requirements.txt

requirements.txt:
Flask==2.0.1
pandas==1.3.3
scikit-learn==0.24.2
geopy==2.2.0
folium==0.12.1
```
### Setup Instructions
1. Clone the repository
2. Navigate into the project directory
3. Create and activate a virtual environment
4. Install the required dependencies
5. Run the Flask application

### How It Works
1. Data Processing- The crime dataset (Nairobi_Crime_Hotspots.csv) is preprocessed using data_processing.py. It normalizes the crime severity to be used in routing calculations.

2. Crime Severity Calculation- Using crime_data.py, crime severity is calculated for road segments using the Haversine formula to check the proximity of each segment to crime hotspots.

3. Route Visualization- The app uses visualize.py to map the safest route. This is displayed on an interactive map in the map.html template.

### Usage
* Input, the user provides the start and end locations.

* Output, the app displays the safest route between the two points, factoring in crime data.

### Future Improvements
Integration with live traffic data.
Enhancing the UI for better user experience.
Incorporating user feedback to improve the safety model.

### Contributors
Joy Kendi

Joy Nyayieka

Simon Kiragu
