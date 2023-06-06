import requests
import googlemaps


key = 'AIzaSyD8hzf6RtCQ8ab6AYdt7M6J-Nr2tgvuz0M'

gmaps = googlemaps.Client(key)

geo_url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyD8hzf6RtCQ8ab6AYdt7M6J-Nr2tgvuz0M'

# geolocation parameters
geo_params = {
    "key": key
}

# request geolocation API
geo_response = requests.get(geo_url, params=geo_params)

print(geo_response.status_code)

# json data from response
data = geo_response.json()

# access location coordinates
latitude = data["location"]["lat"]
longitude = data["location"]["lng"]


# convert lat, lng into address
rev_geocode_origin = gmaps.reverse_geocode((latitude, longitude))

# origin coordinates pulled from geo api
origin = rev_geocode_origin[0]['formatted_address']

# example destination from user input
destination = "Boston"


# put origin and destination through geolocation
url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&mode=transit&key={key}"

# directions parameters
direct_params = {
    "key": key,
    "origin": origin,
    "destination": destination,
    "mode": "transit"
}

# request directions API
response = requests.get(url, params=direct_params)

print(response.status_code)

json_data = response.json()

print(json_data)




