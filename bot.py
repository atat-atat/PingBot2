from discord.ext import commands
import discord
from core.colors import colors
import os
import wikipedia

with(open("bot.info")) as botConfF:
	botConfig = botConfF.read().split(":")

bot = discord.Client()
description = '''A discord bot built using Python (discord.py)'''
bot = commands.Bot(command_prefix='?', description=description)

command_sets = ["core.commands.search_cmd","core.commands.memes"] #command sets to load
last_loaded = []
admins = [] #who can use the SPECIAL commands

title = "PingBot" #Command prompt window caption
os.system("title "+title)

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

	if msg.content.startswith("!leave"):
		if msg.author.id == msg.server.owner.id or msg.author.id in admins:
			await bot.leave_server(msg.server)

	await bot.process_commands(msg)
	print("[{}][{}][{}]: {}".format(msg.server, msg.channel, msg.author, msg.content))

#-----------------------------
#Other bot functions

#returns a boolean depending on if the message author is a developer
def is_dev(ctx):
	if ctx.message.author.id in admins:
		return True
	else:
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