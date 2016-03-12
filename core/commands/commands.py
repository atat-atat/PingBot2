import discord
from discord.ext import commands
import os
import configparser

#Most of these commands are experimental.
class Commands():
    def __init__(self, bot):
        self.bot = bot
        info_dir = "./core/config"
        config = configparser.ConfigParser()
        config.read('./core/config/bot.info')
        self.email = config.get('config', 'email', fallback="Email")
        self.password = config.get('config', 'password', fallback="Password")
        self.allow_bot_changes = config.get('config', 'allow_bot_changes', fallback=True)
        self.enable_clear = config.get('config', 'enable_clear_cmd', fallback=False)
        self.original_name = config.get('config', 'original_name', fallback="PingBot")
        self.no_perm_msg = config.get('messages', 'no_permission', fallback="You do not have the permission to use this command.")
        self.only_owner = config.get('messages', 'only_owner', fallback="You must be the owner of this server to use this command.")
        self.annoyed = config.get('messages', 'nuisance_msg', fallback="Nice try.")
        self.divide_zero = config.get('messages', 'divide_zero', fallback="Haha, you're funny.")
        self.no_kick_perm = config.get('messages', 'no_kick_perm', fallback="Only the owner can kick users.")
        self.kick_forbidden_perm = config.get('messages', 'kick_forbidden', fallback="Failed to kick user.\r\nThe bot does not have the appropriate permission to kick users.")
        self.kick_success = config.get('messages', 'kick_success', fallback="Successfully kicked user.")
        self.no_command_pm = config.get('messages', 'no_command_pm', fallback="You cannot use this command in a PM.")
        self.no_user_msg = config.get('messages', 'failed_to_find_user', fallback="Failed to find that user.")

        with open(os.path.join(info_dir, 'admins.info'), 'r') as admins_file:
            self.admins = admins_file.read().split(',')

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
            await self.bot.say("Something went wrong.")
        except ZeroDivisionError:
            await self.bot.type()
            await self.bot.say(self.divide_zero)

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

    @commands.command(pass_context=True)
    async def change_game(self, ctx, *, game_name : str):
        """
        Changes the bots currently playing game.
        """
        if self.allow_bot_changes == False:
            if ctx.message.author.id in self.admins:
                await self.bot.change_status(discord.Game(name=game_name,idle=None))
                await self.bot.say("PingBot is now playing `{}`".format(game_name))
            else:
                await self.bot.say(self.no_perm_msg)
        else:
            await self.bot.change_status(discord.Game(name=game_name,idle=None))
            await self.bot.say("PingBot is now playing `{}`".format(game_name))

    @commands.command(pass_context=True)
    async def change_name(self, ctx, *, bot_name : str):
        """
        Changes the bots name.
        """
        if self.allow_bot_changes == False:
            if ctx.message.author.id in self.admins:
                await self.bot.edit_profile(password=self.password, username=bot_name)
                await self.bot.say("PingBot has turned into a `{}`".format(bot_name))
            else:
                await self.bot.say(no_perm_msg)
        else:
            await self.bot.edit_profile(password=self.password, username=bot_name)
            await self.bot.say("PingBot has turned into a `{}`".format(bot_name))

    @commands.command(pass_context=True)
    async def change_nameorig(self, ctx):
        """
        Changes the bots name back to its original name.
        """
        if self.allow_bot_changes == False:
            if ctx.message.author.id in self.admins:
                await self.bot.edit_profile(password=self.password, username=self.original_name)
                await self.bot.say("PingBot has returned to its original form.")
            else:
                await self.bot.say(no_perm_msg)
        else:
            await self.bot.edit_profile(password=self.password, username=self.original_name)
            await self.bot.say("PingBot has returned to its original form.")

    @commands.command(pass_context=True, hidden=True)
    async def clear(self, ctx, amount : int): #if you are enabling this feature, disable enable_delete_msg as clearing messages will spam your chat.
        #THIS COMMAND IS STILL NOT FINISHED
        if self.enable_clear == True:
            if ctx.message.author.id == ctx.message.server.owner.id:
                await self.bot.say('{} is deleting this channel\'s chat history...'.format(ctx.message.author))
                logs = await self.bot.logs_from(ctx.message.channel, limit=amount)
                for message in logs:
                    await self.bot.delete_message(message)
            else:
                await self.bot.say(self.annoyed)

def setup(bot):
    bot.add_cog(Commands(bot))