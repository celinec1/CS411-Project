

import requests
from urllib.parse import urlencode, urlparse, parse_qs

# Step 1: Authorization Request

client_id = '3a35c0bb12b54e1f8f0602a408bc6bf3'

client_secret = '17391461037d4d1788e03c089bd4319d'

redirect_uri = 'http://localhost:8000/callback'
scope = 'user-library-read playlist-modify-private'
state = 'some-random-state'

# Build the authorization URL
auth_url = 'https://accounts.spotify.com/authorize'
params = {
    'client_id': client_id,
    'response_type': 'code',
    'redirect_uri': redirect_uri,
    'scope': scope,
    'state': state
}
auth_request_url = auth_url + '?' + urlencode(params)

# Redirect the user to the authorization URL
print('Please visit the following URL to authorize the application:')
print(auth_request_url)

# Simulate the callback URL after the user grants authorization
# Replace 'YOUR_AUTHORIZATION_CODE' with the actual authorization code received in the callback URL
simulated_callback_url = 'http://localhost:8000/callback?code=YOUR_AUTHORIZATION_CODE&state=some-random-state'

# Extract the authorization code from the simulated callback URL
parsed_url = urlparse(simulated_callback_url)
query_params = parse_qs(parsed_url.query)
authorization_code = query_params.get('code')
returned_state = query_params.get('state')

# Verify the state parameter to prevent CSRF attacks
if not authorization_code or not returned_state or returned_state[0] != state:
    raise Exception('Invalid authorization callback.')

authorization_code = authorization_code[0]

# Step 3: Exchange Authorization Code for Access Token

token_url = 'https://accounts.spotify.com/api/token'

# Exchange the authorization code for an access token
token_params = {
    'grant_type': 'authorization_code',
    'code': authorization_code,
    'redirect_uri': redirect_uri,
    'client_id': client_id,
    'client_secret': client_secret
}

response = requests.post(token_url, data=token_params)
response_data = response.json()

# Extract the access token and refresh token from the response
access_token = response_data.get('access_token')
refresh_token = response_data.get('refresh_token')

if not access_token:
    raise Exception('Failed to obtain access token.')

# Step 4: Use the Access Token

# Example API request to retrieve the user's liked songs
api_url = 'https://api.spotify.com/v1/me/tracks'
headers = {
    'Authorization': 'Bearer ' + access_token
}

response = requests.get(api_url, headers=headers)
liked_songs_data = response.json()

# Process the liked songs data as per your requirements
print('Liked Songs:', liked_songs_data)