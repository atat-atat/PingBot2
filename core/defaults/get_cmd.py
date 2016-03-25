import discord
from discord.ext import commands
from core.pingbot import PingbotCore

import urllib
from urllib.request import urlopen
import json

pingbot = PingbotCore()

class GetInfo():
	def __init__(self, bot):
		self.bot = bot
		self.password = pingbot.config_load(False, 'password')
		self.allow_bot_changes = pingbot.config_load(False, 'user_bot_changes')
		self.no_perm_msg = pingbot.config_load_msg('no_perm_msg')
		self.no_user_found = pingbot.config_load_msg('no_user_found')
		self.enable_osu = pingbot.config_load(False, 'enable_osu')
		self.enable_wunderground = pingbot.config_load(False, 'enable_wunderground')

	@commands.command(pass_context=True)
	async def join_date(self, ctx, member : discord.Member=None):
		"""
		Returns the join date of a user.
		"""
		if ctx.message.channel.is_private:
			await self.bot.say("You cannot use this command in a PM.")
			return
		if member != None:
			await self.bot.say("User `{}` joined on `{}`!".format(member.name, member.joined_at))
		else:
			await self.bot.say(self.no_user_found)

	@commands.command(pass_context=True)
	async def game(self, ctx, member : discord.Member=None):
		"""
		Returns the currently playing game of a user.
		"""
		if ctx.message.channel.is_private:
			await self.bot.say("You cannot use this command in a PM.")
			return
		if member != None:
			await self.bot.say("`{}` is currently playing `{}`".format(member.name, member.game))
		else:
			await self.bot.say("You are currently playing `{}`".format(ctx.message.author.game))

	@commands.command(pass_context=True)
	async def userid(self, ctx, member : discord.Member=None):
		"""
		Returns the ID of a user.
		"""
		if ctx.message.channel.is_private:
			await self.bot.say("You cannot use this command in a PM.")
			return
		if member != None:
			await self.bot.say("The ID of `{}` is `{}`".format(member.name, member.id))
		else:
			await self.bot.say("Your ID is `{}`".format(ctx.message.author.id))

	@commands.command(pass_context=True)
	async def serverid(self, ctx):
		"""
		Returns the ID of the server.
		"""
		if ctx.message.channel.is_private:
			await self.bot.say("You cannot use this command in a PM.")
			return
		server = ctx.message.author.server
		await self.bot.say("The ID of `{}` is `{}`".format(server.name, server.id))

	@commands.command(pass_context=True)
	async def chanid(self, ctx, channel : discord.Channel=None):
		"""
		Returns the ID of a channel.
		"""
		if ctx.message.channel.is_private:
			await self.bot.say("You cannot use this command in a PM.")
			return
		if channel != None:
			await self.bot.say("The ID of `{}` is `{}`".format(channel.name, channel.id))
		else:
			await self.bot.say("The current channel ID is `{}`".format(ctx.message.channel.id))
		
	@commands.command(pass_context=True)
	async def userinfo(self, ctx, user : discord.Member=None):
		"""
		Shows information about a user.
		"""
		if user != None:
			member = user
		else:
			member = ctx.message.author
		roles = [role.name.replace('@', '(@)') for role in member.roles]
		await self.bot.say("""```[Showing information about {}]
   Name: {} ({})
     ID: {}
  Roles: {}
 Status: {}
 Joined: {}
Created: {}
Playing: {}
	AFK: {}
  Muted: {}
 Avatar: {}```
{}""".format(member.name, member.name, member.discriminator, member.id, ', '.join(roles), member.status, member.joined_at, member.created_at, member.game, member.is_afk, member.mute, member.avatar, member.avatar_url))


	@commands.command(pass_context=True)
	async def serverinfo(self, ctx):
		"""
		Returns the information of the server.
		"""
		if ctx.message.channel.is_private:
			await self.bot.say("You cannot use this command in a PM.")
			return
		server = ctx.message.author.server
		
		text_channels = 0
		for channel in server.channels:
			is_text = channel.type == discord.ChannelType.text
			text_channels += is_text
		voice_channels = len(server.channels) - text_channels
		roles = [role.name.replace('@', '(@)') for role in server.roles]
		await self.bot.say("""```[Showing information about {}]
	Name: {}
	  ID: {}
 Members: {}
Channels: {} (Voice: {})
  Region: {}
   Owner: {}
   Roles: {}
 Created: {}
    Icon: {}```
{}""".format(server.name, server.name, server.id, len(server.members), text_channels, voice_channels, server.region, server.owner, ', '.join(roles), server.created_at, server.icon, server.icon_url))

	@commands.command(pass_context=True)
	async def avatar(self, ctx, member : discord.Member=None):
		"""
		Gets the avatar of a user.
		"""
		if member != None:
			await self.bot.say("Avatar of `{}` is {}".format(member.name, member.avatar_url))
		else:
			await self.bot.say("Your avatar is {}".format(ctx.message.author.avatar_url))

	@commands.command()
	async def osu_user(self, _username : str):
		if self.enable_osu == True:
			osu_key = pingbot.config_load(False, 'osu_key')
			pingbot.osu_set_key(osu_key)
			pending = await self.bot.say("*...*")
			try:
				user_id = pingbot.osu_get_user(_username, 'user_id')
				username = pingbot.osu_get_user(_username, 'username')
				count300 = pingbot.osu_get_user(_username, 'count300')
				count100 = pingbot.osu_get_user(_username, 'count100')
				count50 = pingbot.osu_get_user(_username, 'count50')
				playcount = pingbot.osu_get_user(_username, 'playcount')
				ranked_score = pingbot.osu_get_user(_username, 'ranked_score')
				total_score = pingbot.osu_get_user(_username, 'total_score')
				level = pingbot.osu_get_user(_username, 'level')
				pp_raw = pingbot.osu_get_user(_username, 'pp_raw')
				accuracy = pingbot.osu_get_user(_username, 'accuracy')
				count_rank_ss = pingbot.osu_get_user(_username, 'count_rank_ss')
				count_rank_s = pingbot.osu_get_user(_username, 'count_rank_s')
				count_rank_a = pingbot.osu_get_user(_username, 'count_rank_a')
				country = pingbot.osu_get_user(_username, 'country')
				pp_country_rank = pingbot.osu_get_user(_username, 'pp_country_rank')
			except UnboundLocalError:
				await self.bot.say("That user does not exist.")
				await self.bot.delete_message(pending)
				return
			await self.bot.delete_message(pending)
			await self.bot.say("""```[Showing information about {}]
	 User: {} ({})
 Accuracy: {}
    Level: {}
Playcount: {}
  Country: {}
	   PP: {} (#{})
(300: {} | 100: {} | 50: {})
(SS: {} | S: {} | A: {})```
http://a.ppy.sh/{}""".format(username, username, user_id, accuracy, level, playcount, country, pp_raw, pp_country_rank, count300, count100, count50, count_rank_ss, count_rank_s, count_rank_a, user_id))

	@commands.command()
	async def osu_get_u(self, user : str, info : str):
		if self.enable_osu == True:
			osu_key = pingbot.config_load(False, 'osu_key')
			pingbot.osu_set_key(osu_key)

			information = pingbot.osu_get_user(user, info)
			await self.bot.say(information)

	@commands.command()
	async def osu_get_b(self, info1 : str, info2 : str):
		if self.enable_osu == True:
			osu_key = pingbot.config_load(False, 'osu_key')
			pingbot.osu_set_key(osu_key)

			information = pingbot.osu_get_beatmap(info1, info2)
			await self.bot.say(information)

	@commands.command()
	async def weather(self, zip_code : str):
		if self.enable_wunderground == True:
			wunderground_key = pingbot.config_load(False, 'wunderground_key')
			pingbot.wunderground_set_key(wunderground_key)

			location = pingbot.wunderground_weather_get(zip_code, 'city', get_location=True)
			icon_url = pingbot.wunderground_weather_get(zip_code, 'icon_url')
			weather = pingbot.wunderground_weather_get(zip_code, 'weather')
			temperature_string = pingbot.wunderground_weather_get(zip_code, 'temperature_string')
			dewpoint_string = pingbot.wunderground_weather_get(zip_code, 'dewpoint_string')
			feelslike_string = pingbot.wunderground_weather_get(zip_code, 'feelslike_string')
			relative_humidity = pingbot.wunderground_weather_get(zip_code, 'relative_humidity')
			wind_string = pingbot.wunderground_weather_get(zip_code, 'wind_string')
			wind_mph = pingbot.wunderground_weather_get(zip_code, 'wind_mph')
			wind_degrees = pingbot.wunderground_weather_get(zip_code, 'wind_degrees')
			observation_time = pingbot.wunderground_weather_get(zip_code, 'observation_time')

			await self.bot.say("```{}\nTemperature: {}\nDewpoint: {}\nFeelslike temperature: {}\nRelative humidity: {}\nWind direction: {}\nWind MPH: {}\nWind degrees: {}\n(Observation time: {})```\n{}".format(location, temperature_string, dewpoint_string, feelslike_string, relative_humidity, wind_string, wind_mph, wind_degrees, observation_time, icon_url))

def setup(bot):
    bot.add_cog(GetInfo(bot))