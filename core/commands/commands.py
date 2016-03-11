import discord
from discord.ext import commands
import os
import configparser

#Most of these commands are experimental.
class Commands():
    def __init__(self, bot):
        self.bot = bot

    config = configparser.ConfigParser()
    config.read('./core/config/bot.info')
    no_perm_msg = config.get('messages', 'no_permission', fallback="You do not have the permission to use this command.")
    only_owner = config.get('messages', 'only_owner', fallback="You must be the owner of this server to use this command.")
    annoyed = config.get('messages', 'nuisance_msg', fallback="Nice try.")
    divide_zero = config.get('messages', 'divide_zero', fallback="Haha, you're funny.")
    no_kick_perm = config.get('messages', 'no_kick_perm', fallback="Only the owner can kick users.")
    kick_forbidden_perm = config.get('messages', 'kick_forbidden', fallback="Failed to kick user.\r\nThe bot does not have the appropriate permission to kick users.")
    kick_success = config.get('messages', 'kick_success', fallback="Successfully kicked user.")
    no_command_pm = config.get('messages', 'no_command_pm', fallback="You cannot use this command in a PM.")

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
            await self.bot.say(self.divide_zero)

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
                await self.bot.say(self.no_command_pm)
            else:
                if ctx.message.author.id == ctx.message.server.owner.id:
                    await self.bot.kick(member)
                    await self.bot.say(self.kick_success)
                else:
                    await self.bot.say(self.no_kick_perm)
        except discord.errors.Forbidden:
            await self.bot.say(self.kick_forbidden_perm)

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

    @commands.command(pass_context=True)
    async def say(self, ctx, *, string : str):
        """
        Makes the bot say something.
        """
        sub_dir = "./core/config"
        with open(os.path.join(sub_dir, "banned_words.info"), 'r') as bw_file:
            banned_words = bw_file.read().split('|')

        with open(os.path.join(sub_dir, "no_say.info"), 'r') as ns_file:
            no_say = ns_file.read().split(',')

        if ctx.message.server.id not in no_say:
            if any(word in string for word in banned_words):
                await self.bot.say(self.annoyed)
            else:
                await self.bot.say(string)

def setup(bot):
    bot.add_cog(Commands(bot))