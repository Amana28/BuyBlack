#import googlemaps
from flask import Flask, render_template, abort, request  
import requests
app = Flask(__name__)
API_KEY = "AIzaSyBIJAAFKaletYozLcOg413VGAdHqNbJzWY"

@app.route("/")
def index():
    return render_template('addy.html') 

@app.route("/", methods=['POST'])
def get_coords():
    addy = request.form["address"]
    params = {
        'key': API_KEY,
        'address': addy.replace(' ', '+')
    }
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    response = requests.get(base_url, params=params)
    data = response.json()
    if data['status'] == 'OK':
        result = data['results'][0]
        location = result['geometry']['location']
        lat = location['lat']
        lng = location['lng']
        print(lat, lng)
    else:
        return "address is invalid"
    return render_template('index.html', latitude = lat, longitude = lng, url = "https://maps.googleapis.com/maps/api/js?key=" + API_KEY + "&callback=initMap") 


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")