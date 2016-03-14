import os
from flask import Flask
from flask import render_template
app = Flask(__name__)
locations = []

@app.route('/')
def home():
    origin = '37.866197,+-122.252968'
    destination = '37.876031,+-122.258791'
    waypoints = 'International+House+Berkeley|Greek+Theater+Berkeley|GSPP+Berkeley'
    return render_template('home.html', \
        origin =origin, \
        destination=destination, \
        waypoints = waypoints)

@app.route('/loc/<lat>/<lng>')
def echo_loc(lat, lng):
    locations.append((lat, lng))
    return str(locations)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)