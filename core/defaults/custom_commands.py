from discord.ext import commands
from core.pingbot import PingbotCore

pingbot = PingbotCore()

class CustomComm():
	def __init__(self, bot):
		self.bot = bot
		self.enable_custom_commands = pingbot.config_load(False, 'enable_custom_commands')

	@commands.command()
	async def command_add(self, command : str=None, *, value : str=None):
		if self.enable_custom_commands == True:
			if command != None and value != None:
				pingbot.add_command(command, value)
				await self.bot.say("Successfully added command!")
			elif command == None:
				await self.bot.say("You must provide the command name.")
			elif value == None:
				await self.bot.say("You must provide the value.")

def setup(bot):
	bot.add_cog(CustomComm(bot))