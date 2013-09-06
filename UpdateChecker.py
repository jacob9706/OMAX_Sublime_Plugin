import sublime, sublime_plugin, datetime, os, urllib2

class OmaxUpdateChecker(sublime_plugin.EventListener):
	def on_load(self, view):
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
		time_page = urllib2.urlopen('http://localhost/sublime_text_2_update_time.php', timeout=0.5)
		server_time = datetime.datetime.strptime(time_page.readline(), '%m.%d.%Y')

		if day < server_time:
			sublime.message_dialog('A new update for the OMAX Sublime Extension is avaliable, please run the installer.')

			f = open(timestamp_path, 'w')
			f.write(server_time.strftime('%m.%d.%Y'))
			f.close()