import sublime, sublime_plugin

# Create a event listener that on file load checks the first line
# of a file and sets the syntax accordingly
class SyntaxSelectorCommand(sublime_plugin.EventListener):
	def on_load(self, view):
		# Get the file name
		fn = view.file_name()

		# Open the file. Once the block finishes the file is closed automatically.
		with open(fn, 'r') as f:
			# Get the first line
			line = f.readline()
			# Check and set syntax
			if 'Pascal' in line:
				view.settings().set('syntax', 'Packages/OMAX_Sublime_Plugin-master/PascalScript/OMAX_Script_Pascal.tmLanguage')
				print "PascalScript"
			elif 'C++' in line:
				view.settings().set('syntax', 'Packages/OMAX_Sublime_Plugin-master/CPPScript/OMAX_C++.tmLanguage')
				print "C++ Script"
