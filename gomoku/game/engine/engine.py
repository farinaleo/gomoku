from dataclasses import dataclass, field
from gomoku import SettingsStruct
import pygame


@dataclass
class Engine:

    def __init__(self):
        pygame.init()
        self.settings = None
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.current_screen = 'main_menu'

    def load_settings(self):
        self.settings = SettingsStruct()
        self.settings.load()
        self.update_settings()
        self.settings.print() # Debug only

    def update_settings(self):
        self.screen = pygame.display.set_mode(self.settings.get_window_size(), pygame.FULLSCREEN if self.settings.get_fullscreen() else 0)

    def save_settings(self):
        self.settings.save()

    def change_screen(self, screen):
        self.current_screen = screen

    def get_current_screen(self):
        return self.current_screen


