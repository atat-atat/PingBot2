import json
import configparser
from core.colors import colors
from core.errors import ErrorsManager

e = ErrorsManager()

class ConfigLoader:
	def __init__(self):
		self.user_config_dir = './user/config/'
		self.sys_config_dir = './core/sys/'
		self.data_dir = './core/data/'
		self.user_config = self.user_config_dir + 'bot.json'
		self.user_msgs = self.user_config_dir + 'messages.json'
		self.system_config = self.sys_config_dir + 'system.json'

	def load(self, sys, name):
		with open(self.user_config, 'r') as config_file:
			json_data = json.load(config_file)
		with open(self.system_config, 'r') as system_file:
			sys_data = json.load(system_file)
		if sys == True:
			return sys_data.get(name)
		elif sys == False:
			return json_data.get(name)

	def load_direct(self, file_name, name):
		with open(file_name, 'r') as json_file:
			json_data = json_file.get(name)
		return json_data

	def load_cc(self, name):
		with open(self.data_dir + 'custom_commands.json', 'r') as cc_file:
			cc_data = json.load(cc_file)
		self.data = cc_data.get(name)
		return self.data

	def load_real(self, name):
		with open(self.sys_config_dir + 'realver.json', 'r') as real_file:
			real_data = json.load(real_file)
		self.data = real_data.get(name)
		return self.data

	def load_ini(self, file_name, section, option):
		config = configparser.SafeConfigParser()
		config.read(self.user_config_dir + file_name)
		return config.get(section, option)

	def write_ini(self, file_name, section, option, value):
		config = configparser.ConfigParser()
		config.read(self.user_config_dir + file_name)
		config[section][option] = value
		with open(self.user_config_dir + file_name, 'w') as configfile:
			config.write(configfile)

	def load_msg(self, name):
		with open(self.user_msgs, 'r') as msgs_file:
			data = json.load(msgs_file)
		return data.get(name)

	def json_append(self, file_name, name, value):
		with open(file_name) as json_file:
			json_data = json.loads(json_file)
		json_data[name].append(value)

	def save(self, sys=False):
		with open(self.user_config, 'r') as config_file:
			json_data = json.load(config_file)
		with open(self.system_config, 'r') as system_file:
			sys_data = json.load(system_file)
		if sys != True:
			with open(self.user_config, 'w') as config_file:
				config_file.write(json.dumps(json_data, sort_keys=True, indent=4, separators=(',', ': ')))
		else:
			with open(self.system_config, 'w') as config_file:
				config_file.write(json.dumps(sys_data, sort_keys=True, indent=4, separators=(',', ': ')))