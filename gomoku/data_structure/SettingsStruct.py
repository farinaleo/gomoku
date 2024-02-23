from dataclasses import dataclass, field
import os
import json


@dataclass
class SettingsStruct:
    """
    SettingsStruct class
    This class is used to store the settings for the application.
    """
    __fps: int = 30
    __music: bool = True
    __sound: bool = True
    __fullscreen: bool = False
    __window_size: [int, int] = field(default=(1280, 720))

    def print(self):
        """print representation of the SettingsStruct. Debug only"""
        print('SettingsStruct contain :')
        print(f'fps: {self.__fps}, music: {self.__music}, sound: {self.__sound}, fullscreen: {self.__fullscreen}, size: {self.__window_size}')

    def get_fps(self) -> int:
        return self.__fps

    def set_fps(self, fps: int):
        self.__fps = fps

    def get_music(self) -> bool:
        return self.__music

    def set_music(self, music: bool):
        self.__music = music

    def get_sound(self) -> bool:
        return self.__sound

    def set_sound(self, sound: bool):
        self.__sound = sound

    def get_fullscreen(self) -> bool:
        return self.__fullscreen

    def set_fullscreen(self, fullscreen: bool):
        self.__fullscreen = fullscreen

    def get_window_size(self) -> [int, int]:
        return self.__window_size

    def set_window_size(self, width: int, height: int):
        self.__window_size = [width, height]

    def save(self):
        """save settings to file. If file does not exist, create it."""
        save_path = os.path.expanduser("~/.config/gomoku/settings.json")
        save_dir = os.path.dirname(save_path)
        settings_file = {
            'max_framerate': self.get_fps(),
            'music': self.get_music(),
            'sound': self.get_sound(),
            'fullscreen': self.get_fullscreen(),
            'window_size': self.get_window_size()
        }
        try:
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            with open(save_path, 'w') as file:
                json.dump(settings_file, file)
                print('settings saved')
        except Exception as e:
            print(f'cannot save settings file: {e}')

    def load(self):
        """load settings from file. If file does not exist, use default settings."""
        settings_path = os.path.expanduser("~/.config/gomoku/settings.json")
        try:
            if not os.path.exists(settings_path):
                print('settings file not found, using default settings...')
                return
            with open(settings_path, 'r') as file:
                settings_file = json.load(file)
                self.set_fps(settings_file['max_framerate'])
                self.set_music(settings_file['music'])
                self.set_sound(settings_file['sound'])
                self.set_fullscreen(settings_file['fullscreen'])
                self.set_window_size(settings_file['window_size'][0], settings_file['window_size'][1])
                print('settings loaded')
        except Exception as e:
            print(f'error loading settings file: {e}')
            return

