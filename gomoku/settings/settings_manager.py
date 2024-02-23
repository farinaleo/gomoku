from gomoku.data_structure import SettingsStruct
import json
import os


def save_settings(settings_config: SettingsStruct):
	save_path = os.path.expanduser("~/.config/gomoku/settings.json")
	save_dir = os.path.dirname(save_path)

	settings_file = {
		'max_framerate': settings_config.get_fps(),
		'music': settings_config.get_music(),
		'sound': settings_config.get_sound(),
		'fullscreen': settings_config.get_fullscreen(),
		'windows_size': settings_config.get_windows_size()
	}
	try:
		if not os.path.exists(save_dir):
			os.makedirs(save_dir)

		with open(save_path, 'w') as file:
			json.dump(settings_file, file)
		print('ok')
	except PermissionError:
		print('cannot save settings file')