import os
import pygame


def load_music(music_file: str, repeat: int = -1):
    """Load and play music file.
    :param music_file: music file name.
    :param repeat: how many times to repeat. -1 for infinite.
    """
    path = os.path.join('ft_gomoku', 'assets', 'music', music_file)
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(repeat)
