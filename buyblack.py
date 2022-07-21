from flask import Flask, render_template, abort, request, flash
from forms import GetChoice
import requests
app = Flask(__name__)
app.secret_key = 'development key'
API_KEY = "AIzaSyBIJAAFKaletYozLcOg413VGAdHqNbJzWY"
LAT = 0
LNG = 0
@app.route("/")
def index():
    return render_template('home.html') 

#search page
@app.route("/", methods=['POST','GET'])
def get_coords():
    global LAT
    global LNG
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
        form = GetChoice()
    else:
        return "address is invalid"
    return render_template('search.html', form = form, latitude = LAT, longitude = LNG, url = "https://maps.googleapis.com/maps/api/js?key=" + API_KEY + "&callback=initMap") 

@app.route("/results", methods=['POST', 'GET'])
def results():
    form = GetChoice()
    choice = form.option.data
    params = {
        'key': 'AIzaSyBIJAAFKaletYozLcOg413VGAdHqNbJzWY',
        'query': "black owned" + choice,
        'location': str(LAT) + ', ' + str(LNG)
    }
    base_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
    response = requests.get(base_url, params=params)
    data = response.json()
    businesses = data['results']
    return render_template('results.html', form = form, choice = choice, businesses = businesses, latitude = LAT, longitude = LNG, url = "https://maps.googleapis.com/maps/api/js?key=" + API_KEY + "&callback=initMap") 
        
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")