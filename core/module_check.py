from core.errors import ErrorsManager
from core.colors import colors
from core.logs import LogManager

e = ErrorsManager()
l = LogManager()

class Checklist:
	def search_for_lib(self, module_name):
		try:
			__import__(module_name)
			self.found = True
		except ImportError:
			self.found = False
			print(colors.cred+"Failed to find module! ("+module_name+")"+colors.cwhite)
			e.return_error(1, 'NoLib', 'Could not find '+module_name)
		return self.found

	def subtle_sfl(self, module_name):
		try:
			__import__(module_name)
			self.found = True
		except ImportError:
			self.found = False
			l.write_log("Failed to find module! ("+module_name+")")
		return self.found