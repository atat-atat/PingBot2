import discord
from discord.ext import commands

from core.search import Search
from core.music import Music

s = Search()
music = Music()

if not discord.opus.is_loaded():
	discord.opus.load_opus('libopus-0.dll')

class MusicBot():
	def __init__(self, bot):
		self.bot = bot
		#determines whether the bot is connected to a voice channel
		self.voice = None
		#!music commands
		self.actions = ['play', 'direct', 'joinchan', 'stop', 'pause', 'leave']
		#the music player
		self.player = None

	@commands.command(pass_context=True)
	async def music(self, ctx, action : str=None, *, name : str=None): #!music play <SONG>
		author = ctx.message.author
		message = ctx.message
		chanel = message.channel
		if chanel.is_private:
			await self.bot.say("You cannot use `music` commands in chat.")
		else:
			if action not in self.actions: #check if action is equal to something
				await self.bot.say("That action does not exist!")
				return
			elif action == None:
				await self.bot.say("You must specify the action.")
				return
			else:
				if action == 'leave': #if the user types !music leave
					if self.voice != None and self.player != None: #check if bot is connected to a voice channel, and if the player is playing something.
						if self.player.is_playing:
							self.player.stop()
						await self.voice.disconnect()
					else:
						await self.bot.say("Not connected to any voice channel.")
				elif action == 'play': #if the user types !music play
					if name == None:
						await self.bot.say("You must specify the song name.")
						return
					if self.voice == None: #If the voice is not connected, then connect to the authors voice channel. (also check if author is connected to voice channel)
						if author.voice_channel != None:
							self.voice = await self.bot.join_voice_channel(author.voice_channel)
							self.player = self.voice.create_ffmpeg_player('')
							music.set_song_host(author.id)
						else:
							await self.bot.say("You must be connected to a voice channel!")
							return
					if music.is_song_host(author.id) == True: #check if the user is the current song host.
						if self.player.is_playing: #check if the player is already playing something, if so, stop the song.
							self.player.stop()
					else:
						await self.bot.say("You are not the current host!")
						return
					if name.startswith('http') or name.startswith('https'): #check if the song name is actually a link.
						music_file = music.download_youtube(True, name) #set music_file to download the url.
						self.player = self.voice.create_ffmpeg_player(music_file) #set player to play the song.
						self.player.start() #play the song.
					else: #if the song name is really just the song name.
						if name == None: #if the search query is set to nothing.
							await self.bot.say("You must specify what you would like to search for.")
							return
						await self.bot.say("Searching for that song on YouTube...")
						url = s.youtube(name) #Search for the song name
						await self.bot.say("Found URL: `{}`".format(url))
						music_file = music.download_youtube(True, url) #set music file to song name
						self.player = self.voice.create_ffmpeg_player('./core/music/' + music_file) #set player to play the song.
						self.player.start() #play the song.
				elif action == 'stop':
					if self.voice != None or self.player != None:
						self.player.stop()
						await self.bot.say("Stopped song.")
					else:
						await self.bot.say("The bot is not playing anything.")
				elif action == 'pause':
					if self.voice != None or self.player != None:
						self.player.pause()
						await self.bot.say("Paused song.")
					else:
						await self.bot.say("The bot is not playing anything.")
				elif action == 'transfer_host':
					if music.is_song_host(author.id) == True:
						for user in message.mentions:
							await self.bot.say("Transfering host privileges to `{}`...".format(user.name))
							music.set_song_host(user.id)
					

def setup(bot):
	bot.add_cog(MusicBot(bot))