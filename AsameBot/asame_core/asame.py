from pingbot import PingbotCore
from asamebot import commands
import discord
import asyncio

pingbot = PingbotCore()
bot = discord.Client()

commands = commands()
asame_cmds = commands.command_list

#Config loading
bot_name = pingbot.config_load(False, 'bot_name')
email = pingbot.config_load(False, 'email')
password = pingbot.config_load(False, 'password')
cmd_prefix = pingbot.config_load(False, 'prefix')
bot_admins = pingbot.config_load(False, 'admins')

@bot.async_event
def on_ready():
	with open('./asame_core/images/icon.png', 'rb') as avatar_file:
		avatar = avatar_file.read()
	yield from bot.edit_profile(password=password, username=bot_name, avatar=avatar)
	print("AsameBot ready!")

@bot.async_event
def on_message(self, msg):
	print("[{}][{}][{}]: {}".format(msg.server.name, msg.channel, msg.author, msg.content))
	if msg.content.startswith('Asame') or msg.content.startswith('asame'):
		cmd = msg.content.split(" ")
		if "join" in cmd:
			invite_link = msg.content.split("join ",1)[1]
			yield from bot.send_message(msg.channel, invite_link)
			try:
				yield from bot.accept_invite(invite_link)
				yield from bot.send_message(msg.channel, "I have successfully joined the invite url.")
			except Exception as e:
				yield from bot.send_message(msg.channel, "I was unable to join that invite url.")
			if "leave" in cmd:
				yield from bot.send_message(msg.channel, "*Good bye.*")
				yield from bot.leave_server(msg.server)

		if msg.channel.is_private:
			if any(word in cmd for word in asame_cmds):
				if "show" and "error" in cmd:
					if self.latest_error != None:
						yield from bot.send_message(msg.channel, "**Unexpected error has occurred!**\n[Error Occurrence]: `{}` (`{}`) : `{}`, caused by command-author: `{}` (`{}`)\n[Message]: {}\n\n[Error]:\n```{}```".format(msg.server, msg.server.id, msg.channel, msg.author, msg.author.id, msg.content, e))
					else:
						yield from bot.send_message(msg.channel, "There have been no errors.")
			else:
				yield from bot.send_message("Unknown command!")

	if msg.content.startswith(cmd_prefix + 'join'):
		invite_link = msg.content[len("join "):].strip()
		yield from bot.send_message(msg.channel, invite_link)
		yield from bot.accept_invite(invite_link)

	if msg.content.startswith(cmd_prefix + 'leave'):
		yield from bot.leave_server(msg.server)

loop = asyncio.get_event_loop()


try:
	loop.run_until_complete(bot.login(email, password))
	loop.run_until_complete(bot.connect())
except Exception:
	loop.run_until_complete(bot.close())
finally:
	loop.close()