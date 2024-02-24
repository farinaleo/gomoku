from random import choice, uniform, randint

import pygame
from gomoku.game.engine import Engine
from gomoku.data_structure import SettingsStruct
from gomoku.game.engine import load_music
from gomoku.game.screen.particle import stars_effect


def main_menu(engine: Engine):
	""" Main menu screen """
	pygame.display.set_caption('Gomoku - Title screen')
	engine.screen.fill((8, 26, 43))
	pygame.display.update()
	load_music('title_screen.mp3')
	running = True
	group_particles = pygame.sprite.Group()
	while running:
		dt = engine.clock.tick(engine.settings.get_fps()) / 1000
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		stars_effect(20, engine.settings.get_width(), engine.settings.get_height(), group_particles)

		#display
		engine.screen.fill((8, 26, 43))
		group_particles.draw(engine.screen)


		#update
		group_particles.update(dt)
		pygame.display.update()

	pygame.quit()
