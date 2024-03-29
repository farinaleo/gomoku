from dataclasses import dataclass
import os
import json


@dataclass
class SettingsStruct:
    """
    SettingsStruct class
    This class is used to store the settings for the application.
    """
    def __init__(self):
        self.__fps = None
        self.__music = None
        self.__fullscreen = None
        self.__window_size = None

    def get_fps(self) -> int:
        return self.__fps

    def set_fps(self, fps: int):
        self.__fps = fps

    def get_music(self) -> bool:
        return self.__music

    def set_music(self, music: bool):
        self.__music = music

    def get_fullscreen(self) -> bool:
        return self.__fullscreen

    def set_fullscreen(self, fullscreen: bool):
        self.__fullscreen = fullscreen

    def get_window_size(self) -> [int, int]:
        return self.__window_size

    def get_width(self) -> int:
        return self.__window_size[0]

    def get_height(self) -> int:
        return self.__window_size[1]

    def set_window_size(self, width: int, height: int):
        """set window size in the settings
        :param width: width of the window
        :param height: height of the window
        """
        self.__window_size = [width, height]

    def save(self) -> bool:
        """save settings to file. If file does not exist, create it."""
        save_path = os.path.expanduser("~/.config/gomoku/settings.json")
        save_dir = os.path.dirname(save_path)
        settings_file = {
            'max_framerate': self.get_fps(),
            'music': self.get_music(),
            'fullscreen': self.get_fullscreen(),
            'window_size': self.get_window_size()
        }
        try:
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            with open(save_path, 'w') as file:
                json.dump(settings_file, file, indent=4)
                print('settings saved')
                return True
        except Exception as e:
            print(f'cannot save settings file: {e}')
            return False

    def load_default_settings(self):
        """load default settings."""
        self.set_fps(60)
        self.set_music(True)
        self.set_fullscreen(True)
        self.set_window_size(1920, 1080)
        print('default settings loaded')

    def load(self):
        """load settings from file. If file does not exist, use default settings."""
        settings_path = os.path.expanduser("~/.config/gomoku/settings.json")
        try:
            if not os.path.exists(settings_path):
                print('settings file not found, using default settings...')
                self.load_default_settings()
                return
            with open(settings_path, 'r') as file:
                settings_file = json.load(file)
                self.set_fps(settings_file['max_framerate'])
                self.set_music(settings_file['music'])
                self.set_fullscreen(settings_file['fullscreen'])
                self.set_window_size(settings_file['window_size'][0], settings_file['window_size'][1])
                print('settings loaded')
        except Exception as e:
            print(f'cannot load settings file: {e}')
            self.load_default_settings()
