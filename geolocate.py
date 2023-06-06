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

def get_address(latitude, longitude, api_key):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        if data["results"]:
            address = data["results"][0]["formatted_address"]
            return address
        else:
            print("Error: No results found for the provided coordinates.")
    else:
        print("Error: Failed to retrieve address.")
    
    return None


api_key = ''

# get + print location
location = get_current_location(api_key)
if location:
    latitude, longitude = location
    print("Latitude:", latitude)
    print("Longitude:", longitude)

if location:
    address = get_address(latitude, longitude, api_key)
    if address:
        print("Address:", address)
