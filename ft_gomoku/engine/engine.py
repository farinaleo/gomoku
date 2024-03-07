from dataclasses import dataclass, field
from ft_gomoku.data_structure.SettingsStruct import SettingsStruct
import pygame
import os


def set_titlescreen(title):
    pygame.display.set_caption(title)


@dataclass
class Engine:

    def __init__(self):
        self.settings = None
        self.screen = None
        self.clock = None
        self.running = False
        self.current_screen = None
        self.font = None
        self.favicon = None
        self.window_size = None
        self.player_turn = None

    def init_engine(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.current_screen = 'main_menu'
        self.init_font()
        self.init_icon()
        self.load_settings()
        self.set_running(True)

    def load_settings(self):
        self.settings = SettingsStruct()
        self.settings.load()
        self.window_size = self.settings.get_window_size()
        self.screen = pygame.display.set_mode(self.get_window_size(), pygame.FULLSCREEN if self.settings.get_fullscreen() else 0)
        if not self.settings.get_music():
            pygame.mixer.music.set_volume(0)
        self.settings.print() # TODO: remove this line

    def change_screen(self, screen):
        """Change the current screen to the one passed as argument.
        :param screen: str
        """
        self.current_screen = screen

    def mute(self):
        """mute the music. If the music is already muted, it will be unmuted."""
        self.settings.set_music(not self.settings.get_music())
        pygame.mixer.music.set_volume(int(self.settings.get_music()))

    def maximize(self):
        """maximize the window. If the window is already maximized, it will be minimized."""
        self.settings.set_fullscreen(not self.settings.get_fullscreen())
        self.window_size = self.settings.get_window_size()
        self.screen = pygame.display.set_mode(self.settings.get_window_size(),
                                              pygame.FULLSCREEN if self.settings.get_fullscreen() else 0)

    def init_font(self):
        """Initialize the font"""
        pygame.font.init()
        self.font = pygame.font.Font('ft_gomoku/assets/fonts/Roboto-Bold.ttf', 20) # TODO: dynamic size

    def init_icon(self):
        """Initialize the icon of the window"""
        image_path = os.path.join('ft_gomoku', 'assets', 'img', 'logo_favicon.png')
        self.favicon = pygame.image.load(image_path)
        pygame.display.set_icon(self.favicon)

    def get_music(self):
        return self.settings.get_music()

    def set_running(self, running):
        self.running = running

    def get_running(self):
        return self.running

    def get_window_size(self):
        return self.window_size

    def get_current_screen(self):
        return self.current_screen

    def save_settings(self):
        if self.settings is not None:
            self.settings.save()
