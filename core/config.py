import json

class Config(self, config_name):
	with(open('config.json', 'r')) as config_file:
		self.json_data = json.load(config_file)