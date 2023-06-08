import requests

#api key
api_key = 'AIzaSyD8hzf6RtCQ8ab6AYdt7M6J-Nr2tgvuz0M'
start = '808 Commonwealth Ave Boston, MA'
destination = '528 Beacon St Boston, MA'

def get_directions_duration(start, destination, mode, api_key):
    if (validate_address(start, api_key) != (None,None)) and (validate_address(destination, api_key) != (None, None)):
        url = f"https://maps.googleapis.com/maps/api/directions/json?origin={start}&destination={destination}&mode={mode}&key={api_key}"
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
    else:
        print("Error: Invalid Address")
    
    #return None

def validate_address(address, api_key): #returns tuple of formatted address and zip code
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["status"] == "OK":
            #get formatted address
            formatted_address = data["results"][0]["formatted_address"]
            #take zipcode for address
            postal_code = None
            for component in data["results"][0]["address_components"]:
                if "postal_code" in component["types"]:
                    postal_code = component["long_name"]
                    break
            return formatted_address, postal_code
        else:
            print("Error: Address validation failed.")
    else:
        print("Error: Failed to validate address.")

    #return None, None

def route_durations(start, destination, api_key):
    modes = ['driving', 'bicycling', 'transit', 'walking']
    for mode in modes:
        directions_durations = get_directions_duration(start, destination, mode, api_key)
        if directions_durations:
            for modes, duration in directions_durations.items(): #this displays "transit" as "walking" not sure why
                if mode != None:
                    print(f"{mode.capitalize()}: {duration}") #prints mode from the list and not the dictionary


print(route_durations(start, destination, api_key))
