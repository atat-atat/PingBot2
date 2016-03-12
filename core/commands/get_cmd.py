import discord
from discord.ext import commands
import configparser

class GetInfo():
	def __init__(self, bot):
		self.bot = bot
		info_dir = "./core/config"
		config = configparser.ConfigParser()
		config.read('./core/config/bot.info')
		self.email = config.get('config', 'email', fallback="Email")
		self.password = config.get('config', 'password', fallback="Password")
		self.allow_bot_changes = config.get('config', 'allow_bot_changes', fallback=True)
		self.enable_clear = config.get('config', 'enable_clear_cmd', fallback=False)
		self.original_name = config.get('config', 'original_name', fallback="PingBot")
		self.no_perm_msg = config.get('messages', 'no_permission', fallback="You do not have the permission to use this command.")
		self.only_owner = config.get('messages', 'only_owner', fallback="You must be the owner of this server to use this command.")
		self.annoyed = config.get('messages', 'nuisance_msg', fallback="Nice try.")
		self.divide_zero = config.get('messages', 'divide_zero', fallback="Haha, you're funny.")
		self.no_kick_perm = config.get('messages', 'no_kick_perm', fallback="Only the owner can kick users.")
		self.kick_forbidden_perm = config.get('messages', 'kick_forbidden', fallback="Failed to kick user.\r\nThe bot does not have the appropriate permission to kick users.")
		self.kick_success = config.get('messages', 'kick_success', fallback="Successfully kicked user.")
		self.no_command_pm = config.get('messages', 'no_command_pm', fallback="You cannot use this command in a PM.")
		self.no_user_msg = config.get('messages', 'failed_to_find_user', fallback="Failed to find that user.")


	@commands.command()
	async def join_date(self, member : discord.Member):
		"""
		Returns the join date of a user.
		"""
		await self.bot.say("User `{}` joined on `{}`!".format(member.name, member.joined_at))

	@commands.command()
	async def game(self, member : discord.Member):
		"""
		Returns the currently playing game of a user.
		"""
		await self.bot.say("`{}` is currently playing `{}`".format(member.name, member.game))

	@commands.command()
	async def userid(self, member : discord.Member):
		"""
		Returns the ID of a user.
		"""
		await self.bot.say("The ID of `{}` is `{}`".format(member.name, member.id))

	@commands.command()
	async def chanid(self, channel : discord.Channel):
		"""
		Returns the ID of a channel.
		"""
		await self.bot.say("The ID of `{}` is `{}`".format(channel.name, channel.id))

	@commands.command()
	async def serverid(self, server : discord.Server):
		"""
		Returns the ID of a server.
		"""
		await self.bot.say("The ID of `{}` is `{}`".format(server.name, server.id))
		

	@commands.command()
	async def userinfo(self, member : discord.Member):
		"""
		Shows information about a user.
		"""
		await self.bot.say("```Showing information about {} -\r\nName: {}\r\nID: {}\r\nDiscriminator: {}\r\nStatus: {}\r\nJoined: {}\r\nCurrently Playing: {}\r\nAFK: {}\r\nMuted: {}\r\nDeafened: {}\r\nVoice Muted: {}\r\nSound Muted: {}\r\nAvatar: {}```\r\n{}".format(member.name, member.name, member.id, member.discriminator, member.status, member.joined_at, member.game, member.is_afk, member.mute, member.deaf, member.self_mute, member.self_deaf, member.avatar, member.avatar_url))



	@commands.command(pass_context=True)
	async def serverinfo(self, ctx):
		"""
		Returns the information of the server.
		"""
		server = ctx.message.author.server
		await self.bot.say("```Showing information about {}\r\nName: {}\r\nID: {}\r\nRegion: {}\r\nOwner: {}\r\nIcon: {}```\r\n{}".format(server.name, server.name, server.id, server.region, server.owner, server.icon, server.icon_url))

	@commands.command()
	async def avatar(self, member : discord.Member):
		"""
		Gets the avatar of a user.
		"""
		await self.bot.say("Avatar of `{}` is {}".format(member.name, member.avatar_url))

def setup(bot):
    bot.add_cog(GetInfo(bot))