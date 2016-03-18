"""
Extremely basic file-writer system
"""
import datetime

class LogManager:
	def write_log(self, text):
		with open('./core/sys/system.log', 'a') as log_file:
			time = datetime.datetime.time(datetime.datetime.now())
			cur_time = str(time)
			log_file.write(cur_time+":"+text)
			pass