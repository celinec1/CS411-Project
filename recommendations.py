import weather
import directions

#start = '808 Commonwealth Ave Boston MA'
#destination = '528 Beacon St Boston MA'
#durations = directions.route_durations(start, destination, directions.api_key)
#zip = (directions.validate_address(start, directions.api_key))[1]


def main(start, destination): #returns recommended mode of transportation
    zip = (directions.validate_address(start, directions.api_key))[1]
    durations = directions.route_durations(start, destination, directions.api_key)
    if zip:
        temp, condition = weather.get_weather(zip, weather.api_key)

        if condition != ('Sunny' or 'Clear' or 'Partly cloudy' or 'Cloudy' or 'Overcast'):
            if temp > 80:
                return 'driving'
            else:
                if durations['walking'][1] >  1200:
                    fastest = min(durations['bicycling'][1], durations['transit'][1])
                    if durations['bicycling'][1] == fastest:
                        return 'bicycling'
                    else:
                        return 'transit'
                else:
                    return 'walking'
        else:
            return shortest_time(durations)
    return None

def shortest_time(durations): #returns shortest mode of transportation
    temp = min([value[1] for value in durations.values()])
    res = [key for key in durations if durations[key][1] == temp]
    return res[0]


#print(durations)

#print(main(start, destination))

    
