from ft_gomoku import Engine
import pygame
from ft_gomoku import main_menu, game_screen, tutorial_screen


def main():
	engine = Engine()
	engine.init_engine()
	while engine.get_running():
		if engine.get_current_screen() == 'main_menu':
			main_menu(engine)
		if engine.get_current_screen() == '1vs1':
			game_screen(engine, False)
		if engine.get_current_screen() == 'ai':
			game_screen(engine, True)
		if engine.get_current_screen() == 'tutorial':
			tutorial_screen(engine)
		if engine.get_current_screen() is None:
			break
	print('Exiting')
	engine.save_settings()
	pygame.quit()


if __name__ == '__main__':
	main()
