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
        self.no_ban_perm = pingbot.config_load_msg('no_ban_perm')
        self.ban_forbidden = pingbot.config_load_msg('ban_forbidden')
        self.ban_success = pingbot.config_load_msg('ban_success')
        self.no_command_pm = pingbot.config_load_msg('no_command_pm')
        self.no_user_found = pingbot.config_load_msg('no_user_found')
        self.avatar_change_success = pingbot.config_load_msg('avatar_change_success')
        self.enable_custom_commands = pingbot.config_load(False, 'enable_custom_commands')
        pingbot.init_command('evaluate')
        pingbot.init_command('waifu')
        pingbot.init_command('whois_waifu')
        pingbot.init_command('say')
        pingbot.init_command('chan_say')
        pingbot.init_command('direct_say')
        pingbot.init_command('global_say')
        pingbot.init_command('announce')
        pingbot.init_command('change_game')
        pingbot.init_command('change_name')
        pingbot.init_command('change_nameorig')
        pingbot.init_command('change_avatar')
        pingbot.init_command('change_avatarorig')
        pingbot.init_command('change_orig')
        pingbot.init_command('rip')
        pingbot.init_command('notes')
        pingbot.init_command('quotes')
        pingbot.init_command('welcome_edit')
        pingbot.init_command('whichone')
        pingbot.init_command('pm')
        pingbot.init_command('mention')
        pingbot.init_command('add_command')
        pingbot.init_command('role_test')
        pingbot.init_command('kick')
        pingbot.init_command('ban')
        pingbot.init_command('google')
        pingbot.init_command('youtube')
        pingbot.init_command('urban')
        pingbot.init_command('wiki')
        pingbot.init_command('clever')

        self.note_options=['list', 'add', 'edit']

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

    @commands.command(pass_context=True, hidden=True)
    async def global_say(self, ctx, *, string : str):
        """Sends this message to all servers the bot is currently connected to."""
        banned_words = pingbot.config_load(False, 'banned_say_words')
        if pingbot.is_bot_admin(ctx) == True:
            if any(word in string for word in banned_words):
                await self.bot.say(annoyed)
            else:
                for i in self.bot.servers:
                    await self.bot.send_message(i, string) #bot.say(string)
        else:
            await bot.say(self.no_perm_msg)

    @commands.command(pass_context=True)
    async def announce(self, ctx, *, string : str):
        """
        Sends a message to all channels of a server.
        """
        banned_words = pingbot.config_load(False, 'banned_say_words')
        if pingbot.is_bot_admin(ctx) == True:
            if any(word in string for word in banned_words):
                await self.bot.say(annoyed)
            else:
                for i in ctx.message.server.channels:
                    try:
                        await self.bot.send_message(i, string) #bot.say(string)
                    except discord.errors.Forbidden:
                        pass
        else:
            await bot.say(self.no_perm_msg)


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
                    await self.bot.say("`403: Forbidden` error occurred.")
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
                await self.bot.say("`403: Forbidden` error occurred.")

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
        """
        Outputs text on a tombstone.
        """
        if name == None:
            await self.bot.say("http://i.imgur.com/Ij5lWrM.png")
        else:
            rl_name = name + " :("
            name_l = len(rl_name)
            name_length = int(128/name_l*4/3)
            image = pingbot.manipulate_text(rl_name, name_length, 58, 149, 'rip', 'comic.ttf')
            await self.bot.send_file(ctx.message.channel, image)

    @commands.command(pass_context=True)
    async def notes(self, ctx, option : str=None, note_name : str=None, *, value : str=None):
        """Notes system."""
        if option == None and note_name == None and value == None:
            await self.bot.say("Unknown action.")
            return

        if option not in self.note_options and note_name == None and value == None:
            config = configparser.SafeConfigParser()
            config.read('./core/docs/list/notes.ini')
            if config.has_option('notes', option):
                note = config.get('notes', option)
                await self.bot.say(note)
            else:
                await self.bot.say("That note does not exist!")

        elif option == 'add':
            if note_name == None:
                await self.bot.say("You must specify the note name.")
                return

            if value == None:
                await self.bot.say("You must specify the note value.")
                return

            if note_name not in self.note_options:
                config = configparser.ConfigParser()
                config.read("./core/docs/list/notes.ini")
                config['notes'][note_name] = value
                with open('./core/docs/list/notes.ini', 'w') as configfile:
                    config.write(configfile)
                with open('./core/docs/list/notes.txt', 'a') as notes_file:
                    notes_file.write(note_name+",")
                await self.bot.type()
                await self.bot.say("Successfully created note!")
            else:
                await self.bot.say(self.annoyed)

        elif option == 'edit':
            if note_name == None:
                await self.bot.say("You must specify the note name.")
                return

            if value == None:
                await self.bot.say("You must specify the note value.")
            config = configparser.SafeConfigParser()
            config.read('./core/docs/list/notes.ini')
            config['notes'][note_name] = value
            with open('./core/docs/list/notes.ini', 'w') as configfile:
                config.write(configfile)
            await self.bot.say("Successfully edited note!")

        elif option == 'list':
            with open('./core/docs/list/notes.txt', 'r') as notes_file:
                notes = notes_file.read()
            await self.bot.say("Notes: `{}`".format(notes))

    @commands.command(hidden=True)
    async def quotes(self, action : str=None, name : str=None, *, value : str=None):
        """
        Quotes system. (wip)
        """
        if action == None:
            self.bot.say("You must specify the action.")
        elif action == 'add':
            self.bot.say("Unknown.")

    @commands.command(pass_context=True)
    async def welcome_edit(self, ctx, *, welcome_info : str):
        """
        Modifies the welcome message of a server.
        """
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

    @commands.command()
    async def command_add(self, command : str=None, *, value : str=None):
        """
        Adds a custom command.
        """
        cur_commands = pingbot.get_commands()
        if command in cur_commands:
            await self.bot.say("That command already exists!")
            return
        if self.enable_custom_commands == True:
            if command != None and value != None:
                pingbot.add_command(command, value)
                await self.bot.say("Successfully added command!")
            elif command == None:
                await self.bot.say("You must provide the command name.")
            elif value == None:
                await self.bot.say("You must provide the value.")

    @commands.command(pass_context=True, hidden=True)
    async def role_test(self, ctx):
        """
        Role permission check-test.
        """
        try:
            if ctx.message.author.roles[1].permissions.kick_members or ctx.message.author.is_owner:
                await self.bot.say("You can kick members.")
            else:
                await self.bot.say("You cannot kick members.")
        except IndexError:
            if ctx.message.author == ctx.message.server.owner:
                await self.bot.say("You can kick members.")
            else:
                await self.bot.say("You cannot kick members.")
        #for permission in ctx.message.author.permissions_for(self):
            #if permission.kick_members == True:
            #    await self.bot.say("You can kick members.")
            #else:
            #    await self.bot.say("You cannot kick members.")
        #for role in ctx.message.author.roles:
            #if role.kick_members:
                #await self.bot.say("You can kick members.")
            #else:
                #await self.bot.say("You cannot kick members.")
        #role1 = ctx.message.author.roles[0]
        #role1_1 = str(role1)
        #role1_final = role1_1.replace('@', '[@]')
        #role2 = ctx.message.author.roles[1]
        #await self.bot.say(role1_final)
        #await self.bot.say(role2)

    @commands.command(pass_context=True)
    async def kick(self, ctx, member : discord.Member):
        """
        Kicks a user. (You must be the server owner to use this command.)
        """
        try:
            if ctx.message.channel.is_private:
                await self.bot.say(self.no_command_pm)
            else:
                if pingbot.is_owner(ctx) == True:
                    await self.bot.kick(member)
                    await self.bot.say(self.kick_success)
                else:
                    await self.bot.say(self.no_kick_perm)
        except discord.errors.Forbidden:
            await self.bot.say(self.kick_forbidden)

    @commands.command(pass_context=True)
    async def ban(self, ctx, member : discord.Member):
        """
        Bans a user. (You must be the server owner to use this command.)
        """
        try:
            if ctx.message.channel.is_private:
                await self.bot.say(self.no_command_pm)
            else:
                if pingbot.is_owner(ctx) == True:
                    await self.bot.ban(member, 0)
                    await self.bot.say(self.ban_success)
                else:
                    await self.bot.say(self.no_ban_perm)
        except discord.errors.Forbidden:
            await self.bot.say(self.ban_forbidden)

    @commands.command()
    async def google(self, *, search_string : str):
        """Searches Google."""
        await self.bot.say(pingbot.search_standard('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&', search_string))

    @commands.command()
    async def youtube(self, *, search_string : str):
        """Searches YouTube."""
        await self.bot.say("*Searching for {}...*".format(search_string))
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
            await self.bot.say("{}\n\n**Example -**\n{}\nContributor-\n{}".format(meaning, example, contributor))
        except AttributeError:
            await self.bot.say("Could not find a definition for that word.")
        except discord.errors.HTTPException:
            await self.bot.say("The definition was too long...")

    @commands.command()
    async def wiki(self, *, search_string : str):
        """Searches Wikipedia."""
        try:
            result = wikipedia.summary(search_string, sentences = 5)
            await self.bot.say("**{}** {}".format(search_string, result))
        except wikipedia.exceptions.DisambiguationError:
            await self.bot.say("That page does not exist!")

    @commands.command()
    async def clever(self, *, input_string : str):
        """Talks to cleverbot."""
        try:
            response = cb1.ask(input_string)
            await self.bot.say(response)
        except cleverbot.cleverbot.CleverbotAPIError:
            await self.bot.say("Error! During attempted communication, something went wrong.")

    async def message_listener(self, msg):
        if msg.content == "F" or msg.content == "f":
            await self.bot.send_message(msg.channel, "{} has paid respects.".format(msg.author.name))

def setup(bot):
    n = Commands(bot)
    bot.add_listener(n.message_listener, 'on_message')
    bot.add_cog(Commands(bot))
