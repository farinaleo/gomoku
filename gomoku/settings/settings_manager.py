from gomoku.data_structure import SettingsStruct
import json
import os


def save_settings(settings_config: SettingsStruct):
	"""Save the settings to a file.
	:param settings_config: SettingsStruct
	"""
	save_path = os.path.expanduser("~/.config/gomoku/settings.json")
	save_dir = os.path.dirname(save_path)

	settings_file = {
		'max_framerate': settings_config.get_fps(),
		'music': settings_config.get_music(),
		'sound': settings_config.get_sound(),
		'fullscreen': settings_config.get_fullscreen(),
		'window_size': settings_config.get_window_size()
	}

	try:
		if not os.path.exists(save_dir):
			os.makedirs(save_dir)

		with open(save_path, 'w') as file:
			json.dump(settings_file, file)
		print('ok')
	except PermissionError:
		print('cannot save settings file')


def load_settings() -> SettingsStruct:
	"""Load the settings from a file.
	:param settings_config: SettingsStruct
	"""
	save_path = os.path.expanduser("~/.config/gomoku/settings.json")
	settings_config = SettingsStruct()
	try:
		if not os.path.exists(save_path):
			print('settings file not found, using default settings...')
			save_settings(settings_config)
			return settings_config
		with open(save_path, 'r') as file:
			settings_file = json.load(file)
			settings_config.set_fps(settings_file['max_framerate'])
			settings_config.set_music(settings_file['music'])
			settings_config.set_sound(settings_file['sound'])
			settings_config.set_fullscreen(settings_file['fullscreen'])
			settings_config.set_window_size(settings_file['window_size'][0], settings_file['window_size'][1])
	except Exception as e:
		print('error loading settings file:')
		print(e)
	return settings_config

