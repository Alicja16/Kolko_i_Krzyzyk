import functions
import os
import random
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


rect_board = functions.rect_board_making(MARGIN_W, MARGIN_H, CELL_WIDTH, CELL_HEIGHT)
centers_board = functions.centers_board_making(MARGIN_W, MARGIN_H, CELL_WIDTH, CELL_HEIGHT)

current_player = None
movement_counter = 0
state = "start" #play, game_over

while game_status:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game_status = False
        
        if state == "start":
            screen_surface.blit(background_image, (0,0))
            start_button = functions.load_button(r"gallery\start_button.png", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 300, 150)
            functions.print_image(start_button, screen_surface)

            current_player = random.choice(['x', 'o'])

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_button[2].collidepoint(mouse_pos):
                    state = "play"
                    screen_surface.blit(background_image, (0,0))
                    functions.drawing_lines(MARGIN_W, MARGIN_H, CELL_WIDTH, CELL_HEIGHT, screen_surface)

    
        elif state == "play":
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                img, current_player = functions.move(mouse_pos, rect_board, centers_board, CELL_WIDTH, CELL_HEIGHT, current_player)
                if img is not None:
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

        
        elif state == "game_over":
            font = pygame.font.SysFont('comicsansms', 72, bold=True)
            text_width, text_height = font.size(text)
            pos = (SCREEN_WIDTH // 2 - text_width // 2, SCREEN_HEIGHT // 2 - text_height // 2)
            functions.text_glow(text, font, (255, 255, 255), (128, 0, 128), screen_surface, pos)

            restart_button = functions.load_button(r"gallery\restart_button.png", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100), 200, 60)
            functions.print_image(restart_button, screen_surface)

            return_button = functions.load_button(r"gallery\return_button.png", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200), 180, 60)
            functions.print_image(return_button, screen_surface)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if restart_button[2].collidepoint(mouse_pos):
                    functions.reset_score()
                    state = "play"
                    movement_counter = 0
                    current_player = random.choice(['x', 'o'])
                    screen_surface.blit(background_image, (0,0))
                    functions.drawing_lines(MARGIN_W, MARGIN_H, CELL_WIDTH, CELL_HEIGHT, screen_surface)
                    
                elif return_button[2].collidepoint(mouse_pos):
                    functions.reset_score()
                    state = "start"
                    movement_counter = 0


        pygame.display.update()
        clock.tick(FPS)
    pass

pygame.quit()
quit()