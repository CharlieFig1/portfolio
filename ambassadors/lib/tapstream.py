import urllib2
from urllib2 import Request, urlopen
from urllib import urlencode

def response_body():
	values = urlencode(
		{'username': 'admin@movablescience.com', 'password': 'M0vable123',
		 'grant_type': 'password', 'client_id': 'tapstream_web'}
		 )
	
	headers = {
	'Content-Type': 'application/x-www-form-urlencoded'
	}

	request = urllib2.Request('https://app.tapstream.com/api/v1/token/', data=values, headers=headers)

	try:
		response = urllib2.urlopen(request)
	except urllib2.HTTPError as e:
		if response.code != 200:
			print response.code
	else:
		print "OK"
	response_body = eval(response.read())
	print response_body["access_token"]
	return response_body

response_body()
# """
# {"token_type": "Bearer", "default_account_name": "figure1", "access_token": "6smzysB11bcp3DGr5TIXzkBHkFOOs7", 
# "scope": "api", "refresh_token": "Qvf3Qz95PcbzfEGCUDzpSwGSPIAz53"}
# """
# import urllib2
# import urllib
# import urlparse
# import json

# ACCESS_TOKEN = '6smzysB11bcp3DGr5TIXzkBHkFOOs7' # An OAuth access token, retrieved earlier

# url = 'https://app.tapstream.com/api/v1/reports/campaigns/?start_date=2015-10-01&end_date=2015-11-08'
# headers = {
#     'Authorization': 'Bearer ' + ACCESS_TOKEN,
# }
# request = urllib2.Request(url, headers=headers)
# response = urllib2.urlopen(request)
# account = json.loads(response.read())
# # print json.dumps(account, sort_keys=True,
# #                   indent=4, separators=(',', ': '))

# for url in account['breakdown']:
# 	print url['url']


# import requests

# ACCESS_TOKEN = 'owNssg1VxykOgnByqeCAsOkEsazsGq' 

# headers = {
#     'Authorization': 'Bearer ' + ACCESS_TOKEN,
# }

# url = 'https://app.tapstream.com/api/v1/reports/rollup/?dimensions=hit_param_value&metrics=converting_hit_count&filters=campaign_name|EXACT|Fall+Ambassadors+%282015%29&order_by=-converting_hit_count'
# r = requests.get(url, headers=headers)
# data = r.json()
# len(data)
# print data














