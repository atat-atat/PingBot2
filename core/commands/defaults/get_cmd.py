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
		self.no_perm_msg = pingbot.config_load(False, 'no_perm_msg')
		self.no_user_found = pingbot.config_load(False, 'no_user_found')
		self.enable_osu = pingbot.config_load(False, 'enable_osu')
		self.enable_wunderground = pingbot.config_load(False, 'enable_wunderground')

	@commands.command(pass_context=True)
	async def join_date(self, ctx, member : discord.Member=None):
		"""
		Returns the join date of a user.
		"""
		if member != None:
			await self.bot.say("User `{}` joined on `{}`!".format(member.name, member.joined_at))
		else:
			await self.bot.say(self.no_user_found)

	@commands.command(pass_context=True)
	async def game(self, ctx, member : discord.Member=None):
		"""
		Returns the currently playing game of a user.
		"""
		if member != None:
			await self.bot.say("`{}` is currently playing `{}`".format(member.name, member.game))
		else:
			await self.bot.say("You are currently playing `{}`".format(ctx.message.author.game))

	@commands.command(pass_context=True)
	async def userid(self, ctx, member : discord.Member=None):
		"""
		Returns the ID of a user.
		"""
		if member != None:
			await self.bot.say("The ID of `{}` is `{}`".format(member.name, member.id))
		else:
			await self.bot.say("Your ID is `{}`".format(ctx.message.author.id))

	@commands.command(pass_context=True)
	async def serverid(self, ctx):
		"""
		Returns the ID of the server.
		"""
		server = ctx.message.author.server
		await self.bot.say("The ID of `{}` is `{}`".format(server.name, server.id))

	@commands.command(pass_context=True)
	async def chanid(self, ctx, channel : discord.Channel=None):
		"""
		Returns the ID of a channel.
		"""
		if channel != None:
			await self.bot.say("The ID of `{}` is `{}`".format(channel.name, channel.id))
		else:
			await self.bot.say("The current channel ID is `{}`".format(ctx.message.channel.id))
		
	@commands.command(pass_context=True)
	async def userinfo(self, ctx, member : discord.Member=None):
		"""
		Shows information about a user.
		"""
		if member != None:
			await self.bot.say("```Showing information about {} -\r\nName: {}\r\nID: {}\r\nDiscriminator: {}\r\nStatus: {}\r\nJoined: {}\r\nCurrently Playing: {}\r\nAFK: {}\r\nMuted: {}\r\nDeafened: {}\r\nVoice Muted: {}\r\nSound Muted: {}\r\nAvatar: {}```\r\n{}".format(member.name, member.name, member.id, member.discriminator, member.status, member.joined_at, member.game, member.is_afk, member.mute, member.deaf, member.self_mute, member.self_deaf, member.avatar, member.avatar_url))
		else:
			await self.bot.say("```Showing information about {} -\r\nName: {}\r\nID: {}\r\nDiscriminator: {}\r\nStatus: {}\r\nJoined: {}\r\nCurrently Playing: {}\r\nAFK: {}\r\nMuted: {}\r\nDeafened: {}\r\nVoice Muted: {}\r\nSound Muted: {}\r\nAvatar: {}```\r\n{}".format(ctx.message.author.name, ctx.message.author.name, ctx.message.author.id, ctx.message.author.discriminator, ctx.message.author.status, ctx.message.author.joined_at, ctx.message.author.game, ctx.message.author.is_afk, ctx.message.author.mute, ctx.message.author.deaf, ctx.message.author.self_mute, ctx.message.author.self_deaf, ctx.message.author.avatar, ctx.message.author.avatar_url))


	@commands.command(pass_context=True)
	async def serverinfo(self, ctx):
		"""
		Returns the information of the server.
		"""
		server = ctx.message.author.server
		await self.bot.say("```Showing information about {}\r\nName: {}\r\nID: {}\r\nRegion: {}\r\nOwner: {}\r\nIcon: {}```\r\n{}".format(server.name, server.name, server.id, server.region, server.owner, server.icon, server.icon_url))

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
			osu_key = c.load(False, 'osu_key')
			o.set_key(osu_key)

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
			await self.bot.say("```User: {} ({})\r\nAccuracy: {}\r\nLevel: {}\r\nPlaycount: {}\r\nCountry: {}\r\nPP: {} (#{})\r\n(300: {} | 100: {} | 50: {})\r\n(SS: {} | S: {} | A: {})```".format(username, user_id, accuracy, level, playcount, country, pp_raw, pp_country_rank, count300, count100, count50, count_rank_ss, count_rank_s, count_rank_a))

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

			await self.bot.say("```{}\r\nTemperature: {}\r\nDewpoint: {}\r\nFeelslike temperature: {}\r\nRelative humidity: {}\r\nWind direction: {}\r\nWind MPH: {}\r\nWind degrees: {}\r\n(Observation time: {})```\r\n{}".format(location, temperature_string, dewpoint_string, feelslike_string, relative_humidity, wind_string, wind_mph, wind_degrees, observation_time, icon_url))

def setup(bot):
    bot.add_cog(GetInfo(bot))