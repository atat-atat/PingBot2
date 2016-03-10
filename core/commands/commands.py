import discord
from discord.ext import commands

#Most of these commands are experimental.
class Commands():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def calc(self, *, value):
        """
        Very terrible calculator system.
        """
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
    async def join_date(self, member : discord.Member):
        """
        Returns the join date of a user.
        """
        await self.bot.say("User `{}` joined on `{}`!".format(member.name, member.joined_at))

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

    @commands.command(pass_context=True)
    async def kick(self, ctx, member : discord.Member):
        """
        Kicks a user. (You must be the server owner to use this command.)
        """
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

    @commands.command()
    async def avatar(self, member : discord.Member):
        """
        Gets the avatar of a user.
        """
        await self.bot.say("Avatar of `{}` is {}".format(member.name, member.avatar_url))

    @commands.command()
    async def waifu(self, member : discord.Member):
        """
        Returns your beloved waifu ;)
        """
        await self.bot.say("**!!WAIFU ALERT!!**\r\n{}\r\n**!!WAIFU ALERT!!**".format(member.avatar_url))

def setup(bot):
    bot.add_cog(Commands(bot))