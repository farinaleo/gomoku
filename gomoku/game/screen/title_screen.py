import pygame
from gomoku.game.screen.particle import stars_effect
from gomoku.game.engine import Engine, load_music, get_image
from gomoku.game.screen.components import mute_button, mute_action, maximize_button, maximize_action


def create_button(image_path, engine, scale_width, scale_height, center_position):
    button_image = get_image(image_path, engine.settings.get_width() // scale_width, engine.settings.get_height() // scale_height)
    button_rect = button_image.get_rect()
    button_rect.center = center_position
    return button_image, button_rect


def handle_events(engine, mute, maximize, is_mute):
    for event in pygame.event.get():
        if event.type in [pygame.KEYDOWN, pygame.QUIT]:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                return False, is_mute
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mute[1].collidepoint(event.pos):
                is_mute = mute_action(engine)
            elif maximize[1].collidepoint(event.pos):
                maximize_action(engine)
    return True, is_mute


def main_menu(engine: Engine):
    pygame.display.set_caption('Gomoku - Title screen')
    load_music('title_screen.mp3')

    pygame.font.init()
    font = pygame.font.Font('gomoku/assets/fonts/Roboto-Bold.ttf', 20)
    credit_text = font.render('Developed by: nskiba and lfarina - ESC to exit', True, (255, 255, 255))

    logo, logo_rect = get_image('logo-game.png', engine.settings.get_width() // 3, engine.settings.get_height() // 3), get_image('logo-game.png', engine.settings.get_width() // 3, engine.settings.get_height() // 3).get_rect(center=(engine.settings.get_width() // 2, engine.settings.get_height() // 4))

    button_1vs1 = create_button('button_1vs1.png', engine, 4, 9, (engine.settings.get_width() // 2, engine.settings.get_height() // 2))
    button_ai = create_button('button_ai.png', engine, 4, 9, (engine.settings.get_width() // 2, engine.settings.get_height() // 2 + (engine.settings.get_width() - engine.settings.get_height()) / 5))

    mute = mute_button(engine)
    is_mute = 1 if engine.settings.get_music() else 0
    maximize = maximize_button(engine)

    groups_particles = pygame.sprite.Group()
    running = True
    while running:
        running, is_mute = handle_events(engine, mute, maximize, is_mute)

        engine.screen.fill((8, 26, 43))
        engine.screen.blit(logo, logo_rect)
        engine.screen.blit(maximize[0], maximize[1])
        engine.screen.blit(mute[is_mute * 2], mute[is_mute * 2 + 1])
        engine.screen.blit(credit_text, (10, engine.settings.get_height() - credit_text.get_height() - 10))
        engine.screen.blit(button_1vs1[0], button_1vs1[1])
        engine.screen.blit(button_ai[0], button_ai[1])
        stars_effect(20, engine.settings.get_width(), engine.settings.get_height(), groups_particles)
        groups_particles.draw(engine.screen)
        pygame.display.update()
        groups_particles.update()
        engine.clock.tick(engine.settings.get_fps())

    engine.change_screen(None)
