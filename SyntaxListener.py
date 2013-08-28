import sublime, sublime_plugin

class ExampleCommand(sublime_plugin.EventListener):
	def on_load(self, view):
		window = self.view.window()
		v = window.active_view()
		fn = v.file_name()

		with open(fn) as f:
			line = f.readline()
			if 'Pascal' in line:
				view.settings().set('syntax', 'Packages/OMAX_Sublime_Plugin-master/PascalScript/OMAX_Script_Pascal.tmLanguage')
				print "PascalScript"
			elif 'C++' in line:
				view.settings().set('syntax', 'Packages/OMAX_Sublime_Plugin-master/CPPScript/OMAX_C++.tmLanguage')
				print "C++ Script"
