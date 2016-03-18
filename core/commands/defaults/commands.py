import discord
from discord.ext import commands
import os
from core.config import ConfigLoader
import configparser

c = ConfigLoader()

#Most of these commands are experimental.
class Commands():
    def __init__(self, bot):
        self.bot = bot
        self.email = c.load(False, 'email')
        self.password = c.load(False, 'password')
        self.allow_bot_changes = c.load(False, 'user_bot_changes')
        self.original_name = c.load(False, 'bot_name')
        self.no_perm_msg = c.load(False, 'no_perm_msg')
        self.only_owner = c.load(False, 'only_owner')
        self.annoyed = c.load(False, 'annoyed')
        self.no_kick_perm = c.load(False, 'no_kick_perm')
        self.kick_forbidden = c.load(False, 'kick_forbidden')
        self.kick_success = c.load(False, 'kick_success')
        self.no_command_pm = c.load(False, 'no_command_pm')
        self.no_user_found = c.load(False, 'no_user_found')
        self.admins = c.load(False, 'admins')
        self.enable_welcome_msg = c.load(False, 'enable_welcome_msg')
        self.note_options = ['add', 'list', 'edit']

    @commands.command()
    async def waifu(self, member : discord.Member=None):
        """
        Returns your beloved waifu ;)
        """
        if member != None:
            await self.bot.say("**!!WAIFU ALERT!!**\r\n{}\r\n**!!WAIFU ALERT!!**".format(member.avatar_url))
        else:
            await self.bot.say(self.no_user_found)

    @commands.command(pass_context=True)
    async def say(self, ctx, *, string : str):
        """
        Makes the bot say something.
        """
        banned_words = c.load(False, 'banned_say_words')

        no_say = c.load(False, 'no_say')

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

    @commands.command(pass_context=True)
    async def rip(self, ctx, name : str=None):
        if name == None:
            await self.bot.say("http://i.imgur.com/Ij5lWrM.png")
        else:
            rl_name = name + " :("
            name_l = len(rl_name)
            name_length = int(128/name_l*4/3)
            image = util.manipulate_text(rl_name, name_length, 58, 149, 'rip', 'comic.ttf')
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
                config.configparser.SafeConfigParser()
                config.read('./core/docs/list/notes.ini')
                config['notes'][name] = value
                with open('./core/docs/list/notes.ini', 'w') as configfile:
                    config.write(configfile)
                await self.bot.type()
                await self.bot.say("Successfully edited note!")

    async def on_message(self, msg):
        if msg.content == "F":
            await self.bot.send_message(msg.channel, "You have paid respects.")

            #edit the welcome message of a server.
        if msg.content.startswith('!welcome_edit'):
            if self.enable_welcome_msg == True:
                if msg.author.id == msg.server.owner.id or msg.author.id in admins:
                    servw = msg.content[len("!welcome_edit "):].strip()
                    with open('./core/docs/welcome/' + msg.server.id + '.txt', 'w') as welcome_file:
                        welcome_file.write(servw)
                    await bot.send_message(msg.channel, "Successfully modified server welcome message!")
                else:
                    await bot.send_message(msg.channel, only_owner)

def setup(bot):
    n = Commands(bot)
    bot.add_listener(n.on_message, 'on_message')
    bot.add_cog(Commands(bot))