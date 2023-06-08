from flask import Flask, render_template, request, redirect, url_for
import requests

import requests
from urllib.parse import quote
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

# Step 1: Authorization - Redirect user to Spotify's authorization page
@app.route('/')
def index():
    # Construct the authorization URL
    auth_url = 'https://accounts.spotify.com/authorize'
    auth_params = {
        'client_id': '3a35c0bb12b54e1f8f0602a408bc6bf3',
        'response_type': 'code',
        'redirect_uri': quote('http://localhost:8000/callback', safe=''),
        'scope': 'user-read-private user-read-email',  # Add necessary scopes
    }

    # Redirect the user to the authorization URL
    auth_redirect_url = auth_url + '?' + '&'.join([f'{k}={v}' for k, v in auth_params.items()])
    return redirect(auth_redirect_url)

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
                user_id = profile_data.get('id')
                display_name = profile_data.get('display_name')
                email = profile_data.get('email')

                # Print the user ID and other information
                print('User ID:', user_id)
                print('Display Name:', display_name)
                print('Email:', email)


                # Add any additional processing or rendering logic as needed
                return render_template('success.html', display_name=display_name, email=email)
            else:
                error_message = profile_data.get('error', {}).get('message')
                return render_template('error.html', error_message=error_message)

    return render_template('error.html', error_message='Access token not obtained.')

if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)

if __name__ == '__main__':
    app.run(debug=True)
