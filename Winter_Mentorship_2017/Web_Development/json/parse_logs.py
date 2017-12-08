import json

with open('2017-12-08.json') as json_file:
	data = json.load(json_file)
	for p in data:
		print(p['text'])
		print("")
