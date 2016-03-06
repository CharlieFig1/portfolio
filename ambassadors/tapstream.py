import requests, json

REFRESH_TOKEN = 'cUZ5gtgaqicmtAf4P48sp8arXajArG'

def refresh_token():
	payload = {'refresh_token': REFRESH_TOKEN, 'grant_type': 'refresh_token', 
	'client_id': 'tapstream_web'}
	
	headers = {
	'Content-Type': 'application/x-www-form-urlencoded'
	}

	r = requests.post('https://app.tapstream.com/api/v1/token/', params=payload, headers=headers)

	response = r.json()
	return response