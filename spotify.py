

import base64
from json import JSONDecodeError
from urllib.error import HTTPError
import requests



client_id = "3a35c0bb12b54e1f8f0602a408bc6bf3"
client_secret = "17391461037d4d1788e03c089bd4319d"


auth_url = 'https://accounts.spotify.com/api/token'
auth_data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret
}

response = requests.post(auth_url, data=auth_data)

if response.status_code == 200:
    response_data = response.json()
    print('Response:', response_data)
    access_token = response_data['access_token']
    print('Access Token:', access_token)
else:
    print('Error:', response.status_code)

##########
# This part of code takes in the track id and returns track name and artist.
##########
track_id = '5jQI2r1RdgtuT8S3iG8zFC?si=e0fd7104641b47cb'
api_url = f'https://api.spotify.com/v1/tracks/{track_id}'

print(access_token, " Access_token")
# Setting the Authorization header with the access token
headers = {
    'Authorization': 'Bearer ' + access_token
}

# This is our API call
try:
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()  # Raise an exception for non-2xx status codes

    try:
        data = response.json()
        print('Track Name:', data['name'])
        print('Artist:', data['artists'][0]['name'])
        # Additional processing of the API response data
    except JSONDecodeError as e:
        print('Error decoding JSON response:', e)
        # Handle the JSONDecodeError
except HTTPError as e:
    print('HTTP Error:', e)
    # Handle the HTTPError
except Exception as e:
    print('Error:', e)
    # Handle other exceptions


##########
# This takes in playlist id and returns the songs + artist.
##########

playlist_id = '37i9dQZF1DX3R7OWWGN4gH?si=ee0ea03d4c3f4948'
api_url = f'https://api.spotify.com/v1/playlists/{playlist_id}'

headers = {
    'Authorization': 'Bearer ' + access_token
}

# Make the API call
response = requests.get(api_url, headers=headers)

# Check the response status code
if response.status_code == 200:
    playlist_data = response.json()
    
    # Extract relevant information from the playlist data
    playlist_name = playlist_data['name']
    track_count = playlist_data['tracks']['total']
    owner_name = playlist_data['owner']['display_name']
    
    print(f'Playlist Name: {playlist_name}')
    print(f'Track Count: {track_count}')
    print(f'Owner Name: {owner_name}')
    
    # Access individual tracks within the playlist
    for track in playlist_data['tracks']['items']:
        track_name = track['track']['name']
        artist_name = track['track']['artists'][0]['name']
        print(f'Track: {track_name} - Artist: {artist_name}')
    
else:
    print('Error:', response.status_code)




