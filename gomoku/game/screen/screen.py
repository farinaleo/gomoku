from random import choice, uniform, randint

import pygame
from gomoku.game.engine import Engine
from gomoku.game.engine import load_music, get_image
from gomoku.game.screen.particle import stars_effect
from gomoku.game.screen.components import mute_button

def main_menu(engine: Engine):
	""" Main menu screen """

	# Set title screen and music
	pygame.display.set_caption('Gomoku - Title screen')
	load_music('title_screen.mp3')

	# Load logo
	logo = get_image('logo-game.png', engine.settings.get_width() // 3, engine.settings.get_height() // 3)
	logo_rect = logo.get_rect()
	logo_rect.center = (engine.settings.get_width() // 2, logo.get_height() // 2)

	# Mute button
	mute = mute_button(engine)
	print(mute)

	# While loop
	running = True
	group_particles = pygame.sprite.Group()
	while running:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				running = False
			if event.type == pygame.QUIT:
				running = False
		engine.screen.fill((8, 26, 43))
		engine.screen.blit(logo, logo_rect)
		is_mute = 0 if engine.settings.get_music() else 2
		engine.screen.blit(mute[0 + is_mute], mute[1 + is_mute])
		stars_effect(20, engine.settings.get_width(), engine.settings.get_height(), group_particles)
		group_particles.draw(engine.screen)
		group_particles.update()
		pygame.display.update()
		engine.clock.tick(engine.settings.get_fps())
	engine.change_screen(None)
