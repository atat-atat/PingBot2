from discord.ext import commands
import discord
from core.colors import colors
import os
import logging
from PIL import Image, ImageFont, ImageDraw
import asyncio
import random



bot = discord.Client()
description = '''A discord bot built using Python (discord.py)'''
bot = commands.Bot(command_prefix='!', description=description, pm_help=True)

last_loaded = [] #last loaded cog
info_dir = "./core/config"

with open(os.path.join(info_dir, 'admins.info'), 'r') as admins_file:
	admins = admins_file.read().split(',')

with open(os.path.join(info_dir, 'no_delete.info'), 'r') as nd_file:
	no_delete = nd_file.read().split(',')

with open(os.path.join(info_dir, 'command_sets.info'), 'r') as cs_file:
	command_sets = cs_file.read().split(',')

with open(os.path.join(info_dir, "bot.info"), 'r') as botConfF:
	botConfig = botConfF.read().split(":")

with open(os.path.join(info_dir, "no_welcome.info"), 'r') as nw_file:
	no_welcome = nw_file.read().split(":")

title = "PingBot2" #Command prompt window caption
os.system("title "+title)

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
	if is_dev(ctx) == True:
		try:
			bot.load_extension(extension_name)
			last_loaded.append(extension_name)
		except (AttributeError, ImportError) as e:
			await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
			print(colors.cred+e+colors.cwhite)
			return
		await bot.say("Successfully loaded `{}`.".format(extension_name))
	else:
		await bot.say("You do not have permission to use this command!")

@bot.command(pass_context=True, hidden=True)
async def unload(ctx, extension_name : str):
	"""Unloads an extension."""
	if is_dev(ctx) == True:
	    if extension_name in last_loaded:
	    	last_loaded.remove(extension_name)
	    bot.unload_extension(extension_name)
	    await bot.say("Successfully unloaded `{}`.".format(extension_name))
	else:
		await bot.say("You don't have permission to use that command!")

@bot.command(pass_context=True, hidden=True)
async def reload(ctx):
	"""Reloads all loaded extensions"""
	if is_dev(ctx) == True:
		reset(ctx)
		if reset(ctx) == True:
			await bot.say("Successfully reloaded!")
		else:
			await bot.say("Failed to reload!")

@bot.command(pass_context=True, hidden=True)
async def show_cogs(ctx):
	"""Shows a list of loaded cogs."""
	if is_dev(ctx) == True:
		await bot.say("Default command sets:")
		for i in command_sets:
			await bot.say(i)
		await bot.say("Recently loaded sets:")
		for i in last_loaded:
			await bot.say(i)

#-----------------------------
#Bot events

#@bot.command()
#async def command_name():
	#await bot.say("Test.")

#display information when the bot is ready.
@bot.event
async def on_ready():
	print(colors.cgreen+"User: %s" % bot.user.name)
	print("ID: %s" % bot.user.id+colors.cwhite)
	servers = len(bot.servers) #get amount of servers connected to
	print("Servers ({}):".format(servers))
	for server in bot.servers: #show a list of servers that the bot is currently connected to
		print("	{} : {}".format(server.name,server.id))
	for extension_name in command_sets: #load default extensions
		bot.load_extension(extension_name)

	sub_dir = "./core/docs/list"
	with open(os.path.join(sub_dir, "games.list"), 'r') as games_file:
			games = games_file.read().split(',')
	await bot.change_status(discord.Game(name="{}".format(random.choice(games)),idle=None))

	print(" ")

