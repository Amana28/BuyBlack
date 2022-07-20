#import googlemaps
from flask import Flask, render_template, abort, request  
import requests
app = Flask(__name__)
API_KEY = "AIzaSyBIJAAFKaletYozLcOg413VGAdHqNbJzWY"
LAT = ""
LNG = ""

@app.route("/")
def index():
    return render_template('addy.html') 

#search page
@app.route("/", methods=['POST'])
def get_coords():
    a1 = request.form["a1"]
    a2 = request.form["a2"]
    a3 = request.form["a3"]
    full_address = a1 + ", " + a2 + ", " + a3
    params = {
        'key': API_KEY,
        'address': full_address
    }
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    response = requests.get(base_url, params=params)
    data = response.json()
    if data['status'] == 'OK':
        result = data['results'][0]
        location = result['geometry']['location']
        LAT = location['lat']
        LNG = location['lng']
        #print(lat, lng)
    else:
        return "address is invalid"
    return render_template('index.html', latitude = LAT, longitude = LNG, url = "https://maps.googleapis.com/maps/api/js?key=" + API_KEY + "&callback=initMap") 

@app.route("/results")
def results():
    params = {
        'key': 'AIzaSyBIJAAFKaletYozLcOg413VGAdHqNbJzWY',
        'query': "black owned restaurant",
        'location': '39.1030000, -84.5120160'
    }
    base_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
    response = requests.get(base_url, params=params)
    data = response.json()

    businesses = data['results']


    return render_template('results.html', businesses = businesses, latitude = 0, longitude = 0, url = "https://maps.googleapis.com/maps/api/js?key=" + API_KEY + "&callback=initMap") 
        
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")