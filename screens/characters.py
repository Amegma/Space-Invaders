import os
import pygame

from .background import slow_bg_obj
from models.icon_button import IconButton
from models.controls import audio_cfg, display_cfg

from constants import WIDTH, \
    CANVAS, \
    center_x, \
    FPS, \
    edit_undo_font, \
    GO_BACK_IMAGE, \
    CHARACTERS_IMAGE, \
    CHARACTERS_IMAGE_2, \
    BOSS_SHIP,\
    PLAYER_SPACE_SHIP,\
    EASY_SPACE_SHIP,\
    MEDIUM_SPACE_SHIP,\
    HARD_SPACE_SHIP,\
    framespersec


def characters():
    background_width = slow_bg_obj.rectBGimg.width
    starting_x = center_x - background_width//2

    characters_title_font = pygame.font.Font(edit_undo_font, 50)

    go_back_btn = IconButton(GO_BACK_IMAGE, (starting_x + 30, 30))

    run = True
    while run:
        slow_bg_obj.update()
        slow_bg_obj.render(CANVAS)

        characters_title_label = characters_title_font.render(
            'Characters', 1, (0, 255, 255))
        CANVAS.blit(characters_title_label, (center_x -
                                             characters_title_label.get_width()//2, 130))
        CANVAS.blit(CHARACTERS_IMAGE, (center_x -
                                       CHARACTERS_IMAGE.get_width()//2 - 170, 120))
        CANVAS.blit(CHARACTERS_IMAGE_2, (center_x -
                                         CHARACTERS_IMAGE.get_width()//2 + 170, 129))

        CANVAS.blit(PLAYER_SPACE_SHIP, (center_x -
                    PLAYER_SPACE_SHIP.get_width()//2, 310))
        CANVAS.blit(EASY_SPACE_SHIP, (center_x -
                    EASY_SPACE_SHIP.get_width()//2, 310))
        CANVAS.blit(MEDIUM_SPACE_SHIP, (center_x -
                    MEDIUM_SPACE_SHIP.get_width()//2, 310))
        CANVAS.blit(HARD_SPACE_SHIP, (center_x -
                    HARD_SPACE_SHIP.get_width()//2, 310))
        CANVAS.blit(BOSS_SHIP, (center_x-BOSS_SHIP.get_width()//2, 310))

        go_back_btn.draw()

        audio_cfg.display_volume(CANVAS)
        framespersec.tick(FPS)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_m:
                    audio_cfg.toggle_mute()
                if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                    audio_cfg.inc_volume(5)
                if event.key == pygame.K_MINUS:
                    audio_cfg.dec_volume(5)
                if event.key == pygame.K_f:
                    display_cfg.toggle_full_screen()
                if event.key == pygame.K_BACKSPACE:
                    run = False

            # Mouse click events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if go_back_btn.isOver():
                        run = False

            # Mouse hover events
            if event.type == pygame.MOUSEMOTION:
                if go_back_btn.isOver():
                    go_back_btn.outline = "onover"
                else:
                    go_back_btn.outline = "default"

            # keys = pygame.key.get_pressed()
            # if keys[pygame.K_BACKSPACE]:
            #     run = False