import functions
import os
import random
import threading
os.chdir(os.path.dirname(__file__))
import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

MARGIN_W, MARGIN_H = SCREEN_WIDTH * 0.125, SCREEN_HEIGHT * 0.125
CELL_WIDTH, CELL_HEIGHT = SCREEN_WIDTH * 0.25, SCREEN_HEIGHT * 0.25


screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("⭕／❌")

clock = pygame.time.Clock()
game_status = True
background_image = pygame.image.load(r"gallery\background.png").convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

background_music = r"sounds\background_music.wav"
click_sound = r"sounds\click_sound.wav"
functions.click_sound_load(click_sound)


rect_board = functions.rect_board_making(MARGIN_W, MARGIN_H, CELL_WIDTH, CELL_HEIGHT)
centers_board = functions.centers_board_making(MARGIN_W, MARGIN_H, CELL_WIDTH, CELL_HEIGHT)

current_player = None
movement_counter = 0
state = "start" #play, game_over

threading.Thread(target=functions.music_loop, args=(background_music,), daemon=True).start()

while game_status:
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game_status = False
        
        if state == "start":
            screen_surface.blit(background_image, (0,0))

            start_text = "Kółko i Krzyżyk"
            font = pygame.font.SysFont('comicsansms', 86, bold=True)
            text_width, text_height = font.size(start_text)
            pos = ((SCREEN_WIDTH // 2 - text_width // 2), (SCREEN_HEIGHT // 2 - text_height // 2) * (4/5))
            functions.text_glow(start_text, font, (255, 255, 255), (204, 153, 255), screen_surface, pos)

            start_button = functions.load_button(r"gallery\start_button.png", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 * (3/2)), 200, 100)
            functions.print_image(start_button, screen_surface)

            music_path = r"gallery\music_on.png" if functions.is_music_on() else r"gallery\music_off.png"
            music_button = functions.load_button(music_path, (SCREEN_WIDTH - 40, 30), 50, 50)
            functions.print_image(music_button, screen_surface)

            sound_path = r"gallery\sound_on.png" if functions.is_sound_on() else r"gallery\sound_off.png"
            sound_button = functions.load_button(sound_path, (SCREEN_WIDTH - 100, 30), 50, 50)
            functions.print_image(sound_button, screen_surface)

            current_player = random.choice(['x', 'o'])

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_button[2].collidepoint(mouse_pos):
                    functions.play_click_sound()
                    state = "play"
                    screen_surface.blit(background_image, (0,0))
                    functions.drawing_lines(MARGIN_W, MARGIN_H, CELL_WIDTH, CELL_HEIGHT, screen_surface)
                
                if music_button[2].collidepoint(mouse_pos):
                    functions.play_click_sound()
                    functions.toggle_music()
                    
                
                if sound_button[2].collidepoint(mouse_pos):
                    functions.play_click_sound()
                    functions.toggle_sound()

    
        elif state == "play":
            music_path = r"gallery\music_on.png" if functions.is_music_on() else r"gallery\music_off.png"
            music_button = functions.load_button(music_path, (SCREEN_WIDTH - 40, 30), 50, 50)
            functions.print_image(music_button, screen_surface)

            sound_path = r"gallery\sound_on.png" if functions.is_sound_on() else r"gallery\sound_off.png"
            sound_button = functions.load_button(sound_path, (SCREEN_WIDTH - 100, 30), 50, 50)
            functions.print_image(sound_button, screen_surface)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                img, current_player = functions.move(mouse_pos, rect_board, centers_board, CELL_WIDTH, CELL_HEIGHT, current_player)
                if img is not None:
                    functions.play_click_sound()
                    functions.print_image(img, screen_surface)
                    movement_counter = movement_counter + 1
                    if functions.winning(current_player):
                        state = "game_over"
                        text = f"WINNER {current_player.upper()}!"
                    elif movement_counter >= 9:
                        state = "game_over"
                        text = f"DRAW!"
                    else:
                        current_player = functions.change_player(current_player)

                if music_button[2].collidepoint(mouse_pos):
                    functions.play_click_sound()
                    functions.toggle_music()
                    
                
                if sound_button[2].collidepoint(mouse_pos):
                    functions.play_click_sound()
                    functions.toggle_sound()
                    

        
        elif state == "game_over":
            music_path = r"gallery\music_on.png" if functions.is_music_on() else r"gallery\music_off.png"
            music_button = functions.load_button(music_path, (SCREEN_WIDTH - 40, 30), 50, 50)
            functions.print_image(music_button, screen_surface)

            sound_path = r"gallery\sound_on.png" if functions.is_sound_on() else r"gallery\sound_off.png"
            sound_button = functions.load_button(sound_path, (SCREEN_WIDTH - 100, 30), 50, 50)
            functions.print_image(sound_button, screen_surface)

            font = pygame.font.SysFont('comicsansms', 72, bold=True)
            text_width, text_height = font.size(text)
            pos = ((SCREEN_WIDTH // 2 - text_width // 2), (SCREEN_HEIGHT // 2 - text_height // 2) * (2/3))
            functions.text_glow(text, font, (255, 255, 255), (204, 153, 255), screen_surface, pos)

            restart_button = functions.load_button(r"gallery\restart_button.png", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10), 200, 60)
            functions.print_image(restart_button, screen_surface)

            return_button = functions.load_button(r"gallery\return_button.png", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100), 180, 60)
            functions.print_image(return_button, screen_surface)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if restart_button[2].collidepoint(mouse_pos):
                    functions.play_click_sound()
                    functions.reset_score()
                    state = "play"
                    movement_counter = 0
                    current_player = random.choice(['x', 'o'])
                    screen_surface.blit(background_image, (0,0))
                    functions.drawing_lines(MARGIN_W, MARGIN_H, CELL_WIDTH, CELL_HEIGHT, screen_surface)
                    
                elif return_button[2].collidepoint(mouse_pos):
                    functions.play_click_sound()
                    functions.reset_score()
                    state = "start"
                    movement_counter = 0
                
                if music_button[2].collidepoint(mouse_pos):
                    functions.play_click_sound()
                    functions.toggle_music()
                    
                
                if sound_button[2].collidepoint(mouse_pos):
                    functions.play_click_sound()
                    functions.toggle_sound()


        pygame.display.update()
        clock.tick(FPS)
    pass

pygame.quit()
quit()