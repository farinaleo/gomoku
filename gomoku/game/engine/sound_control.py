import os
import pygame


def load_music(music_file: str, repeat: int = -1):
    path = os.path.join('gomoku', 'assets', 'music', music_file)
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(repeat)
