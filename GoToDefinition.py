import sublime, sublime_plugin
import os, sys, time, codecs

class GoToDefinitionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selected = self.view.sel()

		search_text = self.view.substr(selected[0])

		if search_text == '':
			sublime.error_message('Select a function name to search for.')
			return
		
		window = self.view.window()
		
		folders = window.folders()

		if len(folders) <= 0:
			sublime.error_message('Please open a project to use GoTo Definition');
			return

		syntax = self.view.settings().get('syntax')

		pre = []
		if syntax == 'Packages/OMAX_Sublime_Plugin-master/CPPScript/OMAX_C++.tmLanguage':
			pre.append('int')
			pre.append('void')
			pre.append('bool')
			pre.append('double')
			pre.append('float')
		elif syntax == 'Packages/OMAX_Sublime_Plugin-master/PascalScript/OMAX_Script_Pascal.tmLanguage':
			pre.append('function')
			pre.append('procedure')
		else:
			sublime.error_message('GoTo Definition can only be used with OMAX Scripts.')

		file, line = self.__get_line(folders, pre, search_text)

		print file, line

		if line == -1:
			sublime.error_message('Definition not found in the current project.')
			return
		
		opened_file = window.open_file(file)

		while opened_file.is_loading():
			time.sleep(0.1)

		pt = self.view.text_point(line, 0)

		self.view.sel().clear()
		self.view.sel().add(sublime.Region(pt))

		self.view.show(pt)




	def __get_files(self, root_dir):
		file_list = []

		for root, sub_folders, files in os.walk(root_dir):
			for file in files:
				f = os.path.join(root, file)
				file_list.append(f)
		return file_list

	def __get_line(self, folders, pre, search_text):
		search_text = search_text.lower()
		for folder in folders:
			files = self.__get_files(folder)
			for f in files:
				with codecs.open(f, 'r', encoding='utf-8') as open_file:
					lines = open_file.readlines()
					for i, line in enumerate(lines):
						line = line.lower()
						for p in pre:
							print str(p) + ' ' + str(search_text)
							if str(str(p) + ' ' + str(search_text)) in str(line):
								return f, i
		return '', -1