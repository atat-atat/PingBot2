import youtube_dl
from core.config import ConfigLoader

c = ConfigLoader()

class Music:
	def __init__(self):
		self.song_host = None
	
	def set_song_host(self, user_id):
		self.song_host = user_id

	def is_song_host(self, user_id):
		if self.song_host != None:
			if self.song_host == user_id:
				return True
			else:
				return False
		else:
			return None

	def download_youtube(self, standard, url):
		options = {
			'format': 'bestaudio/best', # choice of quality
			'extractaudio' : False,      # only keep the audio
			'audioformat' : "mp3",      # convert to mp3 
			'outtmpl': 'core/music/%(id)s',        # name the file the ID of the video
			'noplaylist' : True,        # only download single song, not playlist
			}
		with youtube_dl.YoutubeDL(options) as ydl:
			music = ydl.download([url])
			r = ydl.extract_info(url, download=True)
		return r['id']