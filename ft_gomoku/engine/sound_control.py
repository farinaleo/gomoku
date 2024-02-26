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


def play_sound(sound_file: str):
    """Play sound file.
    :param sound_file: sound file name.
    """
    path = os.path.join('ft_gomoku', 'assets', 'music', sound_file)
    pygame.mixer.Sound(path).play(1)


def stop_sound():
    """Stop sound file."""
    pygame.mixer.stop()
