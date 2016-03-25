import discord
from discord.ext import commands
from datetime import datetime
from pytz import timezone
import urllib
from urllib.request import urlopen
import json
import  requests
from bs4 import BeautifulSoup
from core.osu import osu
from core.wunderground import WundergroundAPI

o = osu()
w = WundergroundAPI()

class PingBotCmds():
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def convert_timezone(self, timezone1 : str, timezone2 : str):
		try:
			fmt = "%Y-%m-%d %H:%M:%S %Z%z"
			timezonelist = [timezone1, timezone2]
			for zone in timezonelist:
				now_time = datetime.now(timezone(zone))
				await self.bot.say("`{}`".format(now_time.strftime(fmt)))
		except pytz.exceptions.UnknownTimeZoneError:
			await self.bot.say("Error! That timezone doesn't exist!")

	@commands.command(pass_context=True)
	async def user_find(self, ctx, user : str):
		member = discord.utils.get(ctx.message.server.members, name=user)
		await self.bot.say(member)

	@commands.command(pass_context=True)
	async def list_users(self, ctx):
		await self.bot.say(ctx.message.channel.server.members)

	async def message_man(self, msg):
		if "@@@" in msg.content:
			split_msg = msg.content.split(' ')
			if "@@@" in split_msg:
				await self.bot.send_message(msg.channel, "<@102964575992832000>")

def setup(bot):
	bot.add_listener(PingBotCmds(bot).message_man, 'on_message')
	bot.add_cog(PingBotCmds(bot))