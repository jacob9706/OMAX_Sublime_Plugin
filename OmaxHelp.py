import sublime, sublime_plugin

s = sublime.load_settings('Preferences.sublime-settings')

def reload_layout_path():
	global s
	prepend = '{\n"cmd": ["'
	postpend = '", "$file"]\n}'
	path = s.get('layout_path', 'C:\\Program Files (x86)\\OMAX Corporation\\OMAX_Layout_and_Make\\Layout.exe')
	path = path.replace('\\', '\\\\')
	f = open(sublime.packages_path() + '/OMAX_Sublime_Plugin-master/OMAX_Script.sublime-build', 'w')
	f.write(prepend+path+postpend)
	f.close()

s.add_on_change('layout_path', reload_layout_path)

class OmaxHelpCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel()

		search_text = self.view.substr(sels[0])

		if search_text == '' or 'OMAX_' not in search_text:
			sublime.error_message('"' + search_text + '" Was not found in the help file.')
			return

		help_file = sublime.packages_path() + '/OMAX_Sublime_Plugin-master/Functions.omaxscript'

		with open(help_file) as f:
			lines = f.readlines()
			for l in lines:
				tmp_split = l.split('//', 1)
				if len(tmp_split) < 2:
						continue
				if ' ' + search_text + '(' in tmp_split[0] or ' ' + search_text + ';' in tmp_split[0] or  search_text + ':' in tmp_split[0]:
					sublime.message_dialog('"' + search_text + '":'+ tmp_split[1])
					return
		sublime.error_message('"' + search_text + '" Was not found in the help file.')