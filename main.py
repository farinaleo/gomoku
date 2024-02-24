from gomoku import SettingsStruct
from gomoku import Engine
import pygame
from gomoku import main_menu


def main():
	engine = Engine()
	engine.load_settings()
	engine.save_settings()
	main_menu(engine)
	pygame.quit()


if __name__ == '__main__':
	main()
