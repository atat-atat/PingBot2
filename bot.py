from discord.ext import commands
import discord
from core.colors import colors
import os
import logging
from PIL import Image, ImageFont, ImageDraw

with(open("bot.info")) as botConfF:
	botConfig = botConfF.read().split(":")

bot = discord.Client()
description = '''A discord bot built using Python (discord.py)'''
bot = commands.Bot(command_prefix='!', description=description)

command_sets = ["core.commands.search_cmd","core.commands.memes", "core.commands.commands"] #command sets to load
last_loaded = []

with open('admins.info', 'r') as admins_file:
	admins = admins_file.read().split(',')

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
@bot.command(pass_context=True)
async def load(ctx, extension_name : str):
	if is_dev(ctx) == True:
		"""Loads an extension."""
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

@bot.command(pass_context=True)
async def unload(ctx, extension_name : str):
	if is_dev(ctx) == True:
	    """Unloads an extension."""
	    if extension_name in last_loaded:
	    	last_loaded.remove(extension_name)
	    bot.unload_extension(extension_name)
	    await bot.say("Successfully unloaded `{}`.".format(extension_name))
	else:
		await bot.say("You don't have permission to use that command!")

@bot.command(pass_context=True)
async def reload(ctx):
	if is_dev(ctx) == True:
		reset(ctx)
		if reset(ctx) == True:
			await bot.say("Successfully reloaded!")
		else:
			await bot.say("Failed to reload!")

@bot.command(pass_context=True)
async def show_cogs(ctx):
	if is_dev(ctx) == True:
		await bot.say("Default command sets:")
		for i in command_sets:
			await bot.say(i)
		await bot.say("Recently loaded sets:")
		for i in last_loaded:
			await bot.say(i)

#owner check test
@bot.command(pass_context = True)
async def check_owner(ctx):
	if is_owner(ctx) == True:
		await bot.say("You are the owner!")
	elif is_owner(ctx) == False:
		await bot.say("You are not the owner!")
	elif is_owner(ctx) == "PRIV":
		await bot.say("This is a private channel!")

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

	print(" ")

@bot.event
async def on_message(msg):
	if msg.channel.is_private and msg.content.startswith('http') and msg.author != bot.user:
		invite = await bot.get_invite(msg.content)
		await bot.accept_invite(invite)
		await bot.send_message(msg.author, "Joining server.")

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

bot.run(botConfig[0], botConfig[1])