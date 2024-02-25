from gomoku import SettingsStruct
from gomoku import Engine
import pygame
from gomoku import main_menu


def main():
	engine = Engine()
	engine.init_engine()
	while engine.get_running():
		if engine.get_current_screen() == 'main_menu':
			main_menu(engine)
		if engine.get_current_screen() == 'game':
			pass
		if engine.get_current_screen() is None:
			break
	print('Exiting')
	engine.save_settings()
	pygame.quit()


if __name__ == '__main__':
	main()
