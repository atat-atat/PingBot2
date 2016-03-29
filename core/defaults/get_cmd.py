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
		self.no_command_pm = pingbot.config_load_msg('no_command_pm')
		self.enable_osu = pingbot.config_load(False, 'enable_osu')
		self.enable_wunderground = pingbot.config_load(False, 'enable_wunderground')

		pingbot.init_command('join_date')
		pingbot.init_command('game')
		pingbot.init_command('userid')
		pingbot.init_command('serverid')
		pingbot.init_command('chanid')
		pingbot.init_command('userinfo')
		pingbot.init_command('serverinfo')
		pingbot.init_command('osu_get')
		pingbot.init_command('weather')
		pingbot.init_command('get_logs')
		pingbot.init_command('clean_logs')
		pingbot.init_command('find')
		pingbot.init_command('get_invite')

	@commands.command(pass_context=True)
	async def join_date(self, ctx, member : discord.Member=None):
		"""
		Returns the join date of a user.
		"""
		if ctx.message.channel.is_private:
			await self.bot.say(self.no_command_pm)
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
			await self.bot.say(self.no_command_pm)
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
			await self.bot.say(self.no_command_pm)
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
			await self.bot.say(self.no_command_pm)
			return
		server = ctx.message.author.server
		await self.bot.say("The ID of `{}` is `{}`".format(server.name, server.id))

	@commands.command(pass_context=True)
	async def chanid(self, ctx, channel : discord.Channel=None):
		"""
		Returns the ID of a channel.
		"""
		if ctx.message.channel.is_private:
			await self.bot.say(self.no_command_pm)
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
		if ctx.message.channel.is_private:
			await self.bot.say(self.no_command_pm)
			return
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
			await self.bot.say(self.no_command_pm)
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
		if ctx.message.channel.is_private:
			await self.bot.say(self.no_command_pm)
			return
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

	@commands.command(hidden=True)
	async def osu_get_u(self, user : str, info : str):
		if self.enable_osu == True:
			osu_key = pingbot.config_load(False, 'osu_key')
			pingbot.osu_set_key(osu_key)

			information = pingbot.osu_get_user(user, info)
			await self.bot.say(information)

	@commands.command(hidden=True)
	async def osu_get_b(self, info1 : str, info2 : str):
		if self.enable_osu == True:
			osu_key = pingbot.config_load(False, 'osu_key')
			pingbot.osu_set_key(osu_key)

			information = pingbot.osu_get_beatmap(info1, info2)
			await self.bot.say(information)

	@commands.command()
	async def weather(self, zip_code : str):
		"""
		Returns weather information based on a zip code.
		"""
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

	#Logging commands- 
	@commands.group(pass_context=True)
	async def get_logs(self, ctx):
		"""
		Log management command.
		"""
		if pingbot.is_bot_admin(ctx) or pingbot.is_owner(ctx):
			pass
		else:
			await self.bot.say(self.no_perm_msg)
			return
		if ctx.invoked_subcommand is None:
			await self.bot.say("You must specify the type.")

	@get_logs.command(name='bot', pass_context=True)
	async def _logbot(self, ctx, limit : int = 30):
		"""
		Get messages sent by the bot.
		"""
		if pingbot.is_bot_admin(ctx) or pingbot.is_owner(ctx):
			pass
		else:
			await self.bot.say(self.no_perm_msg)
			return
		counter = 0
		async for message in self.bot.logs_from(ctx.message.channel, limit):
			if message.author == self.bot.user:
				output = "**[LOGS_FROM: {1.author.name}][{0}][{1.timestamp}][{1.server}][#{1.channel}]**: {1.content}".format(counter, message)
				counter += 1
				await self.bot.whisper(output)
		await self.bot.say("PingBot has sent {} messages within the past {} messages.".format(counter, limit))

	@get_logs.command(name='user', pass_context=True)
	async def _loguser(self, ctx, user : discord.Member=None, limit : int = 30):
		"""
		Get messages sent by a user.
		"""
		if pingbot.is_bot_admin(ctx) or pingbot.is_owner(ctx):
			pass
		else:
			await self.bot.say(self.no_perm_msg)
			return
		if user == None:
			await self.bot.say("You must specify the user.")
			return
		counter = 0
		async for message in self.bot.logs_from(ctx.message.channel, limit):
			if message.author == user:
				output = "**[LOGS_FROM: {1.author.name}][{0}][{1.timestamp}][{1.server}][#{1.channel}]**: {1.content}".format(counter, message)
				counter += 1
				await self.bot.whisper(output)
		await self.bot.say("{} has sent {} messages within the past {} messages.".format(user.name, counter, limit))

	@get_logs.command(name='all', pass_context=True)
	async def _logall(self, ctx, limit : int = 50):
		"""
		Returns a log of past messages.
		"""
		if pingbot.is_bot_admin(ctx) or pingbot.is_owner(ctx):
			pass
		else:
			await self.bot.say(self.no_perm_msg)
			return
		counter = 0
		async for message in self.bot.logs_from(ctx.message.channel, limit):
			output = "**[{0}][{1.timestamp}][{1.server}][#{1.channel}][{1.author.name}]**: {1.content}".format(counter, message)
			counter += 1
			await self.bot.whisper(output)

	@commands.group(pass_context=True)
	async def clean_logs(self, ctx):
		"""
		Chat log cleaner.
		"""
		if pingbot.is_bot_admin(ctx) or pingbot.is_owner(ctx):
			if ctx.invoked_subcommand is None:
				await self.bot.say("You must specify the type.")
		else:
			await self.bot.say("You do not have permission to use this command.")

	@clean_logs.command(name='user', pass_context=True)
	async def _cleanuser(self, ctx, user : discord.Member = None, limit : int = 30):
		"""
		Clean messages sent by a specific user.
		"""
		if pingbot.is_bot_admin(ctx) or pingbot.is_owner(ctx):
			pass
		else:
			await self.bot.say("You do not have permission to use this command.")
			return
		if user == None:
			await self.bot.say("You must specify the user.")
			return
		async for message in self.bot.logs_from(ctx.message.channel, limit):
			if message.author == user:
				await self.bot.delete_message(message)

	@clean_logs.command(name='all', pass_context=True)
	async def _cleanall(self, ctx, limit : int = 1000):
		"""
		Clean all chat logs.
		"""
		if pingbot.is_bot_admin(ctx) or pingbot.is_owner(ctx):
			pass
		else:
			await self.bot.say("You do not have permission to use this command.")
			return
		async for message in self.bot.logs_from(ctx.message.channel, limit):
			await self.bot.delete_message(message)

	@commands.group(pass_context=True)
	async def find(self, ctx):
		"""
		Experimental information finder.
		"""
		if ctx.invoked_subcommand is None:
			await self.bot.say("You must specify the type.")

	@find.command(name='user', pass_context=True)
	async def _finduser(self, ctx, *, user : str=None):
		"""
		Find a member that starts with a specific keyword.
		"""
		if user == None:
			await self.bot.say("You must specify the user.")
			return
		found = 0
		found_members = []
		for member in ctx.message.server.members:
			if user.lower() in member.name.lower() or user in "<@"+member.id+">" or user in member.discriminator or user.lower() == member.name.lower():
				found += 1
				await self.bot.say("`{}` (`#{}`) : `{}`".format(member.name, member.discriminator, member.id))
		await self.bot.say("Found {} users with that name/ID.".format(found))

	@find.command(name='channel', pass_context=True)
	async def _findchan(self, ctx, *, chan : str=None):
		"""
		Find a channel that starts with a specific keyword.
		"""
		if chan == None:
			await self.bot.say("You must specify the channel.")
			return
		found = 0
		for channel in ctx.message.server.channels:
			if chan.lower() in channel.name.lower() or chan in "<#"+channel.id+">" or chan == channel.name.lower():
				found += 1
				await self.bot.say("`#{}` : `{}`".format(channel, channel.id))
		await self.bot.say("Found {} channels with that name/ID.".format(found))

	@commands.command()
	async def get_invite(self, server_name : str):
		"""
		Gets the invite link of a server that the bot is currently on.
		"""
		for server in self.bot.servers:
			if server_name.lower() in server.name.lower():
				invite = await self.bot.create_invite(server, max_age=0, max_uses=0, temporary=False, xkcd=False)
				await self.bot.say(invite)
				return
		await self.bot.say("Server not found.")

def setup(bot):
    bot.add_cog(GetInfo(bot))