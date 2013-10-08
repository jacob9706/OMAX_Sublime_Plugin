import sublime, sublime_plugin, re, os

# This is a TextCommand. It operates on the selected text (in this case) and looks up documentation.
class OmaxHelpCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view

		# Get selected text and convert to lowercase
		selection_region = view.sel()[0]
		word_region = view.word(selection_region)
		search_text = view.substr(word_region).strip()
		search_text = re.sub('[\(\)\{\}\s]', '', search_text)
		orig_search_text = search_text
		search_text = search_text.lower()

		# If what we are looking for does not contain "omax_", show error message
		if search_text == '':
			sublime.error_message('To use OMAX Function Help, put the cursor inside word/function call.')
			return
		elif 'omax_' not in search_text:
			sublime.error_message('"' + orig_search_text + '" is not an OMAX function.')
			return

		# Get the help file path
		help_file = sublime.packages_path() + '/OMAX_Sublime_Plugin-master/Functions.omaxscript'

		# Open the help file
		with open(help_file) as f:
			lines = f.readlines()
			# Loop thorugh each line
			for l in lines:
				# Convert line to lowercase
				l = l.lower()
				# Split the line up at comment
				tmp_split = l.split('//', 1)
				if len(tmp_split) < 2:
						continue
				# If we meet the format conditions show the documentation
				if ' ' + search_text + '(' in tmp_split[0] or ' ' + search_text + ';' in tmp_split[0] or  search_text + ':' in tmp_split[0]:
					sublime.message_dialog('"' + orig_search_text + '"\n'+ tmp_split[1].strip())
					return
		 # If we reach here we did not find anyting so show error message.
		sublime.error_message('"' + orig_search_text + '" was not found in the help file.')


# This is a text command that will launch the omax help document in
# the default system viewer for ".rtf" files.
class OmaxLaunchHelpCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		os.system(r'start %PROGRAMDATA%\OMAX_Sublime_Extension\Sublime_Help_Document.rtf')