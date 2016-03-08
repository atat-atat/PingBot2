"""
A cog full of memes.

Ported from PingBot to PingBot2 by aidybee.
"""
import discord
from discord.ext import commands
import random
import os

class memes():
    def __init__(self, bot):
        self.bot = bot
        #MULTICOMMANDS COMMANDS

    @commands.command()
    async def no(self):
        no = ["http://i.imgur.com/xRBjBAf.jpg","http://i.imgur.com/zpc3sm4.jpg"]
        await self.bot.say(format(random.choice(no)))
    




    @commands.command()
    async def nice(self):
        nice = ["https://media.giphy.com/media/IUZtGhVO8hZ6w/200_s.gif","https://media.giphy.com/media/9uoYC7cjcU6w8/giphy.gif","https://media3.giphy.com/media/EaSH6bwyEQVkA/200_s.gif","https://media.giphy.com/media/IUZtGhVO8hZ6w/200_s.gif","https://media0.giphy.com/media/E6LPrrzKOJwhG/200.gif"]
        await self.bot.say(format(random.choice(nice)))
    




    @commands.command()
    async def really(self):
        really = ["infoboolen1","infoboolen2"]
        await self.bot.say(format(random.choice(really)))
    




    @commands.command()
    async def yes(self):
        yes = ["https://media.giphy.com/media/RA8poJqg54vq8/giphy.gif","https://media2.giphy.com/media/12Rq9uCNxcxtjq/200.gif","https://media3.giphy.com/media/xT0BKIEo6kn0neyQw0/200.gif","https://media0.giphy.com/media/Kzvsru1JqQg4E/200.gif","https://media1.giphy.com/media/x88e1awUi05by/200.gif","https://media2.giphy.com/media/26CalmkpfFU3io3yU/200.gif"]
        await self.bot.say(format(random.choice(yes)))
    




    @commands.command()
    async def lewd(self):
        lewd = ["http://i.imgur.com/XC1Lbxx.gif","http://i.imgur.com/SlNPKcQ.gif"]
        await self.bot.say(format(random.choice(lewd)))
    




    @commands.command()
    async def lmao(self):
        lmao = ["http://i.imgur.com/cumlma9.jpg","http://i.imgur.com/0ikt3oU.png"]
        await self.bot.say(format(random.choice(lmao)))
    




    @commands.command()
    async def kek(self):
        kek = ["http://i.imgur.com/VhACFrU.gif","http://i.imgur.com/KPuXLTF.gif"]
        await self.bot.say(format(random.choice(kek)))
    




    @commands.command()
    async def ded(self):
        ded = ["http://i.imgur.com/U0aFyDu.jpg","http://i.imgur.com/rSxpalQ.jpg","http://i.imgur.com/ZzUn7aN.jpg"]
        await self.bot.say(format(random.choice(ded)))
    




    @commands.command()
    async def aheago(self):
        aheago = ["http://i.imgur.com/DwOflwW.jpg","http://i.imgur.com/HQdXc2B.jpg","http://i.imgur.com/rrkWBF9.jpg","http://i.imgur.com/9aLXKlT.jpg","http://i.imgur.com/PubL4KZ.jpg","http://i.imgur.com/XKkFPYg.jpg","http://i.imgur.com/mVMVQS8.png","http://i.imgur.com/PdprpMW.jpg","http://i.imgur.com/h6vGR5S.jpg","http://i.imgur.com/Ou4hWL9.png","http://i.imgur.com/f998ULI.jpg","http://i.imgur.com/LsXIzYJ.png"]
        await self.bot.say(format(random.choice(aheago)))
    




    @commands.command()
    async def hitler(self):
        hitler = ["http://i.imgur.com/ifrYcSp.jpg","http://i.imgur.com/lyu2cos.jpg","http://i.imgur.com/orcp1Fn.jpg","http://i.imgur.com/0AtQAjo.jpg","http://i.imgur.com/SNhO4oz.jpg"]
        await self.bot.say(format(random.choice(hitler)))
    




    @commands.command()
    async def rekt(self):
        rekt = [":star:Underrekt",":star:Shrekt",":star:Gravity Rekt",":star:Steven Rekt",":star:Rekt Wars",":star:Rektcraft",":star:The Rektjuring",":star:Rekt Alone",":star:Rektmanji",":star:Rekt Alone II",":star:Rekt Alone III",":star:Alvin and the Rekt",":star:Counter-Strike: Global Rekt",":star:Me and Earl and the Rekt Girl",":star:Smosh The Rekt Movie",":star:Kramprekt",":star:How To Train A Rekt",":star:Rekt Time",":star:Hot Tub Rekt Machine", ":star:How I Rekt Your Mother", ":star:Its Always Sunny In Rekt"]
        await self.bot.say(format(random.choice(rekt)))
    




    @commands.command()
    async def woop(self):
        woop = ["http://i.imgur.com/2d8K1Yi.gif","http://i.imgur.com/mgBnxkw.gif"]
        await self.bot.say(format(random.choice(woop)))
    




    @commands.command()
    async def cancer(self):
        cancer = ["http://i.imgur.com/g87Wivp.jpg","http://i.imgur.com/WMiht99.jpg"]
        await self.bot.say(format(random.choice(cancer)))
    




    @commands.command()
    async def salty(self):
        salty = ["http://i.imgur.com/wzwmvhj.jpg","http://i.imgur.com/SeENIgh.jpg","http://i.imgur.com/8Se1zxf.jpg","http://i.imgur.com/6lclZFb.jpg"]
        await self.bot.say(format(random.choice(salty)))
        









        #TEXT RETURN COMMANDS
            ## EXAMPLE:
                #@commands.command()
                #async def boolean(self):
                #await self.bot.say("")
    @commands.command()
    async def triggerd(self):
        await self.bot.say("http://i.imgur.com/l6haVfV.gif")
    




    @commands.command()
    async def xd(self):
        await self.bot.say("http://i.imgur.com/bgdqZ6a.gif")
    




    @commands.command()
    async def wakeupmate(self):
        await self.bot.say("http://i.imgur.com/pOoqHjJ.gif")
    




    @commands.command()
    async def kappa(self):
        await self.bot.say("http://i.imgur.com/giUFzXG.png")
    




    @commands.command()
    async def ysmart(self):
        await self.bot.say("http://i.imgur.com/kjrbRK2.gif")
    




    @commands.command()
    async def yloyal(self):
        await self.bot.say("http://i.imgur.com/PFIObvo.gif")
    




    @commands.command()
    async def ygrateful(self):
        await self.bot.say("http://i.imgur.com/Z6dsmOw.gif")
    




    @commands.command()
    async def anotherone(self):
        await self.bot.say("http://i.imgur.com/vO1sHmy.gif")
    




    @commands.command()
    async def wordsearch(self):
        await self.bot.say("http://i.imgur.com/74XtHfc.png")
    




    @commands.command()
    async def gineq(self):
        await self.bot.say("http://i.imgur.com/xzDAGco.jpg")
    




    @commands.command()
    async def hanginthere(self):
        await self.bot.say("http://i.imgur.com/RQrEkC9.jpg")
    




    @commands.command()
    async def cummies(self):
        await self.bot.say("Just me and my 💕daddy💕, hanging out I got pretty hungry🍆 so I started to pout 😞 He asked if I was down ⬇for something yummy 😍🍆 and I asked what and he said hed give me his 💦cummies!💦 Yeah! Yeah!💕💦 I drink them!💦 I slurp them!💦 I swallow them whole💦 😍 It makes 💘daddy💘 😊happy😊 so it's my only goal... 💕💦😫Harder daddy! Harder daddy! 😫💦💕 1 cummy💦, 2 cummy💦💦, 3 cummy💦💦💦, 4💦💦💦💦 I'm 💘daddy's💘 👑princess 👑but I'm also a whore! 💟 He makes me feel squishy💗!He makes me feel good💜! 💘💘💘He makes me feel everything a little should!~ 💘💘💘 👑💦💘Wa-What!💘💦👑")
    




    @commands.command()
    async def trumpstump(self):
        await self.bot.say("IM STUMPING YOU, TRUMP!😭👋\r\n██]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] 10% complete.....\r\n████]]]]]]]]]]]]]]]]]]]]]]]]]]] 35% complete....\r\n███████]]]]]]]]]]]]]]]] 60% complete....\r\n███████████] 99% complete.....\r\n🚫ERROR!🚫\r\n💯True💯 ✔Trumps 💃👴 are unstumpable 💖I could never stump you Trump!💖 Send this to ten other 👴💃Trumps👴💃 who make 🇺🇸🇺🇸America🇺🇸🇺🇸 great 👍 again Or never stump 👞 again")
    




    @commands.command()
    async def cumstump(self):
        await self.bot.say("IM DELETING YOU, DADDY!😭👋 ██]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] 10% complete..... ████]]]]]]]]]]]]]]]]]]]]]]]]]]] 35% complete.... ███████]]]]]]]]]]]]]]]] 60% complete.... ███████████] 99% complete..... 🚫ERROR!🚫 💯True💯 Daddies are irreplaceable 💖I could never delete you Daddy!💖 Send this to ten other 👪Daddies👪 who give you 💦cummies💦 Or never get called ☁️squishy☁️ again❌❌😬😬❌❌ If you get 0 Back: no cummies for you 🚫🚫👿 3 back: you're squishy☁️💦 5 back: you're daddy's kitten😽👼💦 10+ back: Daddy😛😛💕💕💦👅👅")
    




    @commands.command()
    async def goodshit(self):
        await self.bot.say("IM DELETING YOU, DADDY!😭👋 ██]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] 10% complete..... ████]]]]]]]]]]]]]]]]]]]]]]]]]]] 35% complete.... ███████]]]]]]]]]]]]]]]] 60% complete.... ███████████] 99% complete..... 🚫ERROR!🚫 💯True💯 Daddies are irreplaceable 💖I could never delete you Daddy!💖 Send this to ten other 👪Daddies👪 who give you 💦cummies💦 Or never get called ☁️squishy☁️ again❌❌😬😬❌❌ If you get 0 Back: no cummies for you 🚫🚫👿 3 back: you're squishy☁️💦 5 back: you're daddy's kitten😽👼💦 10+ back: Daddy😛😛💕💕💦👅👅")
    




    @commands.command()
    async def spork(self):
        await self.bot.say("hi every1 im new!!!!!!! holds up spork my name is katy but u can call me t3h PeNgU1N oF d00m!!!!!!!! lol…as u can see im very random!!!! thats why i came here, 2 meet random ppl like me … im 13 years old (im mature 4 my age tho!!) i like 2 watch invader zim w/ my girlfreind (im bi if u dont like it deal w/it) its our favorite tv show!!! bcuz its SOOOO random!!!! shes random 2 of course but i want 2 meet more random ppl =) like they say the more the merrier!!!! lol…neways i hope 2 make alot of freinds here so give me lots of commentses!!!!\r\nDOOOOOMMMM!!!!!!!!!!!!!!!! <--- me bein random again _^ hehe…toodles!!!!!\r\n\r\nlove and waffles,\r\n\r\nt3h PeNgU1N oF d00m")
    




    @commands.command()
    async def porn(self):
        await self.bot.say("http://pornhub.com/random")
    




    @commands.command()
    async def gayporn(self):
        await self.bot.say("http://www.pornhub.com/gay/random")
    




    @commands.command()
    async def bruh(self):
        await self.bot.say("http://i.imgur.com/WLd5fX7.png")
    




    @commands.command()
    async def heybudd(self):
        await self.bot.say("https://www.youtube.com/watch?v=eVm88MX2Gw4")
    




    @commands.command()
    async def heil(self):
        await self.bot.say("http://i.imgur.com/ZvOVr3P.gif")
    




    @commands.command()
    async def kkk(self):
        await self.bot.say("http://i.imgur.com/B6Zfqox.jpg")
    




    @commands.command()
    async def smh(self):
        await self.bot.say("http://i.imgur.com/Jbe85tc.png")
    




    @commands.command()
    async def frick(self):
        await self.bot.say("http://i.imgur.com/SOoEOFr.png")
    




    @commands.command()
    async def aria(self):
        await self.bot.say("http://i.imgur.com/PwpZIsl.gif")












#Special Commands
#Special Commands
    @commands.command()
    async def rip(self):
        try:
            name = msg.content[len("!rip "):].strip()
            img = Image.open("rip.jpg")
            draw = ImageDraw.Draw(img)
                # font = ImageFont.truetype(<font-file>, <font-size>)
            font = ImageFont.truetype("comic.ttf", 28)
                # draw.text((x, y),"Sample Text",(r,g,b))
            draw.text((58, 149),"{} :(".format(name),(0,0,0),font=font)
            img.save('rip-radioedit.jpg')
            await self.bot.say(msg.channel, "rip-radioedit.jpg")
        except IndexError:
            await self.bot.say(msg.channel, "http://i.imgur.com/Ij5lWrM.png")
    









    @commands.command()
    async def funfacts(self):
        sub_dir = "C:/Users/Oppy/Documents/Projects/Python/Discord Bot/PingBot API/docs"
        fff = open(os.path.join(sub_dir,"funfacts.txt"),"r")
        funfacts = fff.read().split(',')
        fff.close()
        await self.bot.say("{}".format(random.choice(funfacts)))

def setup(bot):
    bot.add_cog(memes(bot))