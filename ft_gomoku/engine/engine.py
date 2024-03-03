from dataclasses import dataclass, field
from ft_gomoku import SettingsStruct
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
        self.player_turn = 1

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
        self.update_settings()
        if not self.settings.get_music():
            pygame.mixer.music.set_volume(0)
        self.settings.print() # Debug only

    def update_settings(self): # a voir
        self.screen = pygame.display.set_mode(self.get_window_size(),
                                              pygame.FULLSCREEN if self.settings.get_fullscreen() else pygame.RESIZABLE)

    def save_settings(self):
        if self.settings is not None:
            self.settings.save()

    def change_screen(self, screen):
        self.current_screen = screen

    def get_current_screen(self):
        return self.current_screen

    def get_ticks(self):
        return pygame.time.get_ticks()# a verifi

    def mute(self):
        self.settings.set_music(not self.settings.get_music())
        pygame.mixer.music.set_volume(int(self.settings.get_music()))

    def maximize(self):
        self.settings.set_fullscreen(not self.settings.get_fullscreen())
        self.window_size = self.settings.get_window_size()
        self.screen = pygame.display.set_mode(self.settings.get_window_size(),
                                              pygame.FULLSCREEN if self.settings.get_fullscreen() else pygame.RESIZABLE)

    def get_music(self):
        return self.settings.get_music()

    def init_font(self):
        """Initialize the font"""
        pygame.font.init()
        self.font = pygame.font.Font('ft_gomoku/assets/fonts/Roboto-Bold.ttf', 20)

    def init_icon(self):
        """Initialize the icon of the window"""
        image_path = os.path.join('ft_gomoku', 'assets', 'img', 'logo_favicon.png')
        self.favicon = pygame.image.load(image_path)
        pygame.display.set_icon(self.favicon)

    def set_running(self, running):
        self.running = running

    def get_running(self):
        return self.running

    def get_window_size(self):
        return self.window_size

    def update_screen_size(self):
        window_size = pygame.display.get_window_size()
        size_ratio = window_size[0] / window_size[1]
        if size_ratio > 1.3 and (window_size[0] > 350 and window_size[1] > 350):
            self.window_size = (pygame.display.get_window_size()[0], pygame.display.get_window_size()[1])

