import sublime, sublime_plugin, datetime, os, urllib2

should_check = True
settings = sublime.load_settings("update_settings.sublime-settings")

class OmaxUpdateChecker(sublime_plugin.EventListener):
	def on_load(self, view):
		global should_check, settings

		if should_check and settings.get("check_for_updates", True):
			should_check = False
			appdata_path = os.getenv('APPDATA')
			timestamp_path = appdata_path + r'\OMAX_UPDATE_STAMP.stamp'
			no_file = False
			day = datetime.datetime.today()
			
			if (not os.path.exists(timestamp_path)):
				no_file = True

			if no_file:
				f = open(timestamp_path, 'w')
				f.write(day.strftime('%m.%d.%Y'))
				f.close()
			else:
				with open(timestamp_path, 'r') as f:
					line = f.readline()
					day = datetime.datetime.strptime(line.strip(), '%m.%d.%Y')
			time_page = urllib2.urlopen('http://sweng.omax.com/SublimeExtension/sublime_text_2_update_time.php', timeout=0.5)
			server_time = datetime.datetime.strptime(time_page.readline(), '%m.%d.%Y')

			if day < server_time:
				if sublime.ok_cancel_dialog('A new update for the OMAX Sublime Extension is avaliable.\n\n'+\
					'To install the update click "OK". Once the installer is open close Sublime Text.\n\n'+\
					'To disable this, and future update messages change the settings in "Preferences" -> "OMAX Update Preferences"'):
					path = os.environ["PROGRAMDATA"]
					os.startfile(path + r'\OMAX_Sublime_Extension\OMAX_Sublime_Extension_Installer.exe')