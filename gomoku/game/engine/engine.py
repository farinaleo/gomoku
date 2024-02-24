from dataclasses import dataclass, field
from gomoku import SettingsStruct
import pygame
import os


def init_icon():
    try:
        image_path = os.path.join('gomoku', 'assets', 'img', 'logo_favicon.png')
        favicon = pygame.image.load(image_path)
        pygame.display.set_icon(favicon)
    except Exception as e:
        print(f'load favicon error: {e}')


@dataclass
class Engine:

    def __init__(self):
        pygame.init()
        self.settings = None
        self.screen = None
        self.clock = pygame.time.Clock()
        self.running = True
        self.current_screen = 'main_menu'
        init_icon()

    def load_settings(self):
        self.settings = SettingsStruct()
        self.settings.load()
        self.update_settings()
        if not self.settings.get_music():
            pygame.mixer.music.set_volume(0)
        self.settings.print() # Debug only

    def update_settings(self):
        self.screen = pygame.display.set_mode(self.settings.get_window_size(), pygame.FULLSCREEN if self.settings.get_fullscreen() else 0)

    def save_settings(self):
        self.settings.save()

    def change_screen(self, screen):
        self.current_screen = screen

    def get_current_screen(self):
        return self.current_screen

    def get_ticks(self):
        return pygame.time.get_ticks()# a verifi

    def mute(self):
        self.settings.set_music(not self.settings.get_music())

    def get_music(self):
        return self.settings.get_music()

