from gomoku import SettingsStruct
from gomoku import Engine
import pygame
from gomoku import main_menu


def main():
	engine = Engine()
	engine.load_settings()
	engine.save_settings()
	while True:
		if engine.get_current_screen() == 'main_menu':
			main_menu(engine)
		if engine.get_current_screen() == 'game':
			pass
		if engine.get_current_screen() is None:
			break
	print('Exiting')
	pygame.quit()


if __name__ == '__main__':
	main()
