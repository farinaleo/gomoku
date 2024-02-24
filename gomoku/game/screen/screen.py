from random import choice, uniform, randint

import pygame
from gomoku.game.engine import Engine
from gomoku.game.engine import load_music, get_image
from gomoku.game.screen.particle import stars_effect
from gomoku.game.screen.components import mute_button, button_action

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
	is_mute = 1 if engine.settings.get_music() else 0
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
			if event.type == pygame.MOUSEBUTTONDOWN:
				if mute[1].collidepoint(event.pos):
					is_mute = button_action(engine)
		engine.screen.fill((8, 26, 43))
		engine.screen.blit(logo, logo_rect)

		engine.screen.blit(mute[is_mute * 2], mute[is_mute * 2 + 1])
		stars_effect(20, engine.settings.get_width(), engine.settings.get_height(), group_particles)
		group_particles.draw(engine.screen)
		group_particles.update()
		pygame.display.update()
		engine.clock.tick(engine.settings.get_fps())
	engine.change_screen(None)
	# IL FAUT : voir pour mute et unmute. comment faire la gestion de mute et unmute. faire le bouton clickable pour mute et unmute.
	# IL FAUT : voir pour mute et unmute. comment faire la gestion de mute et unmute. faire le bouton clickable pour mute et unmute.
	# IL FAUT : voir pour mute et unmute. comment faire la gestion de mute et unmute. faire le bouton clickable pour mute et unmute.
	# IL FAUT : voir pour mute et unmute. comment faire la gestion de mute et unmute. faire le bouton clickable pour mute et unmute.
	# IL FAUT : voir pour mute et unmute. comment faire la gestion de mute et unmute. faire le bouton clickable pour mute et unmute.
	# IL FAUT : voir pour mute et unmute. comment faire la gestion de mute et unmute. faire le bouton clickable pour mute et unmute.
	# IL FAUT : voir pour mute et unmute. comment faire la gestion de mute et unmute. faire le bouton clickable pour mute et unmute.
	# IL FAUT : voir pour mute et unmute. comment faire la gestion de mute et unmute. faire le bouton clickable pour mute et unmute.
	# IL FAUT : voir pour mute et unmute. comment faire la gestion de mute et unmute. faire le bouton clickable pour mute et unmute.
	# IL FAUT : voir pour mute et unmute. comment faire la gestion de mute et unmute. faire le bouton clickable pour mute et unmute.
	# IL FAUT : voir pour mute et unmute. comment faire la gestion de mute et unmute. faire le bouton clickable pour mute et unmute.
	# IL FAUT : voir pour mute et unmute. comment faire la gestion de mute et unmute. faire le bouton clickable pour mute et unmute.
