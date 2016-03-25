import discord
from discord.ext import commands
from core.pingbot import PingbotCore

pingbot = PingbotCore()

class AdminTools():
	def __init__(self, bot):
		self.bot = bot
		self.no_kick_perm = pingbot.config_load_msg('no_kick_perm')
		self.kick_forbidden = pingbot.config_load_msg('kick_forbidden')
		self.kick_success = pingbot.config_load_msg('kick_success')
		self.no_ban_perm = pingbot.config_load_msg('no_ban_perm')
		self.ban_forbidden = pingbot.config_load_msg('ban_forbidden')
		self.ban_success = pingbot.config_load_msg('ban_success')
		self.no_command_pm = pingbot.config_load_msg('no_command_pm')

	@commands.command(pass_context=True)
	async def kick(self, ctx, member : discord.Member):
		"""
		Kicks a user. (You must be the server owner to use this command.)
		"""
		try:
			if ctx.message.channel.is_private:
				await self.bot.say(self.no_command_pm)
			else:
				if pingbot.is_owner(ctx) == True:
					await self.bot.kick(member)
					await self.bot.say(self.kick_success)
				else:
					await self.bot.say(self.no_kick_perm)
		except discord.errors.Forbidden:
			await self.bot.say(self.kick_forbidden)

	@commands.command(pass_context=True)
	async def ban(self, ctx, member : discord.Member):
		"""
		Bans a user. (You must be the server owner to use this command.)
		"""
		try:
			if ctx.message.channel.is_private:
				await self.bot.say(self.no_command_pm)
			else:
				if pingbot.is_owner(ctx) == True:
					await self.bot.ban(member, 0)
					await self.bot.say(self.ban_success)
				else:
					await self.bot.say(self.no_ban_perm)
		except discord.errors.Forbidden:
			await self.bot.say(self.ban_forbidden)

def setup(bot):
	bot.add_cog(AdminTools(bot))