import discord
from discord.ext import commands
import os
import configparser
from core.pingbot import PingbotCore
import urllib
import random
from random import randrange

pingbot = PingbotCore()

#Most of these commands are experimental.
class Commands():
    def __init__(self, bot):
        self.bot = bot
        self.username = pingbot.config_load(False, 'bot_name')
        self.email = pingbot.config_load(False, 'email')
        self.password = pingbot.config_load(False, 'password')
        self.allow_bot_changes = pingbot.config_load(False, 'user_bot_changes')
        self.original_name = pingbot.config_load(False, 'bot_name')
        self.admins = pingbot.config_load(False, 'admins')
        self.enable_welcome_msg = pingbot.config_load(False, 'enable_welcome_msg')
        self.no_perm_msg = pingbot.config_load_msg('no_perm_msg')
        self.only_owner = pingbot.config_load_msg('only_owner')
        self.annoyed = pingbot.config_load_msg('annoyed')
        self.no_kick_perm = pingbot.config_load_msg('no_kick_perm')
        self.kick_forbidden = pingbot.config_load_msg('kick_forbidden')
        self.kick_success = pingbot.config_load_msg('kick_success')
        self.no_command_pm = pingbot.config_load_msg('no_command_pm')
        self.no_user_found = pingbot.config_load_msg('no_user_found')
        self.avatar_change_success = pingbot.config_load_msg('avatar_change_success')

        self.note_options = ['add', 'list', 'edit']

    @commands.command(hidden=True)
    async def evaluate(self, *, eval_value : str=None):
        """
        Evaluate a line of code.
        """
        try:
            if eval_value != None:
                result = eval(eval_value)
                await self.bot.say(result)
            else:
                await self.bot.say("Empty value.")
        except Exception as e:
            await self.bot.say("An error occurred.\n```{}: {}```".format(str(e), e.args))

    @commands.command()
    async def waifu(self, member : discord.Member=None):
        """
        Returns your beloved waifu ;)
        """
        if member != None:
            await self.bot.say("**!!WAIFU ALERT!!**\n{}\n**!!WAIFU ALERT!!**".format(member.avatar_url))
        else:
            await self.bot.say(self.no_user_found)

    @commands.command(pass_context=True)
    async def whois_waifu(self, ctx):
        """
        Returns PingBot's personal waifu.
        """
        if ctx.message.channel.is_private:
            await self.bot.say("You cannot use this command in a PM.")
        else:
            server = ctx.message.author.server
            members = server.members
            _member = random.sample(list(members), 1)
            member = random.choice(_member)
            if member == self.bot.user:
                await self.bot.say("My waifu is *myself* :heart:")
            elif member == ctx.message.author:
                await self.bot.say("My waifu is *you*, <@{}> :heart:".format(member.id))
            else:
                await self.bot.say("My waifu is *{}* :heart:".format(member.name))

    @commands.command(pass_context=True)
    async def say(self, ctx, *, string : str):
        """
        Makes the bot say something.
        """
        banned_words = pingbot.config_load(False, 'banned_say_words')

        no_say = pingbot.config_load(False, 'no_say')

        if ctx.message.server.id not in no_say:
            if any(word in string for word in banned_words):
                await self.bot.say(self.annoyed)
            else:
                await self.bot.say(string)

    @commands.command(pass_context=True)
    async def chan_say(self, ctx, channel : discord.Channel=None, *, message : str=None):
        """
        Send a direct message to a server/channel.
        """
        if channel == None or message == None:
            await self.bot.say("You did not provide the correct parameters.")
            return
        await self.bot.say("Sent message to the channel, `{}`.".format(channel))
        await self.bot.send_message(channel, message)

    @commands.command(pass_context=True)
    async def direct_say(self, ctx, user : discord.Member=None, *, message : str=None):
        """
        Sends a direct message to a user.
        """
        if user == None:
            await self.bot.say("You must specify a user.")
        elif message == None:
            await self.bot.say("You must specify a message.")
        elif user == ctx.message.author:
            await self.bot.say("Sent message to yourself.")
        elif user == self.bot.user:
            await self.bot.say(self.annoyed)
        else:
            await self.bot.say("Sending message to `{}`".format(user.name))
            await self.bot.send_message(user, message)


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
            if pingbot.is_bot_admin(ctx):
                await self.bot.edit_profile(password=self.password, username=bot_name)
                await self.bot.say("PingBot has turned into a `{}`".format(bot_name))
            else:
                await self.bot.say(self.no_perm_msg)
        else:
            await self.bot.edit_profile(password=self.password, username=bot_name)
            await self.bot.say("PingBot has turned into a `{}`".format(bot_name))

    @commands.command(pass_context=True)
    async def change_avatar(self, ctx, image_url : str):
        """
        Changes the bots avatar.
        """
        if self.allow_bot_changes == False:
            if pingbot.is_bot_admin(ctx):
                try:
                    pingbot.updater().retrieve_url(image_url, 'avatar_dl.png')
                    with open('./core/sys/cache/avatar_dl.png', 'rb') as avatar_file:
                        avatar = avatar_file.read()
                    await self.bot.edit_profile(password=self.password, avatar=avatar)
                    await self.bot.say("PingBot has changed its avatar to `{}`".format(image_url))
                except urllib.error.HTTPError:
                    await self.bot.say("`403: Forbidden` error occurred.\n(For now, blame the jews.)")
            else:
                await self.bot.say(self.no_perm_msg)
        else:
            try:
                pingbot.updater().retrieve_url(image_url, 'avatar_dl.png')
                with open('./core/sys/cache/avatar_dl.png', 'rb') as avatar_file:
                    avatar = avatar_file.read()
                await self.bot.edit_profile(password=self.password, avatar=avatar)
                await self.bot.say("PingBot has changed its avatar to `{}`".format(image_url))
            except urllib.error.HTTPError:
                await self.bot.say("`403: Forbidden` error occurred.\n(For now, blame the jews.)")

    @commands.command(pass_context=True)
    async def change_avatarorig(self, ctx):
        """
        Changes the bot's avatar back to the original avatar.
        """
        if self.allow_bot_changes == False:
            if pingbot.is_bot_admin(ctx):
                with open('./user/avatar.png', 'rb') as avatar_file:
                    avatar = avatar_file.read()
                await self.bot.edit_profile(password=self.password, avatar=avatar)
                await self.bot.say("PingBot has changed its avatar back to the original.")
            else:
                await self.bot.say(self.no_perm_msg)
        else:
            with open('./user/avatar.png', 'rb') as avatar_file:
                avatar = avatar_file.read()
            await self.bot.edit_profile(password=self.password, avatar=avatar)
            await self.bot.say("PingBot has changed its avatar back to the original.")

    @commands.command(pass_context=True)
    async def change_avatar_dl(self, ctx):
        """
        Changes avatar to the most recent downloaded avatar.
        """
        if self.allow_bot_changes == False:
            if pingbot.is_bot_admin(ctx):
                with open('./core/sys/cache/avatar_dl.png', 'rb') as avatar_file:
                    avatar = avatar_file.read()
                await self.bot.say(self.avatar_rf_change_success)
                await self.bot.edit_profile(password=self.password, avatar=avatar)
            else:
                await self.bot.say(self.no_perm_msg)
                return
        else:
            with open('./core/sys/cache/avatar_dl.png', 'rb') as avatar_file:
                avatar = avatar_file.read()
            await self.bot.say(self.avatar_rf_change_success)
            await self.bot.edit_profile(password=self.password, avatar=avatar)

    @commands.command(pass_context=True)
    async def change_orig(self, ctx):
        """
        Changes some of the bots information back to original.
        """
        if self.allow_bot_changes == False:
            if pingbot.is_bot_admin(ctx):
                with open('./core/images/icon.png', 'rb') as avatar_file:
                    avatar = avatar_file.read()
                await self.bot.edit_profile(password=self.password, username=self.username, avatar=avatar)
                await self.bot.say("Returned information back to original.")
            else:
                await self.bot.say(self.no_perm_msg)
        else:
            with open('./core/images/icon.png', 'rb') as avatar_file:
                avatar = avatar_file.read()
            await self.bot.edit_profile(password=self.password, username=self.username, avatar=avatar)
            await self.bot.say("Returned information back to original.")


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
                await self.bot.say(self.no_perm_msg)
        else:
            await self.bot.edit_profile(password=self.password, username=self.original_name)
            await self.bot.say("PingBot has returned to its original form.")

    @commands.command(pass_context=True)
    async def rip(self, ctx, *, name : str=None):
        if name == None:
            await self.bot.say("http://i.imgur.com/Ij5lWrM.png")
        else:
            rl_name = name + " :("
            name_l = len(rl_name)
            name_length = int(128/name_l*4/3)
            image = pingbot.manipulate_text(rl_name, name_length, 58, 149, 'rip', 'comic.ttf')
            await self.bot.send_file(ctx.message.channel, image)

    @commands.command()
    async def notes(self, option : str, name : str=None, *, value : str=None):
        """Notes system."""
        if option not in self.note_options:
            config = configparser.SafeConfigParser()
            config.read('./core/docs/list/notes.ini')
            if config.has_option('notes', option):
                note = config.get('notes', option)
                await self.bot.say(note)
            else:
                await self.bot.say("That note does not exist!")
        else:
            if name == None and value == None:
                if option == "list":
                    with open('./core/docs/list/notes.txt', 'r') as notes_file:
                        notes = notes_file.read()
                    await self.bot.say("Notes: `{}`".format(notes))
            elif option == "add":
                if name not in self.note_options:
                    config = configparser.ConfigParser()
                    config.read("./core/docs/list/notes.ini")
                    config['notes'][name] = value
                    with open('./core/docs/list/notes.ini', 'w') as configfile:
                        config.write(configfile)
                    with open('./core/docs/list/notes.txt', 'a') as notes_file:
                        notes_file.write(name+",")
                    await self.bot.type()
                    await self.bot.say("Successfully created note!")
                else:
                    await self.bot.say(self.annoyed)
            elif option == "edit":
                config = configparser.SafeConfigParser()
                config.read('./core/docs/list/notes.ini')
                config['notes'][name] = value
                with open('./core/docs/list/notes.ini', 'w') as configfile:
                    config.write(configfile)
                await self.bot.type()
                await self.bot.say("Successfully edited note!")

    @commands.command()
    async def quotes(self, action : str=None, name : str=None, *, value : str=None):
        """
        Quotes system. (wip)
        """
        if action == None:
            self.bot.say("You must specify the action.")
        elif action == 'add':
            self.bot.say("Unknown.")

    @commands.command(pass_context=True)
    async def welcome_edit(self, ctx, welcome_info : str):
        msg = ctx.message
        if self.enable_welcome_msg == True:
            if pingbot.is_owner(ctx) == True or pingbot.is_bot_admin(ctx) == True:
                with open('./core/docs/welcome/' + msg.server.id + '.txt', 'w') as welcome_file:
                    welcome_file.write(welcome_info)
                await self.bot.say("Successfully modified server welcome message!")
            else:
                await self.bot.say(self.only_owner)

    @commands.command()
    async def whichone(self, *, choices_string : str):
        """
        Selects a choice.
        """
        if ' or ' in choices_string:
            choices = choices_string.split(' or ')
            random_index = randrange(0, len(choices))
            await self.bot.say("I would choose, {}.".format(choices[random_index]))
        else:
            await self.bot.say("I'm not sure...")

    @commands.command(pass_context=True)
    async def pm(self, ctx, user : discord.Member=None, *, message : str=None):
        """
        Sends a message to a user.
        """
        if user == None:
            await self.bot.say(self.no_user_found)
        elif message == None:
            await self.bot.say(self.annoyed)
        elif user == self.bot.user:
            await self.bot.say(self.annoyed)
        elif user == ctx.message.author:
            await self.bot.say("Well, alright then. \nSending message to yourself.")
            await self.bot.send_message(user, "You have sent yourself the following message: {}".format(message))
        else:
            await self.bot.say("Sending message to `{}`...".format(user))
            await self.bot.send_message(user, "`{}` has sent you the following message: {}".format(ctx.message.author, message))

    @commands.command(pass_context=True)
    async def mention(self, ctx, user : discord.Member=None):
        """
        Mentions a user.
        """
        holidays = ["Merry Christmas", "Happy Halloween", "Happy Thanksgiving", "Happy Hanukkah"]
        if user == None:
            await self.bot.say("You must specify a user.")
        elif user == ctx.message.author:
            await self.bot.say("{}, <@{}>".format(random.choice(holidays), user.id))
        else:
            await self.bot.say("<@{}>".format(user.id))

    async def message_listener(self, msg):
        if msg.content == "F" or msg.content == "f":
            await self.bot.send_message(msg.channel, "{} has paid respects.".format(msg.author.name))

def setup(bot):
    n = Commands(bot)
    bot.add_listener(n.message_listener, 'on_message')
    bot.add_cog(Commands(bot))