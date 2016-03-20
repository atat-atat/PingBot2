import json
import configparser
from core.colors import colors
from core.errors import ErrorsManager

e = ErrorsManager()

class ConfigLoader:
	def load(self, sys, name):
		with open('./core/config/bot.json', 'r') as config_file:
			json_data = json.load(config_file)
		with open('./core/sys/system.json', 'r') as system_file:
			sys_data = json.load(system_file)
		if sys == True:
			return sys_data.get(name)
		elif sys == False:
			return json_data.get(name)

	def load_cc(self, name):
		with open('./core/config/bot.json', 'r') as config_file:
			json_data = json.load(config_file)
		with open('./core/sys/system.json', 'r') as system_file:
			sys_data = json.load(system_file)
		with open('./core/config/custom_commands.json', 'r') as cc_file:
			cc_data = json.load(cc_file)
		self.data = cc_data.get(name)
		return self.data

	def load_real(self, name):
		with open('./core/sys/realver.json', 'r') as real_file:
			real_data = json.load(real_file)
		self.data = real_data.get(name)
		return self.data

	def load_ini(self, file_name, section, option):
		config = configparser.SafeConfigParser()
		config.read('./core/config/' + file_name)
		return config.get(section, option)

	def write_ini(self, file_name, section, option, value):
		config = configparser.ConfigParser()
		config.read('./core/config/' + file_name)
		config[section][option] = value
		with open('./core/config/' + file_name, 'w') as configfile:
			config.write(configfile)

	def save(self, sys=False):
		with open('./core/config/bot.json', 'r') as config_file:
			json_data = json.load(config_file)
		with open('./core/sys/system.json', 'r') as system_file:
			sys_data = json.load(system_file)
		if sys != True:
			with open('./core/config/bot.json', 'w') as config_file:
				config_file.write(json.dumps(json_data, sort_keys=True, indent=4, separators=(',', ': ')))
		else:
			with open('./core/sys/system.json', 'w') as config_file:
				config_file.write(json.dumps(sys_data, sort_keys=True, indent=4, separators=(',', ': ')))