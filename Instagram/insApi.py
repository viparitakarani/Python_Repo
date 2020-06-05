#!/usr/local/anaconda3/bin/python


import requests
import json


#grep instagram profile data
resIg = requests.get("https://api.instagram.com/v1/users/self/media/recent?count=20&access_token=<access_token>")
resjsonIg = json.loads(resIg.text)
for post in resjsonIg['data']:
	print('id : '+post['id'])
	print('username : '+post['user']['username'])
	print('caption : '+post['caption']['text'])
	print('likes : %s' % (post['likes']['count']))
	print('link : '+post['link'])

	if post['location'] is not None:
		print('location : '+post['location']['name'])
		resMap = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?query='+post['location']['name']+'&region=jakarta&key=<google api key>')
		resjsonMap = json.loads(resMap.text)
		for loc in resjsonMap['results']:
			print('Location Type : %s' % (loc['types']))
	print("===========================================================")