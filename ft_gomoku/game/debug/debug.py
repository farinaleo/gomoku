import pygame

from ft_gomoku.engine import Engine
from ft_gomoku.data_structure.GameStruct import GameStruct
from ft_gomoku.data_structure.DebuggerStruct import DebuggerStruct


def debug_screen(engine: Engine, game_engine: GameStruct, debug_struct: DebuggerStruct):
    debug_struct.update_settings(engine, game_engine)
    debug_struct.update_ram_info()
    dict_debug = debug_struct.get_all_game_info()
    window_size = engine.get_window_size()
    image_bg = pygame.Surface((window_size[0], window_size[1]))
    image_text = pygame.Surface((window_size[0], window_size[1])).convert_alpha()
    image_text.fill((0, 0, 0, 0))
    image_bg.fill((0, 0, 0))
    image_bg.set_alpha(10)
    for i, (key, value) in enumerate(dict_debug.items()):
        if key != 'board_grid':
            font = pygame.font.Font(None, 24)
            text = font.render(f"{key} : {value}", True, (255, 255, 255))
            text_rect = text.get_rect(topleft=(10, 10 + i * 30))
            image_text.blit(text, text_rect)
    engine.screen.blit(image_bg, (0, 0))
    engine.screen.blit(image_text, (0, 0))
    pygame.display.flip()
