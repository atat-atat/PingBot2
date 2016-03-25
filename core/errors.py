"""
This class is pretty much just custom-raises.
"""
from core.colors import colors
import datetime
import os

class ErrorsManager:

	#for big errors
	def return_error(self, error_type, name, info):
		if error_type > 3:
			print(colors.cred+"Incorrect error type!"+colors.cwhite)
			input()
			sys.exit(0)
		print(colors.cred+name+": "+info+colors.cwhite)
		time = datetime.datetime.time(datetime.datetime.now())
		cur_time = str(time)
		if os.path.isfile('errors.log') == True:
			with open('errors.log', 'a') as error_log:
				error_log.write(cur_time+"[ERROR:"+error_type+"] "+name+": "+info)
		else:
			with open('errors.log', 'w') as error_log:
				error_log.write(cur_time+"[ERROR:"+error_type+"] "+name+": "+info)
		if error_type == 3:
			sys.exit(0)

	def subtle_error(self, name, info="Error has occured. Ignoring."):
		time = datetime.datetime.time(datetime.datetime.now())
		cur_time = str(time)
		if os.path.isfile('errors.log') == True:
			with open('errors.log', 'a') as error_log:
				error_log.write(cur_time+"[ERROR:1] "+name+": "+info)
		else:
			with open('errors.log', 'w') as error_log:
				error_log.write(cur_time+"[ERROR:1] "+name+": "+info)
		return