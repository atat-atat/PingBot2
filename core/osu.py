import urllib
from urllib.request import urlopen
import json

"""
Returns the information of an osu! user.
"""
class osu:

	def set_key(self, key):
		self.key = key

	def get_beatmap(self, name, value, parameters='m=0'): #Not completed! still dont get the point of this!
		url = "https://osu.ppy.sh/api/get_beatmaps?u=" + name + "&" + parameters + "&k=" + self.key
		search_response = urllib.request.urlopen(url)
		search_results = search_response.read().decode("utf8")
		results = json.loads(search_results)
		for i in results:
			val = i[value]
		self.info = val
		return self.info

	def get_user(self, name, value, parameters='m=0'):
		"""
		Values -
		user_id : returns the user id.
		username : returns the username.
		count300 : returns the number of 300s
		count100 : returns the number of 100s
		count50 : returns the number of 50s
		playcount : returns the playcount
		ranked_score : returns the ranked score.
		total_score : returns the total score.
		pp_rank : returns the PP rank.
		level : returns the level.
		pp_raw : returns the raw PP.
		accuracy : returns the accuracy.
		count_rank_ss : returns the number of SS'
		count_rank_s : returns the number of S'
		count_rank_a : returns the number of A's.
		country : returns the country.
		pp_country_rank : returns the PP country rank.
		events {
		display_html
		beatmap_id
		beatmapset_id
		date
		epicfactor
		}
		"""
		url = "https://osu.ppy.sh/api/get_user?u=" + name + "&" + parameters + "&k=" + self.key
		search_response = urllib.request.urlopen(url)
		search_results = search_response.read().decode("utf8")
		results = json.loads(search_results)
		for i in results:
			val = i[value]
		self.info = val
		return self.info