@bot.event
async def on_message(msg):
	if msg.content.startswith("!join"):
		invite = msg.content[len("!join "):].strip()
		await bot.accept_invite(invite)

	#leave the server
	if msg.content.startswith("!leave"):
		if msg.author.id == msg.server.owner.id or msg.author.id in admins:
			await bot.leave_server(msg.server)

	#rip message
	if msg.content.startswith("!rip"):
			try:
				name = msg.content[len("!rip "):].strip()
				img = Image.open("./core/images/rip.jpg")
				draw = ImageDraw.Draw(img)
					# font = ImageFont.truetype(<font-file>, <font-size>)
				font = ImageFont.truetype("comic.ttf", 28)
					# draw.text((x, y),"Sample Text",(r,g,b))
				draw.text((58, 149),"{} :(".format(name),(0,0,0),font=font)
				img.save('./core/images/rip-radioedit.jpg')
				await bot.send_file(msg.channel, "./core/images/rip-radioedit.jpg")
			except IndexError:
				await bot.send_typing(msg.channel)
				await bot.send_message(msg.channel, "http://i.imgur.com/Ij5lWrM.png")

	#message the user if the user mentioned is offline
	if len(msg.mentions) > 0:
		for user in msg.mentions:
			if user.status == user.status.offline:
				server = msg.server
				channel = msg.channel
				await bot.send_typing(msg.channel)
				await bot.send_message(msg.channel, "`{}` is currently offline!\r\nYour message has been sent via PM.".format(user.name))
				await bot.send_typing(user)
				await bot.send_message(user, "`{}` mentioned you while you were away in the server: {} (#{}).\r\n\r\n{}".format(msg.author.name, server, channel, msg.content))

	#edit the welcome message of a server.
	if msg.content.startswith('!welcome_edit'):
		if msg.author.id == msg.server.owner.id or msg.author.id in admins:
			servw = msg.content[len("!welcome_edit "):].strip()
			sub_dir = "./core/docs/welcome"
			with open(os.path.join(sub_dir, msg.server.id+".txt"), 'w') as welcome_file:
				welcome_file.write(servw)
			await bot.send_message(msg.channel, "Successfully modified server welcome message!")
		else:
			await bot.send_message(msg.channel, "You do not have the permission to modify the server welcome message.")

	await bot.process_commands(msg)
	print("[{}][{}][{}]: {}".format(msg.server, msg.channel, msg.author, msg.content))

#welcome message
@bot.event
async def on_member_join(member):
	if member.server.id not in no_welcome:
		server_id = member.server.id
		server = member.server
		sub_dir = "./core/docs/welcome"
		try:
			with open(os.path.join(sub_dir, server_id+".txt"),'r') as welcome_file:
				welcome = welcome_file.read()
		except FileNotFoundError:
			with open(os.path.join(sub_dir, "0.txt"),'r') as welcome_file:
				welcome = welcome_file.read()
		#fmt = 'Welcome {0.mention} to {1.name}!\r\n{2.welcome}'
		await bot.send_typing(server)
		await bot.send_message(server, "Welcome {} to {}!\r\n{}".format(member.mention, server.name, welcome))

@bot.event
async def on_message_delete(msg):
	if msg.server.id not in no_delete: #if the server is not equal to any of the servers above, then enable the on_message_delete feature.
		await bot.send_message(msg.channel, "`{0.author.name}` deleted the message:\r\n`{0.content}`".format(msg))

#-----------------------------
#Other bot functions

#returns a boolean depending on if the message author is a developer
def is_dev(ctx):
	if ctx.message.author.id in admins:
		return True
	else:
		print(colors.cred+"USER ATTEMPTED UNAUTHORIZED DEV COMMAND!"+colors.cwhite)
		return False

#returns a boolean depending on if the message author is an owner
def is_owner(ctx):
	if ctx.message.channel.is_private:
		return "PRIV"
	else:
		if ctx.message.author.id == ctx.message.server.owner.id:
			return True
		else:
			return False

#reloads the extensions.
def reset(ctx):
	if is_dev(ctx) == True:
		for i in command_sets:
			bot.unload_extension(i)
			bot.load_extension(i)
		for i in last_loaded:
			bot.unload_extension(i)
			bot.load_extension(i)
		return True
	else:
		return False

#random game loop
async def random_game():
	await bot.wait_until_ready()
	while not bot.is_closed:
		sub_dir = "./core/docs/list"
		with open(os.path.join(sub_dir, "games.list"), 'r') as games_file:
			games = games_file.read().split(',')
		await bot.change_status(discord.Game(name="{}".format(random.choice(games)),idle=None))
		await asyncio.sleep(100)

#random messages loop (Disabled for now.)
loop = asyncio.get_event_loop()

try:
    loop.create_task(random_game())
    #loop.create_task(command_input())
    loop.run_until_complete(bot.login(botConfig[0], botConfig[1]))
    loop.run_until_complete(bot.connect())
except Exception:
    loop.run_until_complete(bot.close())
finally:
   loop.close()