import pygame
from pygame.rect import RectType
from ft_gomoku.engine import Engine
from pygame import Surface, SurfaceType, Rect


def get_gomoku_logo(engine: Engine) -> list[Surface | SurfaceType | Rect | RectType]:
	"""Return gomoku logo
	:param engine: Engine
	"""
	img_width = engine.get_window_size()[0] // 3
	img_height = engine.get_window_size()[1] // 3
	image = pygame.image.load('ft_gomoku/assets/img/logo-game.png')
	image = pygame.transform.scale(image, (img_width, img_height))
	image_rect = image.get_rect(center=(engine.get_window_size()[0] // 2, engine.get_window_size()[1] // 4))
	return [image, image_rect]

