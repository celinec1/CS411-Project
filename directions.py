import requests

def get_directions_duration(start, destination, api_key):
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={start}&destination={destination}&key={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        if data["status"] == "OK":
            durations = {}
            for route in data["routes"]:
                for leg in route["legs"]:
                    mode = leg["steps"][0]["travel_mode"]
                    duration = leg["duration"]["text"]
                    durations[mode] = duration
            
            return durations
        else:
            print(f"Error: {data['status']}")
    else:
        print("Error: Failed to retrieve directions.")
    
    return None

#api key
api_key = ''

#put in start and destination (city, state) format as of rn
start = 'Boston, MA'
destination = 'New York, NY'

# not sure if this part is busted or the function
directions_durations = get_directions_duration(start, destination, api_key)
if directions_durations:
    for mode, duration in directions_durations.items():
        print(f"{mode.capitalize()}: {duration}")