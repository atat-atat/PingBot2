"""
Retrieve information from Wunderground.
For values, see https://www.wunderground.com/weather/api/d/docs
"""
import urllib
from urllib.request import urlopen
import json

class WundergroundAPI:
	def set_key(self, key):
		self.key = key

	def weather_get(self, zip_code, value, get_location=False):
		url = "http://api.wunderground.com/api/" + self.key +    "/geolookup/conditions/q/PA/" + zip_code + ".json"
		f = urllib.request.urlopen(url)
		json_string = f.read().decode('utf-8')
		parsed_json = json.loads(json_string)
		if get_location == False:
			self.result = parsed_json['current_observation'][value]
		elif get_location == True:
			self.result = parsed_json['location'][value]
		return self.result