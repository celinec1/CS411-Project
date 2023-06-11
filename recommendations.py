import weather
import directions

start = ''
destination = ''

def main(start, destination):
    zip = (directions.validate_address(start, directions.api_key))[1]
    if zip:
        temp, condition = weather.get_weather(zip, weather.api_key)
    
    if condition != ('Sunny' or 'Clear' or 'Partly cloudy' or 'Cloudy' or 'Overcast'):
        i = 1
    return None

def shortest_time(durations):
    temp = min(durations.values())
    res = [key for key in durations if durations[key] == temp]

    
