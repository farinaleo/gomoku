from dataclasses import dataclass, field


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
    __windows_size: [int, int] = field(default=(1280, 720))

    def print(self):
        """print representation of the SettingsStruct. Debug only"""
        print('SettingsStruct contain :')
        print(f'fps: {self.__fps}, music: {self.__music}, sound: {self.__sound}, fullscreen: {self.__fullscreen}, size: {self.__windows_size}')

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

    def get_windows_size(self) -> [int, int]:
        return self.__windows_size

    def set_windows_size(self, width: int, height: int):
        self.__windows_size = [width, height]

