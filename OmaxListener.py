import sublime, sublime_plugin

class OmaxListenerCommand(sublime_plugin.EventListener):
	def on_activated(self, view):
		print view.file_name()