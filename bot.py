"""
PingBot2; a bot for Discord made using Discord.py, made by Oppy/@@.
"""
from core.pingbot import PingbotCore
from core.colors import colors

from discord.ext import commands
import asyncio
import random
import sys
import os
import logging
import discord
import datetime

pingbot = PingbotCore()
bot = discord.Client()

pingbot.updater().update_check('https://dl.dropboxusercontent.com/s/1welpdvy23ycyih/realver.json?dl=0')

user_cogs_dir = "user.extensions."
sys_cogs_dir = "core.defaults."

sys_version = pingbot.config_load(True, 'sys_version')
bot_name = pingbot.config_load(False, 'bot_name')
bot_token = pingbot.config_load(False, 'bot_token')
email = pingbot.config_load(False, 'email')
password = pingbot.config_load(False, 'password')
cmd_prefix = pingbot.config_load(False, 'prefix')
pm_help = pingbot.config_load(False, 'pm_help')
bot_description = pingbot.config_load(False, 'description')
enable_delete_msg = pingbot.config_load(False, 'enable_delete_msg')
enable_welcome_msg = pingbot.config_load(False, 'enable_welcome_msg')
enable_offline_messenger = pingbot.config_load(False, 'enable_offline_messenger')
enable_random_games = pingbot.config_load(False, 'random_games')
enable_custom_commands = pingbot.config_load(False, 'enable_custom_commands')
startup_cogs = pingbot.config_load(False, 'startup_cogs')
banned_say_words = pingbot.config_load(False, 'banned_say_words')

no_perm_msg = pingbot.config_load_msg('no_perm_msg')
only_owner = pingbot.config_load_msg('only_owner')
annoyed = pingbot.config_load_msg('annoyed')
invalid_invite = pingbot.config_load_msg('invalid_invite_link')
server_farewell = pingbot.config_load_msg('server_farewell')
success = pingbot.config_load_msg('success_command')

admins = pingbot.config_load(False, 'admins')
no_command_users = pingbot.config_load(False, 'no_command_users')
no_delete = pingbot.config_load(False, 'no_delete')
no_say = pingbot.config_load(False, 'no_say')
no_welcome = pingbot.config_load(False, 'no_welcome')
enable_mention_message = pingbot.config_load(False, 'enable_mention_message')
mm_ifin = pingbot.config_load(False, 'mm_ifin')
mention_messages = pingbot.config_load(False, 'mention_messages')

bot_version = pingbot.config_load(True, 'sys_version')

pingbot.init_command('cog')
pingbot.init_command('set_show')
pingbot.init_command('servers')
pingbot.init_command('version')
pingbot.init_command('join')
pingbot.init_command('leave')
pingbot.init_command('ping')
pingbot.init_command('close')
pingbot.init_command('exit')
pingbot.init_command('shh')
pingbot.init_command('shh_del')

date = datetime.datetime.now()
current_date = '{0.month}-{0.day}-{0.year}'.format(date)

last_loaded = [] #last loaded cog(s)
sys_cogs = ["commands", "get_cmd"]

shh_list = []

os.system("title PingBot2 (Loading...)")

#-----------------------------

#File Logging
discord_logger = logging.getLogger('discord')
discord_logger.setLevel(logging.CRITICAL)
log = logging.getLogger()
log.setLevel(logging.INFO)
handler = logging.FileHandler(filename='./user/log/'+current_date+'.log', encoding='utf-8', mode='w')
log.addHandler(handler)

#-----------------------------

