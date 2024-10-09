from flask import Flask, render_template, request

# Create an instance of the Flask class
app = Flask(__name__)

# Define the home route for the web application
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_routes',  
 methods=['POST'])
def routes():  
    start_location = request.form['start_location']
    end_location = request.form['end_location']

    # Process data, calculate safety score (replace with your logic)
   

    return render_template('routes.html', start_location=start_location, end_location=end_location)  # Pass data to template


    # Handle the form submission here (e.g., process data, perform calculations)
    # ... your code ...

if __name__ == "__main__":
    app.run(debug=True) 