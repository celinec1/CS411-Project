import requests
import directions

#pulls data from weatherapi, and using the geolocate call it is able to pull the data from the location the person is at
api_key = "c4a56e33ea2e4d26801202756230506"

def get_weather(zip, api_key):
    url = f"https://api.weatherapi.com/v1/current.json?q={zip}&key={api_key}"
    response = requests.get(url)
    data = response.json()

    if 'error' in data:
        print(f"Error: {data['error']['message']}")
    else:
        current_weather = data['current']
        location = f"{zip}"
        print(f"Weather at {location}:")
        print(f"Temperature: {current_weather['temp_f']}°F")
        print(f"Condition: {current_weather['condition']['text']}")

# retrieve latitude and longitude from geolocate module

zip = (directions.validate_address(directions.start, directions.api_key))[1]
if zip:
    get_weather(zip, api_key)
