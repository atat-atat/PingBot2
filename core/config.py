import json
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
			self.data = sys_data.get(name)
		elif sys == False:
			self.data = json_data.get(name)
		return self.data

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