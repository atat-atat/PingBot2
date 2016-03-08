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
    async def google(self, search_string : str): #!google command that utilizes the search module.
        h=""
        query = urllib.parse.urlencode({'q': search_string})
        url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
        search_response = urllib.request.urlopen(url)
        search_results = search_response.read().decode("utf8")
        results = json.loads(search_results)
        data = results['responseData']
        #print('Total results: %s' % data['cursor']['estimatedResultCount'])
        hits = data['results']
        #print('Top %d hits:' % len(hits))
                #len(hits) = 1
        for h in hits:
            h = h['url']
        await self.bot.say(h)
        #await self.bot.say(search.h)

    @commands.command()
    async def image(self, search_string : str): #!google command that utilizes the search module.
        h=""
        query = urllib.parse.urlencode({'q': search_string})
        url = 'https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=%s' % query
        search_response = urllib.request.urlopen(url)
        search_results = search_response.read().decode("utf8")
        results = json.loads(search_results)
        data = results['responseData']
        #print('Total results: %s' % data['cursor']['estimatedResultCount'])
        hits = data['results']
        #print('Top %d hits:' % len(hits))
                #len(hits) = 1
        for h in hits:
            h = h['url']
        await self.bot.say(h)
        #await self.bot.say(search.h)

    @commands.command()
    async def youtube(self, search_string : str):
        h=""
        query = urllib.parse.urlencode({'q': search_string})
        url = 'https://ajax.googleapis.com/ajax/services/search/video?v=1.0&%s' % query
        search_response = urllib.request.urlopen(url)
        search_results = search_response.read().decode("utf8")
        results = json.loads(search_results)
        data = results['responseData']
        #print('Total results: %s' % data['cursor']['estimatedResultCount'])
        hits = data['results']
        #print('Top %d hits:' % len(hits))
                #len(hits) = 1
        for h in hits:
            h = h['url']
        await self.bot.say(h)

    @commands.command()
    async def urban(self, search_string : str):
        try:
            await self.bot.say("Showing definition of {} from Urban Dictionary.".format(search_string))
            r = requests.get("http://www.urbandictionary.com/define.php?term={}".format(search_string))
            soup = BeautifulSoup(r.content)
            meaning = soup.find("div",attrs={"class":"meaning"}).text
            example = soup.find("div",attrs={"class":"example"}).text
            contributor = soup.find("div",attrs={"class":"contributor"}).text
            await self.bot.say("{}\r\n\r\n**Example -**\r\n{}\r\nContributor-\r\n{}".format(meaning, example, contributor))
        except AttributeError:
            await self.bot.say("Could not find a definition for that word.")


    @commands.command()
    async def define(self, search_string : str):
        try:
            await self.bot.say("Showing definition of {} from Dictionary.com".format(search_string))
            r = requests.get("http://dictionary.reference.com/browse/{}?s=t".format(search_string))
            soup = BeautifulSoup(r.content)
            meaning = soup.find("div",attrs={"class":"def-content"}).text
            #example = soup.find("div",attrs={"class":"example"}).text
            #contributor = soup.find("div",attrs={"class":"contributor"}).text
            await self.bot.say("{}".format(meaning))
        except AttributeError:
            await self.bot.say("Could not find a definition for that word.")


def setup(bot):
    bot.add_cog(Commands(bot))