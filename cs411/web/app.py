import os
import random
from flask import Flask, request, redirect, jsonify
from flask_cors import CORS
import requests
from urllib.parse import quote

import sys
# Get the grandparent directory of the current file (app.py)
grandparent_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Add grandparent directory to sys.path
sys.path.append(grandparent_directory)

import directions, weather, recommendations
from pymongo import MongoClient

connection_string = 'mongodb+srv://lkk19:IONc14XUBjIgI9Oi@cluster0.6oclfrh.mongodb.net/Testing'
# # Create a MongoClient to interact with MongoDB Atlas
client = MongoClient(connection_string)

# # Select your database
db = client['Testing']

# # Select the collection within the database
collection = db['lindsay_test']

app = Flask(__name__)
CORS(app)
user = ''
access = ''

#working on taking in inputs 
@app.route('/api/submit', methods=['POST'])
def submit():
    data = request.get_json()
    location = data.get('location')
    destination = data.get('destination')

    print('Location:', location)
    print('Destination:', destination)

    global durations
    durations = directions.route_durations(location, destination, directions.api_key)
    #durations = list[durations]
    
    global loco_data
    loco_data = [location, destination]
    #user_data.update(loco_data) #idk why but commenting out this line breaks everything LOL
    #collection.insert_one(data)

    recommended = recommendations.main(location, destination)
    temp, condition = weather.get_weather(((directions.validate_address(location, directions.api_key))[1]), weather.api_key)


    response = {'driving' : durations['driving'][0], 'bicycling': durations['bicycling'][0], 'transit': durations['transit'][0], 'walking': durations['walking'][0], 'recommended' : recommended, 'temp': temp, 'condition': condition}
    print(response)
    return jsonify(response)


@app.route('/api/transportation', methods=['POST'])
def handle_transportation_selection():
    transportation = request.json.get('transportation')

    print (transportation)

    response = {'message': 'Transportation selection received', 'transportation': transportation}
    
    global playlist_length
    playlist_length = durations[transportation][1]
    print(durations[transportation])
    print(playlist_length)
    link = create_top_tracks_playlist(user_id, access_token, playlist_length)
    trip_data = [transportation, link]
    trip_data += loco_data

    print(trip_data)

    existing_user = collection.find_one({'User ID': user_id})
    if existing_user:
        #collection.update_one({'User ID': user_id}, {'$set': {'trip': []}})
        collection.update_one({'User ID': user_id}, {'$push': {'trip': trip_data}})
        print('collection updated')
    else:
        user_data['trip'] = [trip_data]
        collection.insert_one(user_data)
        print('new object created')
    
    past_trips(10)
    return jsonify({'link': link})



# Step 1: Authorization - Redirect user to Spotify's authorization page
@app.route('/')
def index():
    # Construct the authorization URL
    auth_url = 'https://accounts.spotify.com/authorize'
    auth_params = {
        'client_id': '3a35c0bb12b54e1f8f0602a408bc6bf3',
        'response_type': 'code',
        'redirect_uri': quote('http://localhost:8000/callback', safe=''),
        'scope': 'user-read-private user-read-email user-top-read playlist-modify-private',
        # Add necessary scopes
    }

    # Redirect the user to the authorization URL
    auth_redirect_url = auth_url + '?' + '&'.join([f'{k}={v}' for k, v in auth_params.items()])
    return redirect(auth_redirect_url)


