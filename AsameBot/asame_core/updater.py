import urllib.request
from urllib.request import Request, urlopen
import json
import os
from core.config import ConfigLoader
from core.colors import colors

c = ConfigLoader()

class Updater:
	def check_updates(self, url):
		cur_version = c.load(True, 'sys_version')
		urllib.request.urlretrieve(url, os.path.join('./core/sys/realver.json'))
		real_version = c.load_real('real_version')
		if cur_version < real_version:
			print(colors.cred+"There is a new version of PingBot available! ("+real_version+")")
			print("Please go to https://github.com/oppers/PingBot2 and update your PingBot!"+colors.cwhite)
		os.remove('./core/sys/realver.json')

	def download_value(self, url, value, directory):
		urllib.request.urlretrieve(url, os.path.join(directory))
		real_version = c.load_real(value)
		return real_version

	def delete_file(self, file):
		os.remove(file)

	def url_retrieve(self, input_url, file_name):
		result = urllib.request.urlretrieve(input_url, './core/sys/cache/' + file_name)
		return result