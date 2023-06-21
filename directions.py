import requests

#api key
api_key = 'AIzaSyD8hzf6RtCQ8ab6AYdt7M6J-Nr2tgvuz0M'
start = '808 Commonwealth Ave Boston, MA'
destination = '528 Beacon St Boston, MA'

#returns dictionary where key is mode and value is a tuple (time in text, time in seconds)
def get_directions_duration(start, destination, mode, api_key):
    #global location
    #location = start
    if (validate_address(start, api_key) != (None,None)) and (validate_address(destination, api_key) != (None, None)):
        url = f"https://maps.googleapis.com/maps/api/directions/json?origin={start}&destination={destination}&mode={mode}&key={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            
            if data["status"] == "OK":
                durations = {}
                for route in data["routes"]:
                    for leg in route["legs"]:
                        #mode = leg["steps"][0]["travel_mode"]
                        duration = (leg["duration"]["text"], leg['duration']['value']) #tuple of text and seconds
                        durations[mode] = duration
                        #print(duration)
                
                return durations
            else:
                print(f"Error: {data['status']}")
        else:
            print("Error: Failed to retrieve directions.")
    else:
        print("Error: Invalid Address")
    
    return None

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

    return None, None

#returns dictionary of all modes where the value is tuple (time in text, time in)
def route_durations(start, destination, api_key):
    all_durations = {}
    modes = ['driving', 'bicycling', 'transit', 'walking']
    for mode in modes:
        directions_durations = get_directions_duration(start, destination, mode, api_key)
        if directions_durations:
            #print(directions_durations)
            for modes, duration in directions_durations.items(): #this displays "transit" as "walking" not sure why
                if mode != None:
                    all_durations[mode] = duration
    return(all_durations)

def print_durations(durations):
    for modes, duration in durations.items(): #this displays "transit" as "walking" not sure why
        if modes != None:
                print(f"{modes.capitalize()}: {duration[0]}") #prints mode from the list and not the dictionary



#durations = route_durations(start, destination, api_key)
#print_durations(durations)
#print(get_directions_duration(start, destination, 'transit', api_key))




