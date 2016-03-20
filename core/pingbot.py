"""
This module simply makes accessing all the scripts easier without having to import everything for each module you want to use.
"""
from core.config import *
from core.errors import *
from core.logs import *
from core.module_check import *
from core.osu import *
from core.search import *
from core.updater import *
from core.util import *
from core.wunderground import *

osu = osu()
module_check = Checklist()
logs = LogManager()
error = ErrorsManager()
config_m = ConfigLoader()
wunderground = WundergroundAPI()
util = Util()
updater = Updater()
search = Search()
search_div = Div()

class PingbotCore:
	def update_check(self, url):
		updater.check_updates(url)

	def value_download(self, url, value, directory):
		return updater.download_value(url, value, directory)

	def file_delete(self, file):
		updater.delete_file(file)

	def retrieve_url(self, input_url, file_name):
		return updater.url_retrieve(input_url, file_name)

	def custom_command(self, message):
		return util.custom_command(message)

	def add_command(self, cmd, string):
		util.add_command(cmd, string)

	def manipulate_text(self, text, text_length, text_x, text_y, image_name, set_font):
		return util.manipulate_text(text, text_length, text_x, text_y, image_name, set_font)

	def is_owner(self, ctx):
		return util.is_owner(ctx)

	def is_bot_admin(self, ctx):
		return util.is_bot_admin(ctx)

	def reset(self, ctx, cog_list, last_loaded_cog):
		return util.reset(ctx, cog_list, last_loaded_cog)

	def wunderground_set_key(self, key):
		wunderground.set_key(key)

	def wunderground_weather_get(self, zip_code, value, get_location=False):
		return wunderground.weather_get(zip_code, value, get_location)

	def return_error(self, error_type, name, info):
		error.return_error(error_type, name, info)

	def subtle_error(self, name, info="Error has occured. Ignoring."):
		error.subtle_error(name, info)

	def config_load(self, sys, name):
		return config_m.load(sys, name)

	def config_load_cc(self, sys, name):
		return config_m.load_cc(name)

	def config_load_real(self, name):
		return config_m.load_real(name)

	def config_load_ini(self, file_name, section, option):
		return config_m.load_ini(file_name, section, option)

	def config_write_ini(self, file_name, section, option, value):
		config_m.write_ini(file_name, section, option, value)

	def config_save_json(self, sys=False):
		config_m.save(sys)

	def search_for_lib(self, module_name):
		module_check.search_for_lib(module_name)

	def subtle_sfl(self, module_name):
		module_check.subtle_sfl(module_name)

	def write_log(self, text):
		logs.write_log(text)

	def osu_set_key(self, key):
		osu.set_key(key)

	def osu_get_beatmap(self, name, value, parameters='m=0'):
		return osu.get_beatmap(name, value, parameters)

	def osu_get_user(self, name, value, parameters='m=0'):
		return osu.get_user(name, value, parameters)

	def search_standard(self, search_link, query_string='bacon'):
		return search.search(search_link, query_string)

	def search_youtube(self, query_string):
		return search.youtube(query_string)

	def search_div_set_link(self, url, query):
		search_div.div_set_link(url, query)

	def search_div_get(self, content):
		return search_div.div_get('class', content)