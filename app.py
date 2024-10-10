from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define the home route for the web application
@app.route('/')
def home():
    return "SafeWay App Running!"

if __name__ == "__main__":
    app.run(debug=True) 



    