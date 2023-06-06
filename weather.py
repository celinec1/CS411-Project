import requests

location = input("Enter a location: ")

api_key = 
url = f"https://api.weatherapi.com/v1/current.json?q={location}&key={api_key}"

response = requests.get(url)
data = response.json()

if 'error' in data:
    print(f"Error: {data['error']['message']}")
else:
    current_weather = data['current']
    print(f"Weather in {location}:")
    print(f"Temperature: {current_weather['temp_c']}°C")
    print(f"Condition: {current_weather['condition']['text']}")

