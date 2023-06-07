import requests
import geolocate

api_key = ""
w_api_key = ""

def get_weather(latitude, longitude, api_key):
    url = f"https://api.weatherapi.com/v1/current.json?q={latitude},{longitude}&key={api_key}"
    response = requests.get(url)
    data = response.json()

    if 'error' in data:
        print(f"Error: {data['error']['message']}")
    else:
        current_weather = data['current']
        location = f"{latitude}, {longitude}"
        print(f"Weather at {location}:")
        print(f"Temperature: {current_weather['temp_f']}°F")
        print(f"Condition: {current_weather['condition']['text']}")

# retrieve latitude and longitude from geolocate module
location = geolocate.get_current_location(w_api_key)
if location:
    latitude, longitude = location
    get_weather(latitude, longitude, api_key)
