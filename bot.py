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
email = pingbot.config_load(False, 'email')
password = pingbot.config_load(False, 'password')
cmd_prefix = pingbot.config_load(False, 'prefix')
pm_help = pingbot.config_load(False, 'pm_help')
bot_description = pingbot.config_load(False, 'description')
enable_delete_msg = pingbot.config_load(False, 'enable_delete_msg')
enable_welcome_msg = pingbot.config_load(False, 'enable_welcome_msg')
enable_offline_messenger = pingbot.config_load(False, 'enable_offline_messenger')
enable_random_names = pingbot.config_load(False, 'enable_random_names')
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
no_delete = pingbot.config_load(False, 'no_delete')
no_say = pingbot.config_load(False, 'no_say')
no_welcome = pingbot.config_load(False, 'no_welcome')
enable_mention_message = pingbot.config_load(False, 'enable_mention_message')
mm_ifin = pingbot.config_load(False, 'mm_ifin')
mention_messages = pingbot.config_load(False, 'mention_messages')
#ignore_offline_users = pingbot.config_load_direct('./user/ignored_offline_users.json', 'ignore_offline_users')

bot_version = pingbot.config_load(True, 'sys_version')

bot = commands.Bot(command_prefix=cmd_prefix, description=bot_description, pm_help=pm_help)

last_loaded = [] #last loaded cog(s)
sys_cogs = ["admintools", "commands", "custom_commands", "get_cmd", "search_cmd"]

os.system("title PingBot2 (Loading...)")

#-----------------------------

#Logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#-----------------------------
#Extension load commands
@bot.command(pass_context=True, hidden=True)
async def load(ctx, extension_name : str):
	"""Loads an extension."""
	if pingbot.is_bot_admin(ctx) == True:
		try:
			if extension_name not in sys.modules:
				bot.load_extension(extension_name)
				last_loaded.append(extension_name)
			else:
				await bot.say("The cog, `{}` has already been loaded!\nUse !reload to reload the cogs.".format(extension_name))
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
		await bot.say("Successfully loaded `{}`.".format(extension_name))
	else:
		await bot.say(no_perm_msg)

@bot.command(pass_context=True, hidden=True)
async def unload(ctx, extension_name : str):
	"""Unloads an extension."""
	if pingbot.is_bot_admin(ctx) == True:
		if extension_name in sys.modules:
			if extension_name in last_loaded:
				last_loaded.remove(extension_name)
			bot.unload_extension(extension_name)
			await bot.say("Successfully unloaded `{}`.".format(extension_name))
		else:
			await bot.say("`{}` is not loaded!".format(extension_name))
	else:
		await bot.say(no_perm_msg)

@bot.command(pass_context=True, hidden=True)
async def reload(ctx):
	"""Reloads all loaded extensions"""
	if pingbot.is_bot_admin(ctx) == True:
		try:
			pingbot.reset(bot, ctx, user_cogs_dir, startup_cogs, last_loaded, sys_cogs_dir, sys_cogs)
			await bot.say("Successfully reloaded cogs.")
		except Exception as e:
			await bot.say("Something went wrong!\n```{}: {} ({})```".format(type(e), e, e.args))
			print(colors.cred+str(e)+colors.cwhite)

@bot.command(pass_context=True, hidden=True)
async def show_cogs(ctx):
	"""Shows a list of loaded cogs."""
	if pingbot.is_bot_admin(ctx) == True:
		await bot.say("Startup cogs (`{}`):\n`{}`".format(len(startup_cogs), '\n'.join(startup_cogs)))
		await bot.say("Recently loaded cogs (`{}`):\n`{}`".format(len(last_loaded), '\n'.join(last_loaded)))
		await bot.say("System cogs (`{}`): \n`{}`".format(len(sys_cogs), '\n'.join(sys_cogs)))

@bot.command(pass_context=True, hidden=True)
async def announce(ctx, *, string : str):
	"""Sends this message to all servers the bot is currently connected to."""
	if pingbot.is_bot_admin(ctx) == True:
		if any(word in string for word in banned_say_words):
			await bot.say(annoyed)
		else:
			for i in bot.servers:
				await bot.send_message(i, string) #bot.say(string)
	else:
		await bot.say(no_perm_msg)

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
	if pingbot.is_bot_admin(ctx) == True:
		servers = len(bot.servers)
		await bot.say("Currently connected to `%s` server(s)." % servers)
		if len(bot.servers) < 20:
			for i in bot.servers:
				await bot.send_message(ctx.message.author, "`{}` : `{}`".format(i.name, i.id))
	else:
		await bot.say(no_perm_msg)

@bot.command(hidden=True)
async def version():
	"""
	Returns the version of PingBot, as well as the latest update version.
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
	Joins a channel.
	"""
	try:
		await bot.say(success)
		await bot.accept_invite(url)
	except discord.errors.NotFound:
		await bot.say(invalid_invite)

@bot.command(pass_context=True)
async def leave(ctx):
	"""
	Leaves a channel.
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
	current_time = datetime.datetime.now().strftime('%H:%M:%S')
	try:
		print("[{}][{}][{}][{}]: {}".format(current_time, msg.server, msg.channel, msg.author, msg.content))
	except UnicodeEncodeError:
		print("[{}][{}][{}][{}] [Contains Character]".format(current_time, msg.server, msg.channel, msg.author))

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

	await bot.process_commands(msg)

#welcome message
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
			await bot.send_message(server, "Welcome {} to {}!\n{}".format(member.mention, server.name, welcome))

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

#random messages loop (Disabled for now.)
loop = asyncio.get_event_loop()

try:
	loop.create_task(random_game())
	if enable_random_names == True:
		loop.create_task(random_name())
	try:
		loop.run_until_complete(bot.login(email, password))
		loop.run_until_complete(bot.connect())
	except discord.errors.LoginFailure:
		print(colors.cred+"ERROR! Failed to login!")
		print("The information you set in bot.info is wrong."+colors.cwhite)
		e.subtle_error('BadLogin', 'Bad login information given.')
	finally:
		loop.run_until_complete(bot.close())
		loop.close()
except Exception:
	pingbot.subtle_error('Exception', 'Unexpected exception!')
	loop.run_until_complete(bot.close())
except ConnectionResetError as e:
	e.return_error(3, 'UnexpectedClose', 'Unexpectedly closed connection.')
finally:
	loop.run_until_complete(bot.close())
	loop.close()