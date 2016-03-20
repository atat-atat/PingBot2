import discord
from discord.ext import commands
import wikipedia
import cleverbot
from core.pingbot import PingbotCore

cb1 = cleverbot.Cleverbot()
pingbot = PingbotCore()

class Commands():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def google(self, *, search_string : str):
        """Searches Google."""
        await self.bot.say(pingbot.search_standard('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&', search_string))

    @commands.command()
    async def youtube(self, *, search_string : str):
        """Searches YouTube. (MAY BE DEPRECATED)"""
        await self.bot.say(pingbot.search_youtube(search_string))

    @commands.command()
    async def urban(self, *, search_string : str):
        """Searches Urban Dictionary."""
        try:
            pingbot.search_div_set_link('http://www.urbandictionary.com/define.php?term=', search_string)
            await self.bot.say("Showing definition of `{}` from Urban Dictionary.".format(search_string))
            meaning = pingbot.search_div_get('meaning')
            example = pingbot.search_div_get('example')
            contributor = pingbot.search_div_get('contributor')
            await self.bot.say("{}\r\n\r\n**Example -**\r\n{}\r\nContributor-\r\n{}".format(meaning, example, contributor))
        except AttributeError:
            await self.bot.say("Could not find a definition for that word.")
        except discord.errors.HTTPException:
            await self.bot.say("The definition was too long...")

    @commands.command()
    async def wiki(self, *, search_string : str):
        """Searches Wikipedia."""
        try:
            result = wikipedia.summary(search_string, sentences = 5)
            await self.bot.say(result)
        except wikipedia.exceptions.DisambiguationError:
            await self.bot.say("That page does not exist!")

    @commands.command()
    async def clever(self, *, input_string : str):
        """Talks to cleverbot."""
        try:
            await self.bot.say(">>> {}".format(input_string))
            response = cb1.ask(input_string)
            await self.bot.type()
            await self.bot.say(response)
        except cleverbot.cleverbot.CleverbotAPIError:
            await self.bot.say("Error, something went wrong.")

def setup(bot):
    bot.add_cog(Commands(bot))