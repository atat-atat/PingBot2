from core.config import ConfigLoader
import configparser
from PIL import Image, ImageFont, ImageDraw
import json

c = ConfigLoader()

class Util:
	def custom_command(self, message):
		customcommand = message.split('!')[1]
		try:
			command = c.load_cc(customcommand)
			return command
		except KeyError:
			return None

	def add_command(self, cmd, string):
		with open('./core/config/custom_commands.json') as f:
			json_decoded = json.load(f)

		json_decoded[cmd] = string

		with open('./core/config/custom_commands.json', 'w') as f:
			json.dump(json_decoded, f)

	def manipulate_text(self, text, text_length, text_x, text_y, image_name, set_font):
		img = Image.open("./core/images/"+image_name+".jpg")
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype(set_font, text_length)
		draw.text((text_x, text_y),"{}".format(text),(0,0,0),font=font)
		img.save('./core/images/'+image_name+'-edit.jpg')
		return "./core/images/"+image_name+"-edit.jpg"

	def is_owner(self, ctx):
		if ctx.message.author.id == ctx.message.server.owner.id:
			return True
		else:
			return False

	def is_bot_admin(self, ctx):
		admins = c.load(False, 'admins')
		if ctx.message.author.id in admins:
			return True
		else:
			return False

	def reset(self, ctx, cog_list, last_loaded_cog):
		if self.is_bot_admin(ctx) == True:
			for i in cog_list:
				bot.unload_extension(i)
				bot.load_extension(i)
			for i in last_loaded:
				bot.unload_extension(i)
				bot.load_extension(i)
			return True
		else:
			return False