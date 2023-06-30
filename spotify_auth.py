import requests
from urllib.parse import quote

# Client credentials
client_id = ''
client_secret = ''
redirect_uri = 'http://127.0.0.1:5000/'

# Step 1: Authorization - Redirect user to Spotify's authorization page

# Construct the authorization URL
auth_url = 'https://accounts.spotify.com/authorize'
auth_params = {
    'client_id': client_id,
    'response_type': 'code',
    'redirect_uri': quote(redirect_uri, safe=''),
    'scope': 'user-read-private user-read-email',  # Add necessary scopes
}

# Redirect the user to the authorization URL
auth_redirect_url = auth_url + '?' + '&'.join([f'{k}={v}' for k, v in auth_params.items()])
print('Please visit the following URL to authorize your application:')
print(auth_redirect_url)

# Step 2: Obtain authorization code - Handle redirect URI and retrieve the code

# After the user grants permission, Spotify will redirect to your specified redirect URI with an authorization code.
authorization_code = input('Enter the authorization code from the redirected URL: ')

# Step 3: Exchange authorization code for access token

# Make a POST request to Spotify's token endpoint
token_url = 'https://accounts.spotify.com/api/token'
token_data = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'authorization_code',
    'code': authorization_code,
    'redirect_uri': redirect_uri,
}

response = requests.post(token_url, data=token_data)

# Parse the response JSON
token_response = response.json()

# Extract access token and refresh token
access_token = token_response.get('access_token')
refresh_token = token_response.get('refresh_token')

# Step 4: Use the access token to make API requests

if access_token:
    # Example API request: Get user profile information
    profile_url = 'https://api.spotify.com/v1/me'
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    
    profile_response = requests.get(profile_url, headers=headers)
    profile_data = profile_response.json()
    
    if profile_response.status_code == 200:
        print('User profile information:')
        print('Display name:', profile_data.get('display_name'))
        print('Email:', profile_data.get('email'))
    else:
        print('Error retrieving user profile:', profile_data)
else:
    print('Access token not obtained.')
