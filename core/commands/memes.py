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
    async def cummies(self):
        """An iconic meme."""
        await self.bot.say("Just me and my 💕daddy💕, hanging out I got pretty hungry🍆 so I started to pout 😞 He asked if I was down ⬇for something yummy 😍🍆 and I asked what and he said hed give me his 💦cummies!💦 Yeah! Yeah!💕💦 I drink them!💦 I slurp them!💦 I swallow them whole💦 😍 It makes 💘daddy💘 😊happy😊 so it's my only goal... 💕💦😫Harder daddy! Harder daddy! 😫💦💕 1 cummy💦, 2 cummy💦💦, 3 cummy💦💦💦, 4💦💦💦💦 I'm 💘daddy's💘 👑princess 👑but I'm also a whore! 💟 He makes me feel squishy💗!He makes me feel good💜! 💘💘💘He makes me feel everything a little should!~ 💘💘💘 👑💦💘Wa-What!💘💦👑")

    @commands.command()
    async def stump(self):
        """An iconic meme."""
        await self.bot.say("IM STUMPING YOU, TRUMP!😭👋\r\n██]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] 10% complete.....\r\n████]]]]]]]]]]]]]]]]]]]]]]]]]]] 35% complete....\r\n███████]]]]]]]]]]]]]]]] 60% complete....\r\n███████████] 99% complete.....\r\n🚫ERROR!🚫\r\n💯True💯 ✔Trumps 💃👴 are unstumpable 💖I could never stump you Trump!💖 Send this to ten other 👴💃Trumps👴💃 who make 🇺🇸🇺🇸America🇺🇸🇺🇸 great 👍 again Or never stump 👞 again")

    @commands.command()
    async def cumstump(self):
        """An iconic meme."""
        await self.bot.say("IM DELETING YOU, DADDY!😭👋 ██]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] 10% complete..... ████]]]]]]]]]]]]]]]]]]]]]]]]]]] 35% complete.... ███████]]]]]]]]]]]]]]]] 60% complete.... ███████████] 99% complete..... 🚫ERROR!🚫 💯True💯 Daddies are irreplaceable 💖I could never delete you Daddy!💖 Send this to ten other 👪Daddies👪 who give you 💦cummies💦 Or never get called ☁️squishy☁️ again❌❌😬😬❌❌ If you get 0 Back: no cummies for you 🚫🚫👿 3 back: you're squishy☁️💦 5 back: you're daddy's kitten😽👼💦 10+ back: Daddy😛😛💕💕💦👅👅")

    @commands.command()
    async def goodshit(self):
        """An iconic meme."""
        await self.bot.say("👌👀👌👀👌👀👌👀👌👀 good shit go౦ԁ sHit👌 thats ✔ some good👌👌shit right👌👌there👌👌👌 right✔there ✔✔if i do ƽaү so my self 💯 i say so 💯 thats what im talking about right there right there (chorus: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ) mMMMMᎷМ💯 👌👌 👌НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ👌 👌👌 👌 💯 👌 👀 👀 👀 👌👌Good shit")

    @commands.command()
    async def spork(self):
        """An iconic meme."""
        await self.bot.say("hi every1 im new!!!!!!! holds up spork my name is katy but u can call me t3h PeNgU1N oF d00m!!!!!!!! lol…as u can see im very random!!!! thats why i came here, 2 meet random ppl like me … im 13 years old (im mature 4 my age tho!!) i like 2 watch invader zim w/ my girlfreind (im bi if u dont like it deal w/it) its our favorite tv show!!! bcuz its SOOOO random!!!! shes random 2 of course but i want 2 meet more random ppl =) like they say the more the merrier!!!! lol…neways i hope 2 make alot of freinds here so give me lots of commentses!!!!\r\nDOOOOOMMMM!!!!!!!!!!!!!!!! <--- me bein random again _^ hehe…toodles!!!!!\r\n\r\nlove and waffles,\r\n\r\nt3h PeNgU1N oF d00m")
    
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
    async def note(self, option : str, name : str, *, value : str):
        """Notes system."""
        if option == "add":
            config = configparser.ConfigParser()
            config.read("commands.ini")
            config['commands'][name] = value
            with open('commands.ini', 'w') as configfile:
                config.write(configfile)
            with open(os.path.join(self.sub_dir,'commands.txt'), 'a') as notes_file:
                notes_file.write(name+",")
            await self.bot.type()
            await self.bot.say("Successfully created note!")
        elif option == "edit":
            config.configparser.SafeConfigParser()
            config.read('commands.ini')
            config['commands'][name] = value
            with open('commands.ini', 'w') as configfile:
                config.write(configfile)
            await self.bot.type()
            await self.bot.say("Successfully edited note!")
        elif option == "list":
            with open(os.path.join(self.sub_dir,'commands.txt'),'r') as notes_file:
                notes = notes_file.read()
            await self.bot.type()
            await self.bot.say("Notes: `{}`".format(notes))

    @commands.command()
    async def notes(self, name : str):
        """Read a note."""
        config = configparser.SafeConfigParser()
        config.read('commands.ini')
        cmd = config.get('commands', name)
        await self.bot.type()
        await self.bot.say(cmd)

def setup(bot):
    bot.add_cog(memes(bot))