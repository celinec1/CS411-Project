

import base64
import requests



client_id = '3a35c0bb12b54e1f8f0602a408bc6bf3'
client_secret = '17391461037d4d1788e03c089bd4319d'


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

url = 'https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb'
headers = {
    'Authorization': 'Bearer BQBgj_QEsMbvr9Mul8yD5_BohTmZ__havoYedSME7uuPqqYkCMa2BJNfqyzFBz7ECLuOa3kAeUezsPvTPHJhBX_RHg_4_3gYoS8HOAQbAinceVDMCmE'
}




#accesstoken = 'BQAExJOnCakf_dx2nhW5EaWnstCDDMqjUWtcqn90bmb4CCb0B9Ee_QPTR9ufHDIyxJ8jiDgv_lUltqU1IBr-0tO4WUvICOaP6sZW20_Bd3cz638hpRA'