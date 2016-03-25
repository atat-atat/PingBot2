import discord
from discord.ext import commands
import os
import random

class ASCIIART():
	def __init__(self, bot):
		self.bot = bot
		self.sub_dir = "./core/docs/ascii"

	@commands.command()
	async def boo(self):
		with open(os.path.join(self.sub_dir,'ghost1.txt'), 'r') as ghost_file:
			ghost1 = ghost_file.read()
		with open(os.path.join(self.sub_dir, 'ghost2.txt'), 'r') as ghost_file:
			ghost2 = ghost_file.read()
		with open(os.path.join(self.sub_dir, 'ghost3.txt'), 'r') as ghost_file:
			ghost3 = ghost_file.read()

		ghosts = [ghost1, ghost2, ghost3]

		await self.bot.say("```{}```".format(random.choice(ghosts)))

def setup(bot):
	bot.add_cog(ASCIIART(bot))