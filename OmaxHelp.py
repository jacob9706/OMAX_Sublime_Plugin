import sublime, sublime_plugin, re

class OmaxHelpCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view

		#get current word
		selection_region = view.sel()[0]
		word_region = view.word(selection_region)
		search_text = view.substr(word_region).strip()
		search_text = re.sub('[\(\)\{\}\s]', '', search_text)
		orig_search_text = search_text
		search_text = search_text.lower()

		if search_text == '' or 'omax_' not in search_text:
			sublime.error_message('"' + search_text + '" Was not found in the help file.')
			return

		help_file = sublime.packages_path() + '/OMAX_Sublime_Plugin-master/Functions.omaxscript'

		with open(help_file) as f:
			lines = f.readlines()
			for l in lines:
				l = l.lower()
				tmp_split = l.split('//', 1)
				if len(tmp_split) < 2:
						continue
				if ' ' + search_text + '(' in tmp_split[0] or ' ' + search_text + ';' in tmp_split[0] or  search_text + ':' in tmp_split[0]:
					sublime.message_dialog('"' + orig_search_text + '":'+ tmp_split[1])
					return
		sublime.error_message('"' + orig_search_text + '" Was not found in the help file.')