import sublime, sublime_plugin, datetime, os, urllib2, webbrowser

should_check = True
should_display = True
settings = sublime.load_settings("update_settings.sublime-settings")

changelog_file = sublime.packages_path() + '/OMAX_Sublime_Plugin-master/CHANGE_LOG.txt'
changelog_settings_file = sublime.packages_path() + '/OMAX_Sublime_Plugin-master/changelog_settings.sublime-settings'

class OmaxUpdateChecker(sublime_plugin.EventListener):
	def on_load(self, view):
		global should_check, settings, changelog_settings, changelog_file, should_display

		if should_check and settings.get("check_for_updates", True):
			should_check = False
			appdata_path = os.getenv('APPDATA')
			
			if sublime.ok_cancel_dialog('This version of the OMAX Sublime Extension is out dated and no longer supported.\n\n' +
										'Please visit http://omax.com/support/ to download the latest version.\n\n' +
										'Click Ok to go to the site.'):
				webbrowser.open('http://omax.com/support/')