def create_top_tracks_playlist(user_id, access_token, length):
    # Create a new playlist
    playlist_url = f'https://api.spotify.com/v1/users/{user_id}/playlists'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
    }
    playlist_data = {
        'name': 'Have a safe trip!',
        'public': False,
    }
    response = requests.post(playlist_url, headers=headers, json=playlist_data)

    if response.status_code == 201:
        playlist_data = response.json()
        playlist_id = playlist_data['id']
        print('Playlist ID:', playlist_id)

        # Get the user's top tracks
        top_tracks_url = 'https://api.spotify.com/v1/me/top/tracks'
        params = {
            'limit': 200,
        }
        response = requests.get(top_tracks_url, headers=headers, params=params)

        if response.status_code == 200:
            tracks_data = response.json()
            track_ids = [track['id'] for track in tracks_data['items']]
            random.shuffle(track_ids)

            # Add the top tracks to the playlist
            add_tracks_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
            tracks_data = []
            total_duration = 0

            for track_id in track_ids:
                track_info_url = f'https://api.spotify.com/v1/tracks/{track_id}'
                response = requests.get(track_info_url, headers=headers)

                if response.status_code == 200:
                    track_info = response.json()
                    duration_ms = track_info['duration_ms']
                    if total_duration + duration_ms <= length * 1000:
                        tracks_data.append({'uri': f'spotify:track:{track_id}', 'duration_ms': duration_ms})
                        total_duration += duration_ms
                    else:
                        break

            response = requests.post(add_tracks_url, headers=headers, json={'uris': [track['uri'] for track in tracks_data]})

            if response.status_code == 201:
                print('Playlist created successfully with top tracks!')
                link = f'https://open.spotify.com/playlist/{playlist_id}'
                print(link)

                data = {'Playlist': link}
                #collection.insert_one(data)

                return link
            else:
                print('Error adding tracks to playlist:', response.text)
        else:
            print('Error retrieving top tracks:', response.text)
    else:
        print('Error creating playlist:', response.text)


# Step 2: Obtain authorization code - Handle redirect URI and retrieve the code
@app.route('/callback')
def callback():
    authorization_code = request.args.get('code')

    # Step 3: Exchange authorization code for access token
    token_url = 'https://accounts.spotify.com/api/token'
    token_data = {
        'client_id': '3a35c0bb12b54e1f8f0602a408bc6bf3',
        'client_secret': '17391461037d4d1788e03c089bd4319d',
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'redirect_uri': 'http://localhost:8000/callback',
    }

    response = requests.post(token_url, data=token_data)

    # Step 4: Use the access token to make API requests
    if response.status_code == 200:
        token_response = response.json()
        global access_token
        access_token = token_response.get('access_token')
        refresh_token = token_response.get('refresh_token')
        
        if access_token:
            # Example API request: Get user profile information
            profile_url = 'https://api.spotify.com/v1/me'
            headers = {
                'Authorization': f'Bearer {access_token}',
            }

            profile_response = requests.get(profile_url, headers=headers)
            profile_data = profile_response.json()

            if profile_response.status_code == 200:
                profile_data = profile_response.json()
                print('Profile Data:', profile_data)  # Print the entire JSON response

                # Extract user ID from the response
                global user_id
                global email
                user_id = profile_data.get('id')
                print(user_id)
                display_name = profile_data.get('display_name')
                email = profile_data.get('email')

                global user_data
                user_data = {'User ID': user_id, 'Display Name': display_name, 'Email': email}
                #collection.insert_one(data)

                # Print the user ID and other information
                print('User ID:', user_id)
                print('Display Name:', display_name)
                print('Email:', email)

                # Add any additional processing or rendering logic as needed
                #create_top_tracks_playlist(user_id, access_token, num_songs, 1200)

                response_data = {'User_ID': user_id, 'Display Name': display_name, 'Email': email,}


                #return jsonify(response_data)
                return redirect("http://localhost:3000/webpage")
            

            else:
                error_message = profile_data.get('error', {}).get('message')
                return jsonify({'error': error_message})
        
    
    return jsonify({'error': 'Access token not obtained.'})

from flask import request, jsonify, make_response

@app.route('/api/past_trips', methods=['GET'])
def past_trips():
    # Get the 'n' query parameter, default to 10 if not provided
    n = request.args.get('n', default=10, type=int)

    # Get the user_id from the request (this should be adjusted based on how you're passing the user_id)
    user_id = request.args.get('user_id')

    if user_id:
        user_doc = collection.find_one({'User ID': user_id})

        if user_doc:
            # Retrieve the trip history array
            trip_history = user_doc.get('trip', [])

            # Limit to 'n' number of trips
            limited_trips = trip_history[:n]

            # Convert list of trips to dictionary format
            response = {str(index): trip for index, trip in enumerate(limited_trips)}

            return jsonify(response)
        else:
            # Return a 404 error response if no user is found
            return make_response(jsonify({'error': f"No user found with ID: {user_id}"}), 404)
    else:
        # Return a 400 error response if no user_id is provided
        return make_response(jsonify({'error': "No user_id provided"}), 400)


# access_token = access

if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)