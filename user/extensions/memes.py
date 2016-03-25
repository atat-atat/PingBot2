"""
A cog full of memes.

Ported from PingBot to PingBot2 by aidybee.
"""
import discord
from discord.ext import commands
import random
import os
import configparser

class memes():

    def __init__(self, bot):
        self.bot = bot
        sub_dir = "./core/docs/list"
        self.sub_dir = sub_dir
        #MULTICOMMANDS COMMANDS

    @commands.command()
    async def no(self):
        """Returns a personalized meme to fit the feeling of "No"."""
        with open(os.path.join(self.sub_dir,'no.list'), 'r') as no_file:
            no = no_file.read().split(',')
        await self.bot.say(format(random.choice(no)))

    @commands.command()
    async def nice(self):
        """Returns a personalized meme to fit the feeling of "Nice"."""
        with open(os.path.join(self.sub_dir,'nice.list'), 'r') as nice_file:
            nice = nice_file.read().split(',')
        await self.bot.say(format(random.choice(nice)))

    @commands.command()
    async def really(self):
        """Returns a personalized meme to fit the feeling of "Really?"."""
        with open(os.path.join(self.sub_dir,'really.list'), 'r') as really_file:
            really = really_file.read().split(',')
        await self.bot.say(format(random.choice(really)))

    @commands.command()
    async def yes(self):
        """Returns a personalized meme to fit the feeling of "Yes"."""
        with open(os.path.join(self.sub_dir,'yes.list'), 'r') as yes_file:
            yes = yes_file.read().split(',')
        await self.bot.say(format(random.choice(yes)))

    @commands.command()
    async def lewd(self):
        """Returns a personalized meme to fit the feeling of "Lewd"."""
        with open(os.path.join(self.sub_dir,'lewd.list'), 'r') as lewd_file:
            lewd = lewd_file.read().split(',')
        await self.bot.say(format(random.choice(lewd)))

    @commands.command()
    async def lmao(self):
        """Returns a personalized meme to fit the feeling of "Lmao"."""
        with open(os.path.join(self.sub_dir,'lmao.list'), 'r') as lmao_file:
            lmao = lmao_file.read().split(',')
        await self.bot.say(format(random.choice(lmao)))

    @commands.command()
    async def kek(self):
        """Returns a personalized meme to fit the feeling of "Kek"."""
        with open(os.path.join(self.sub_dir,'kek.list'), 'r') as kek_file:
            kek = kek_file.read().split(',')
        await self.bot.say(format(random.choice(kek)))

    @commands.command()
    async def ded(self):
        """Returns a personalized meme to fit the feeling of "ded"."""
        with open(os.path.join(self.sub_dir,'ded.list'), 'r') as ded_file:
            ded = ded_file.read().split(',')
        await self.bot.say(format(random.choice(ded)))

    @commands.command()
    async def ahegao(self):
        """Returns some lewd material."""
        with open(os.path.join(self.sub_dir,'ahegao.list'), 'r') as ahegao_file:
            ahegao = ahegao_file.read().split(',')
        await self.bot.say(format(random.choice(ahegao)))

    @commands.command()
    async def hitler(self):
        """Returns a picture of Adolf Hitler."""
        with open(os.path.join(self.sub_dir,'hitler.list'), 'r') as hitler_file:
            hitler = hitler_file.read().split(',')
        await self.bot.say(format(random.choice(hitler)))

    @commands.command()
    async def rekt(self):
        """Returns some text."""
        with open(os.path.join(self.sub_dir,'rekt.list'), 'r') as rekt_file:
            rekt = rekt_file.read().split(',')
        await self.bot.say(format(random.choice(rekt)))

    @commands.command()
    async def woop(self):
        """Woop!"""
        with open(os.path.join(self.sub_dir,'woop.list'), 'r') as woop_file:
            woop = woop_file.read().split(',')
        await self.bot.say(format(random.choice(woop)))

    @commands.command()
    async def cancer(self):
        """Returns a random image."""
        with open(os.path.join(self.sub_dir,'cancer.list'), 'r') as cancer_file:
            cancer = cancer_file.read().split(',')
        await self.bot.say(format(random.choice(cancer)))

    @commands.command()
    async def salty(self):
        """Returns some salt."""
        with open(os.path.join(self.sub_dir,'salty.list'), 'r') as salty_file:
            salty = salty_file.read().split(',')
        await self.bot.say(format(random.choice(salty)))

    @commands.command()
    async def triggered(self):
        """Returns a meme to simulate "Triggered." """
        await self.bot.say("http://i.imgur.com/l6haVfV.gif")

    @commands.command()
    async def xd(self):
        """xD"""
        await self.bot.say("http://i.imgur.com/bgdqZ6a.gif")

    @commands.command()
    async def haha(self):
        """xD"""
        await self.bot.say("http://i.imgur.com/bgdqZ6a.gif")

    @commands.command()
    async def wakeupmate(self):
        await self.bot.say("http://i.imgur.com/pOoqHjJ.gif")

    @commands.command()
    async def wakemeup(self):
        await self.bot.say("http://i.imgur.com/pOoqHjJ.gif")

    @commands.command()
    async def kappa(self):
        """Outputs the iconic Twitch meme."""
        await self.bot.say("http://i.imgur.com/giUFzXG.png")

    @commands.command()
    async def ysmart(self):
        """An iconic DJ Khaled meme."""
        await self.bot.say("http://i.imgur.com/kjrbRK2.gif")

    @commands.command()
    async def yloyal(self):
        """An iconic DJ Khaled meme."""
        await self.bot.say("http://i.imgur.com/PFIObvo.gif")
    
    @commands.command()
    async def ygrateful(self):
        """An iconic DJ Khaled meme."""
        await self.bot.say("http://i.imgur.com/Z6dsmOw.gif")

    @commands.command()
    async def anotherone(self):
        """Another (one)iconic DJ Khaled meme."""
        await self.bot.say("http://i.imgur.com/vO1sHmy.gif")

    @commands.command()
    async def wordsearch(self):
        """Returns a wordsearch."""
        await self.bot.say("http://i.imgur.com/74XtHfc.png")

    @commands.command()
    async def gineq(self):
        await self.bot.say("http://i.imgur.com/xzDAGco.jpg")

    @commands.command()
    async def gaminginequality(self):
        await self.bot.say("http://i.imgur.com/xzDAGco.jpg")

    @commands.command()
    async def hanginthere(self):
        """Hang in there."""
        await self.bot.say("http://i.imgur.com/RQrEkC9.jpg")
    
    @commands.command()
    async def porn(self):
        """Returns some porn."""
        await self.bot.say("http://pornhub.com/random")
    
    @commands.command()
    async def gayporn(self):
        """Returns some gay porn."""
        await self.bot.say("http://www.pornhub.com/gay/random")
    
    @commands.command()
    async def bruh(self):
        """A hilarious meme."""
        await self.bot.say("http://i.imgur.com/WLd5fX7.png")
    
    @commands.command()
    async def heybudd(self):
        """Returns a meme."""
        await self.bot.say("https://www.youtube.com/watch?v=eVm88MX2Gw4")
    
    @commands.command()
    async def heil(self):
        """Returns a meme."""
        await self.bot.say("http://i.imgur.com/ZvOVr3P.gif")

    @commands.command()
    async def kkk(self):
        """Returns a meme."""
        await self.bot.say("http://i.imgur.com/B6Zfqox.jpg")
    
    @commands.command()
    async def smh(self):
        """Shaking my head."""
        await self.bot.say("http://i.imgur.com/Jbe85tc.png")

    @commands.command()
    async def frick(self):
        """Frick."""
        await self.bot.say("http://i.imgur.com/SOoEOFr.png")

    @commands.command()
    async def aria(self):
        """Sigh."""
        await self.bot.say("http://i.imgur.com/PwpZIsl.gif")

    @commands.command()
    async def funfacts(self):
        """Returns a fun fact."""
        with open(os.path.join(self.sub_dir, 'funfacts.list')) as fff:
            funfacts = fff.read().split(',')
        await self.bot.say(format(random.choice(funfacts)))

    @commands.command()
    async def jigabootime(self):
        """Returns a lyric from The Pharcyde - Jigaboo Time."""
        with open(os.path.join(self.sub_dir, 'jigaboo.list')) as jigaboo_file:
            jigaboo = jigaboo_file.read().split('|')
        await self.bot.say(format(random.choice(jigaboo)))

    @commands.command()
    async def autism(self, user : discord.Member=None):
        """
        Returns its own personal critique on an individual.
        """
        if user == None:
            await self.bot.say("You must specify a user.")
        else:
            autism_msg = "The individual {} has {} amounts of autism. I advise you to not speak so lightly, or even at all, about {}'s autism.\n*Thank you.*"
            autisms = ['high', 'medium', 'low']
            await self.bot.say(autism_msg.format(user.name, random.choice(autisms), user.name))

def setup(bot):
    bot.add_cog(memes(bot))