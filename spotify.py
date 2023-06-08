

import base64
from json import JSONDecodeError
import random
from urllib.error import HTTPError
import requests



client_id = 
client_secret = 


auth_url = 'https://accounts.spotify.com/api/token'
auth_data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': 'user-library-read'
}

response = requests.post(auth_url, data=auth_data)

if response.status_code == 200:
    response_data = response.json()
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

##########
#
##########

num_songs = 10  # Number of songs to include in the playlist

# This is Lin's user id
user_id = '31kehdawawjcaac7i2sfhkevuhsq'
# Retrieve user's liked songs
api_url = 'https://api.spotify.com/v1/me/tracks'
headers = {
    'Authorization': 'Bearer ' + access_token
}
params = {
    'limit': 50  # We can adjust this later.
}
response = requests.get(api_url, headers=headers, params=params)
liked_songs_data = response.json().get('items', [])

# Randomly select songs
if num_songs > len(liked_songs_data):
    num_songs = len(liked_songs_data)

selected_songs = random.sample(liked_songs_data, num_songs)

# Create a new playlist
playlist_name = 'My Liked Songs Playlist'
playlist_description = 'A playlist with my liked songs'
playlist_public = True

create_playlist_url = f'https://api.spotify.com/v1/users/{user_id}/playlists'
create_playlist_data = {
    'name': playlist_name,
    'description': playlist_description,
    'public': playlist_public
}

create_playlist_response = requests.post(create_playlist_url, headers=headers, json=create_playlist_data)

# Check the response status code
if create_playlist_response.status_code == 201:
    create_playlist_data = create_playlist_response.json()
    playlist_id = create_playlist_data.get('id')

    if playlist_id:
        # Remove all existing tracks from the playlist
        remove_tracks_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
        remove_tracks_response = requests.delete(remove_tracks_url, headers=headers)

        if remove_tracks_response.status_code == 200:
            # Get the URIs of selected songs
            track_uris = [song['track']['uri'] for song in selected_songs]

            # Add selected songs to the playlist
            add_tracks_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
            add_tracks_data = {
                'uris': track_uris
            }

            add_tracks_response = requests.post(add_tracks_url, headers=headers, json=add_tracks_data)

            # Check the response status code
            if add_tracks_response.status_code == 201:
                print('Playlist created successfully and tracks added!')
            else:
                print('Error adding tracks to the playlist:', add_tracks_response.status_code)
        else:
            print('Error removing existing tracks from the playlist:', remove_tracks_response.status_code)
    else:
        print('Error creating playlist. Response:', create_playlist_data)
else:
    print('Error creating playlist:', create_playlist_response.status_code)