if __name__ == '__main__':
	bot = pingbot.TokenBot(command_prefix=cmd_prefix, description=bot_description, pm_help=pm_help)

	@bot.group(hidden=True, pass_context=True)
	async def cog(ctx):
		"""
		Cog-related commands.
		"""
		if ctx.invoked_subcommand is None:
			await bot.say("You must specify the cog action.")


	@cog.command(name='load', pass_context=True, hidden=True)
	async def _cogload(ctx, cog_name : str):
		"""
		Loads a cog.
		"""
		if pingbot.is_bot_admin(ctx):
			try:
				if cog_name not in sys.modules:
					bot.load_extension(cog_name)
					last_loaded.append(cog_name)
				else:
					await bot.say("The cog, `{}` has already been loaded!\nUse !reload to reload the cogs.".format(cog_name))
					return
			except Exception as e:
				await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
				print(colors.cred)
				print(e)
				print(colors.cwhite)
				return
			except discord.errors.ClientException as e:
				await bot.say("Failed to load extension!")
				print(colors.cred)
				print(e)
				print(colors.cwhite)
				return
			await bot.say("Successfully loaded `{}`.".format(cog_name))
		else:
			await bot.say(no_perm_msg)

	@cog.command(name='unload', pass_context=True, hidden=True)
	async def _cogunload(ctx, extension_name : str):
		"""
		Unloads a cog.
		"""
		if pingbot.is_bot_admin(ctx) == True:
			if cog_name in sys.modules:
				if extension_name in last_loaded:
					last_loaded.remove(cog_name)
				bot.unload_extension(cog_name)
				await bot.say("Successfully unloaded `{}`.".format(cog_name))
			else:
				await bot.say("`{}` is not loaded!".format(cog_name))
		else:
			await bot.say(no_perm_msg)

	@cog.command(name='reload', pass_context=True, hidden=True)
	async def _cogreload(ctx):
		"""
		Reloads all currently loaded cogs.
		"""
		if pingbot.is_bot_admin(ctx) == True:
			try:
				pingbot.reset(bot, ctx, user_cogs_dir, startup_cogs, last_loaded, sys_cogs_dir, sys_cogs)
				await bot.say("Successfully reloaded cogs.")
			except Exception as e:
				await bot.say("Something went wrong!\n```{}: {} ({})```".format(type(e), e, e.args))
				print(colors.cred+str(e)+colors.cwhite)

	@cog.command(name='list', pass_context=True, hidden=True)
	async def _coglist(ctx):
		"""
		Shows all cogs.
		"""
		if pingbot.is_bot_admin(ctx) == True:
			await bot.say("Startup cogs (`{}`):\n`{}`".format(len(startup_cogs), '\n'.join(startup_cogs)))
			await bot.say("Last loaded cogs (`{}`):\n`{}`".format(len(last_loaded), '\n'.join(last_loaded)))
			await bot.say("System cogs (`{}`): \n`{}`".format(len(sys_cogs), '\n'.join(sys_cogs)))

	@bot.command(pass_context=True, hidden=True)
	async def set_show(ctx, option : str):
		if pingbot.is_bot_admin(ctx) == True:
			if "password" not in option:
				setting = pingbot.config_load(False, option)
				if setting != None:
					await bot.say("`{}` is set to `{}`".format(option, setting))
				else:
					await bot.say("That setting does not exist!")
			else:
				await bot.say(annoyed)
		else:
			await bot.say(no_perm_msg)

	@bot.command(pass_context=True, hidden=True)
	async def servers(ctx):
		"""Returns all servers the bot is currently connected to."""
		#if pingbot.is_bot_admin(ctx) == True:
		servers = len(bot.servers)
		await bot.say("Currently connected to `%s` server(s)." % servers)
		if pingbot.is_bot_admin(ctx):
			for server in bot.servers:
				await bot.whisper('`{}` : `{}`'.format(server, server.id))
		#else:
			#await bot.say(no_perm_msg)

	@bot.command(hidden=True)
	async def version():
		"""
		Returns the version of PingBot, as well as the latest update-version.
		"""
		real_version = pingbot.updater().value_download('https://dl.dropboxusercontent.com/s/1welpdvy23ycyih/realver.json?dl=0', 'real_version', './core/sys/realver.json')
		pingbot.updater().file_delete('./core/sys/realver.json')
		if bot_version == real_version:
			version_msg = "(Up to date.)"
		else:
			version_msg = "**(Please update!)**"
		await bot.say("The currently installed PingBot version is, `{}`. Latest version is `{}` \n{}".format(bot_version, real_version, version_msg))

	@bot.command()
	async def join(url : str):
		"""
		Joins an invite link.
		"""
		try:
			#await bot.say(success)
			await bot.accept_invite(url)
		except discord.errors.NotFound:
			await bot.say(invalid_invite)

	@bot.command(pass_context=True)
	async def leave(ctx):
		"""
		Leaves a server.
		"""
		if pingbot.is_bot_admin(ctx) == True or pingbot.is_owner(ctx) == True:
			await bot.say(server_farewell)
			await bot.leave_server(ctx.message.server)
		else:
			await bot.say(only_owner)

	@bot.command()
	async def ping(other : str=None):
		"""
		Ping!
		"""
		actions = ["Pong!", "Missed!"]
		score = ["**It's hopeless.**", "**There's no point.**", "**You shouldn't exist.**", "**Why should you?**", "**There is no score.**", "**You should just quit.**", "**You'll keep going, won't you?**", "**It's honestly sad to watch you fail everyday.**", "**Your mother misses you very much.**"]
		if other == None:
			await bot.say(random.choice(actions))
			return
		elif other == 'score':
			await bot.say(random.choice(score))
			return
		else:
			await bot.say("Huh?")
			return

	@bot.command(pass_context=True, hidden=True)
	async def close(ctx):
		if pingbot.is_bot_admin(ctx) == True:
			await bot.say(logout)
			await bot.logout()
		else:
			await bot.say(no_perm_msg)

	@bot.command(pass_context=True, hidden=True)
	async def exit(ctx):
		if pingbot.is_bot_admin(ctx) == True:
			await bot.say(logout)
			await bot.logout()
			loop.close()
			sys.exit(0)
		else:
			await bot.say(no_perm_msg)

	@bot.command(pass_context=True)
	async def shh(ctx, user : discord.Member=None):
		"""
		Silences a user.
		"""
		if enable_delete_msg == True:
			await bot.say("This command is unavailable due to the fact that the `message-delete` function is enabled.")
			return
		else:
			if pingbot.is_bot_admin(ctx) == True or pingbot.is_owner(ctx) == True:
				if user == None:
					await bot.say("You must provide a user.")
					return
				if user.id in shh_list:
					await bot.say("That user has already been silenced.")
					return
				if user.id in admins:
					await bot.say(annoyed)
					return
				if user == ctx.message.author:
					await bot.say("You cannot silence yourself.")
					return
				if user == bot.user:
					await bot.say(annoyed)
					return
				shh_list.append(user.id)
				#await bot.server_voice_state(user, mute=True, deafen=False)
				await bot.say("*Shhh, {}*".format(user.name))
			else:
				await bot.say(no_perm_msg)

	@bot.command(pass_context=True)
	async def shh_del(ctx, user : discord.Member=None):
		"""
		Lets a user speak.
		"""
		if enable_delete_msg == True:
			await bot.say("This command is unavailable due to the fact that the `message-delete` function is enabled.")
			return
		else:
			if pingbot.is_bot_admin(ctx) == True or pingbot.is_owner(ctx) == True:
				if user == None:
					await bot.say("You must provide a user.")
					return
				shh_list.remove(user.id)
				#await bot.server_voice_state(user, mute=False)
				await bot.say("{} can now speak.".format(user.name))
			else:
				await bot.say(no_perm_msg)

	#-----------------------------
	#Bot events

	#display information when the bot is ready.
	@bot.event
	async def on_ready():
		print(colors.cgreen+"Successfully loaded PingBot!")
		print("Currently running version; %s" % colors.bwhite+colors.cblue+sys_version+colors.bblack+colors.cgreen)
		print("--------------------------------------")
		print("User: %s" % bot.user.name)
		print("ID: %s" % bot.user.id)
		servers = len(bot.servers) #get amount of servers connected to
		print("Servers ({}):".format(servers))
		for server in bot.servers: #show a list of servers that the bot is currently connected to
			print("	{} : {}".format(server.name,server.id))
		print("Cogs ({}): {}".format(len(startup_cogs), ', '.join(startup_cogs)))
		print(colors.cwhite)

		for i in startup_cogs:
			bot.load_extension(user_cogs_dir + i)

		for e in sys_cogs:
			bot.load_extension(sys_cogs_dir + e)

		games = pingbot.config_load(False, 'games')
		await bot.change_status(discord.Game(name="{}".format(random.choice(games)),idle=None))

		title = bot.user.name #Set command prompt window caption to bot name
		
		os.system("title "+title+" (PingBot2)")

		print(" ")

	@bot.event
	async def on_message(msg):
		output = "[{0.timestamp}][{0.server}][{0.channel}][{0.author}]: {0.content}".format(msg)
		log.info(output)
		#output.encode('utf-8')
		#if '\U0'.lower() in output:
			#output.replace('\U0', ':ok_hand:')
			#print(output.replace('\U0', ':ok_hand:'))
			#return
		#try:
			#print(output)
		#except UnicodeEncodeError:
			#print("[Unicode Character]")
		output_encode = output.encode('utf-8')
		output_final = str(output_encode)
		print(output_final)

		if enable_mention_message == True:
			if mm_ifin == True:
				if '<@'+bot.user.id+'>' in msg.content:
					mention_messages = pingbot.config_load(False, 'mention_messages') #Always get currently set mention messages.
					await bot.send_message(msg.channel, random.choice(mention_messages))
			else:
				if msg.content == '<@'+bot.user.id+'>':
					mention_messages = pingbot.config_load(False, 'mention_messages') #Always get currently set mention messages.
					await bot.send_message(msg.channel, random.choice(mention_messages))

		if msg.author != bot.user:
			if '(╯°□°）╯︵ ┻━┻' in msg.content:
				await bot.send_message(msg.channel, '┬─┬﻿ ノ( ゜-゜ノ)')

		if msg.author != bot.user:
			if '┬─┬﻿ ノ( ゜-゜ノ)' in msg.content:
				await bot.send_message(msg.channel, '(╯°□°）╯︵ ┻━┻')

		if enable_custom_commands == True:
			if msg.content.startswith(cmd_prefix):
				command = pingbot.custom_command(msg.content)
				if command != None:
					await bot.send_message(msg.channel, command)

		#message the user if the user mentioned is offline
		if enable_offline_messenger == True:
			if len(msg.mentions) > 0:
				for user in msg.mentions:
					if user.status == user.status.offline:
						server = msg.server
						channel = msg.channel
						await bot.send_message(msg.channel, "`{}` is currently offline!\nYour message has been sent via PM.".format(user.name))
						await bot.send_message(user, "`{}` mentioned you while you were away in the server: {} (#{}).\n\n{}".format(msg.author.name, server, channel, msg.content))

		if msg.author.id in shh_list:
			try:
				await bot.delete_message(msg)
			except discord.errors.Forbidden:
				await bot.send_message(msg.channel, "PingBot is unable to delete messages.")

		await bot.process_commands(msg)

	@bot.event
	async def on_member_join(member):
		if enable_welcome_msg == True:
			if member.server.id not in no_welcome:
				server_id = member.server.id
				server = member.server
				try:
					with open('./core/docs/welcome' + server_id + '.txt', 'r') as welcome_file:
						welcome = welcome_file.read()
				except FileNotFoundError:
					with open('./core/docs/welcome/0.txt','r') as welcome_file:
						welcome = welcome_file.read()
				await bot.send_typing(server)
				await bot.send_message(server, welcome.format(member))

	@bot.event
	async def on_message_delete(msg):
		if enable_delete_msg == True:
			if msg.author != bot.user:
				if msg.server.id not in no_delete: #if the server is not equal to any of the servers above, then enable the on_message_delete feature.
					await bot.send_message(msg.channel, "`{0.author.name}` deleted the message:\n`{0.content}`".format(msg))

	#-----------------------------

	#random game loop
	async def random_game():
		await bot.wait_until_ready()
		while not bot.is_closed:
			games = pingbot.config_load(False, 'games')
			await bot.change_status(discord.Game(name="{}".format(random.choice(games)),idle=None))
			await asyncio.sleep(100)

	loop = asyncio.get_event_loop()
	try:
		if enable_random_games == True:
			loop.create_task(random_game())
		try:
			if bot_token == None:
				loop.run_until_complete(bot.login(email, password))
				loop.run_until_complete(bot.connect())
			else:
				loop.run_until_complete(bot.run(bot_token))
		except discord.errors.LoginFailure:
			print(colors.cred+"ERROR! Failed to login!")
			print("The information you set in bot.info is wrong."+colors.cwhite)
			e.subtle_error('BadLogin', 'Bad login information given.')
		finally:
			loop.run_until_complete(bot.close())
			loop.close()
	except Exception:
		print(colors.cred+"An exception occurred."+colors.cwhite)
		pingbot.subtle_error('Exception', 'Unexpected exception!')
		loop.run_until_complete(bot.close())
	except ConnectionResetError as e:
		print(colors.cred+"Connection reset."+colors.cwhite)
		e.return_error(3, 'UnexpectedClose', 'Unexpectedly closed connection.')
	finally:
		loop.run_until_complete(bot.close())
		loop.close()