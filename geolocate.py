import requests

def get_current_location(api_key):
    url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}"
    response = requests.post(url)
    

    if response.status_code == 200: #if api call worked
        data = response.json()
        latitude = data["location"]["lat"]
        longitude = data["location"]["lng"]
        return latitude, longitude
    else:
        print("Error: Failed to retrieve current location.")
        return None

api_key = "AIzaSyD8hzf6RtCQ8ab6AYdt7M6J-Nr2tgvuz0M"

# get + print location
location = get_current_location(api_key)
if location:
    latitude, longitude = location
    print("Latitude:", latitude)
    print("Longitude:", longitude)
