import discord
from discord.ext import commands
import json
import urllib.parse
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import wikipedia

class Commands():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, text1 : str, text2 : str, *, text3 : str): #!google command that utilizes the search module.
        await self.bot.type()
        await self.bot.say("{} {} {}".format(text1, text2, text3))

    @commands.command()
    async def calc(self, *, value):
        try:
            result = eval(value)
            await self.bot.type()
            await self.bot.say(result)
        except SyntaxError:
            await self.bot.type()
            await self.bot.say("SyntaxError occurred.")
        except ZeroDivisionError:
            await self.bot.type()
            await self.bot.say("Haha, you're funny.")

    @commands.command()
    async def pingbottest(self):
        await self.bot.type()
        await self.bot.say("Test")

    @commands.command()
    async def join_date(self, member : discord.Member):
        await self.bot.say("User `{}` joined on `{}`!".format(member.name, member.joined_at))

    @commands.command()
    async def userinfo(self, member : discord.Member):
        await self.bot.say("```Showing information about {} -\r\nName: {}\r\nID: {}\r\nDiscriminator: {}\r\nStatus: {}\r\nJoined: {}\r\nCurrently Playing: {}\r\nAFK: {}\r\nMuted: {}\r\nDeafened: {}\r\nVoice Muted: {}\r\nSound Muted: {}\r\nAvatar: {}```\r\n{}".format(member.name, member.name, member.id, member.discriminator, member.status, member.joined_at, member.game, member.is_afk, member.mute, member.deaf, member.self_mute, member.self_deaf, member.avatar, member.avatar_url))

    @commands.command(pass_context=True)
    async def serverinfo(self, ctx):
        server = ctx.message.author.server
        await self.bot.say("```Showing information about {}\r\nName: {}\r\nID: {}\r\nRegion: {}\r\nOwner: {}\r\nIcon: {}```\r\n{}".format(server.name, server.name, server.id, server.region, server.owner, server.icon, server.icon_url))

    @commands.command(pass_context=True)
    async def kick(self, ctx, member : discord.Member):
        try:
            if ctx.message.channel.is_private:
                await self.bot.say("You cannot use this command in a PM!")
            else:
                if ctx.message.author.id == ctx.message.server.owner.id:
                    await self.bot.kick(member)
                    await self.bot.say("Successfully kicked user.")
                else:
                    await self.bot.say("Only the owner can kick users.")
        except discord.errors.Forbidden:
            await self.bot.say("Failed to kick user!\r\nThe bot does not have the appropriate permission to kick users!")

    @commands.command(help_attrs="Prefix test")
    async def command_prefix_test(self):
        await self.bot.say("Prefix is: {}\r\nHelp: {}" .format(self.bot.command_prefix, self.bot.help_attrs))

def setup(bot):
    bot.add_cog(Commands(bot))