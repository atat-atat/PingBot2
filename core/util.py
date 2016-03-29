from core.config import ConfigLoader
import configparser
from PIL import Image, ImageFont, ImageDraw
import json

c = ConfigLoader()

class Util:
	def __init__(self):
		self.commands = []

	def custom_command(self, message):
		customcommand = message.split('!')[1]
		try:
			command = c.load_cc(customcommand)
			return command
		except KeyError:
			return None

	def add_command(self, cmd, string):
		with open('./core/data/custom_commands.json') as f:
			json_decoded = json.load(f)

		json_decoded[cmd] = string

		with open('./core/data/custom_commands.json', 'w') as f:
			json.dump(json_decoded, f)

	def manipulate_text(self, text, text_length, text_x, text_y, image_name, set_font):
		img = Image.open("./core/data/images/"+image_name+".jpg")
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype(set_font, text_length)
		draw.text((text_x, text_y),"{}".format(text),(0,0,0),font=font)
		img.save('./core/data/images/'+image_name+'-edit.jpg')
		return "./core/data/images/"+image_name+"-edit.jpg"

	def is_owner(self, ctx):
		if ctx.message.author.id == ctx.message.server.owner.id:
			return True
		else:
			return False

	#def is_moderator(self, ctx):
		#if ctx.message

	def is_bot_admin(self, ctx):
		admins = c.load(False, 'admins')
		if ctx.message.author.id in admins:
			return True
		else:
			return False

	def reset(self, bot, ctx, cog_dir1, cog_list, last_loaded_cog, cog_dir2, sys_cogs):
		if self.is_bot_admin(ctx) == True:
			for i in cog_list:
				bot.unload_extension(cog_dir1 + i)
				bot.load_extension(cog_dir1 + i)
			for i in last_loaded_cog:
				bot.unload_extension(cog_dir1 + i)
				bot.load_extension(cog_dir1 + i)
			for e in sys_cogs:
				bot.unload_extension(cog_dir2 + e)
				bot.load_extension(cog_dir2 + e)
			return True
		else:
			return False

	def init_command(self, command):
		if command in self.commands:
			return False
		else:
			self.commands.append(command)
			return True

	def get_commands(self):
		return self.commands