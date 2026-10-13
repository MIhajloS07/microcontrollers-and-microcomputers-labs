from flask import Flask, render_template_string
# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL
HTML = """
<h1>DHT11 – Sensor Comparison</h1>
<img src="/static/graph.png">
"""

@app.route("/")
def index():
    return render_template_string(HTML)

# Run the Flask application on all available network interfaces 
app.run(host="0.0.0.0", port=5000)
