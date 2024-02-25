import pygame
from gomoku.game.screen.particle import stars_effect
from gomoku.game.engine import Engine, load_music, get_image, set_titlescreen
from gomoku.game.screen.components import mute_button, mute_action, maximize_button, maximize_action, get_gomoku_logo, get_1vs1_button, get_ai_button


def handle_events(engine, events_list) -> str | bool:
    for event in pygame.event.get():
        if event.type in [pygame.VIDEORESIZE]:
            if not engine.settings.get_fullscreen():
                engine.update_screen_size()
                return 'restart'
        elif event.type in [pygame.KEYDOWN, pygame.QUIT]:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                return 'quit'
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if events_list[0][1].collidepoint(event.pos):
                mute_action(engine)
            elif events_list[1][1].collidepoint(event.pos):
                maximize_action(engine)
                return 'restart'
            elif events_list[2][1].collidepoint(event.pos):
                engine.change_screen('game_1vs1')
                return 'game_1vs1'
    return True


def main_menu(engine: Engine):
    set_titlescreen('Gomoku - Main Menu')
    load_music('title_screen.mp3')
    while True:

        credit_text = engine.font.render('Developed by: nskiba and lfarina - ESC to exit', True, (255, 255, 255))
        logo, logo_rect = get_gomoku_logo(engine)
        button_1vs1 = get_1vs1_button(engine)
        button_ai = get_ai_button(engine)
        mute = mute_button(engine)
        maximize = maximize_button(engine)

        groups_particles = pygame.sprite.Group()
        events_list = [mute, maximize, button_1vs1, button_ai]
        running = True
        while running:
            is_mute = 1 if engine.settings.get_music() else 0
            result = handle_events(engine, events_list)
            if result == 'quit':
                engine.change_screen(None)
                return False
            elif result == 'restart':
                break
            engine.screen.fill((8, 26, 43))
            stars_effect(20, engine.get_window_size()[0], engine.get_window_size()[1], groups_particles)
            groups_particles.update()
            groups_particles.draw(engine.screen)
            engine.screen.blit(logo, logo_rect)
            engine.screen.blit(maximize[0], maximize[1])
            engine.screen.blit(mute[is_mute * 2], mute[is_mute * 2 + 1])
            engine.screen.blit(credit_text, (10, engine.get_window_size()[1] - credit_text.get_height() - 10))
            engine.screen.blit(button_1vs1[0], button_1vs1[1])
            engine.screen.blit(button_ai[0], button_ai[1])
            pygame.display.update()
            engine.clock.tick(engine.settings.get_fps())
