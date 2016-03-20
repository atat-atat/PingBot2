import json
import urllib.parse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from core.errors import ErrorsManager
from core.colors import colors
import random

e = ErrorsManager()

class Search:
	def search(self, search_link, query_string='bacon'):
		"""
		Known search types -
		Google : http://ajax.googleapis.com/ajax/services/search/web?v=1.0&
		YouTube : https://ajax.googleapis.com/ajax/services/search/video?v=1.0&
		"""
		query = urllib.parse.urlencode({'q': query_string})
		url = search_link + '%s' % query
		search_response = urllib.request.urlopen(url)
		search_results = search_response.read().decode("utf8")
		results = json.loads(search_results)
		data = results['responseData']
		hits = data['results']
		for h in hits:
			h = h['url']
		self.output = h
		return self.output

	def youtube(self, query_string): #this is here to only clear a strange bug with searching on YouTube
		query = urllib.parse.quote(query_string)
		url = "https://www.youtube.com/results?search_query=" + query
		response = urllib.request.urlopen(url)
		html = response.read()
		soup = BeautifulSoup(html, "html.parser")
		vids = soup.findAll(attrs={'class':'yt-uix-tile-link'})
		vid = random.choice(vids)
		video = 'https://www.youtube.com' + vid['href']
		return video

class Div:
	def div_set_link(self, url, query):
		self.div_url = url
		self.div_query = query

	def div_get(self, dtype, content):
		try:
			r = requests.get(self.div_url+"{}".format(self.div_query))
			soup = BeautifulSoup(r.content, "html.parser")
			outcome = soup.find("div",attrs={dtype:content}).text
		except AttributeError as e:
			print(colors.cred+"An attribute error occurred!"+colors.cwhite)
			e.return_error(2, 'AttributeError', e)
			return
		return outcome