import json
import sys

with open(sys.argv[1], 'r') as json_file:
	data = json.load(json_file)
	string = ''
	for p in data:
		user = p['user']
		if user == 'U888HQS7K':
			user = 'Shashank'
		elif user == 'U88K2UW8Z':
			user = 'Utkarsh'
		string += '\n' + user + ':\n' + p['text'] + '\n'
	print(string)
