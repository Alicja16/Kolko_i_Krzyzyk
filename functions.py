import random
import os
os.chdir(os.path.dirname(__file__))
import pygame
pygame.init()


scoreboard = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]


def change_player(current_player: str):
    if current_player == 'x':
        return 'o'
    return 'x'


def rect_board_making(M_W: int, M_H: int, C_W: int, C_H: int) -> list:
    rect_board = []
    for row in range(3):
        row_list = []
        for col in range(3):
            x = M_W + col * C_W
            y = M_H + row * C_H
            rect = pygame.Rect(x, y, C_W, C_H)
            row_list.append(rect)
        rect_board.append(row_list)
    return rect_board



def centers_board_making(M_W: int, M_H: int, C_W: int, C_H: int) -> list:
    centers_board = []
    for row in range(3):
        row_list = []
        for col in range(3):
            center_x = M_W + col * C_W + C_W // 2
            center_y = M_H + row * C_H + C_H // 2
            row_list.append((center_x, center_y))
        centers_board.append(row_list)
    return centers_board


def drawing_lines(M_W: int, M_H: int, C_W: int, C_H: int, screen_surface) -> None:
    #pygame.draw.line(surface, color, start_pos, end_pos, thickness)
    pygame.draw.line(screen_surface, (0,0,0), (M_W + C_W, M_H), (M_W + C_W, M_H + 3 * C_H), 3)
    pygame.draw.line(screen_surface, (0,0,0), (M_W + 2*C_W, M_H), (M_W + 2*C_W, M_H + 3 * C_H), 3)
    pygame.draw.line(screen_surface, (0,0,0), (M_W, M_H + C_H), (M_W + 3* C_W, M_H + C_H), 3)
    pygame.draw.line(screen_surface, (0,0,0), (M_W, M_H + 2*C_H), (M_W + 3* C_W, M_H + 2*C_H), 3)


def load_image(image_path: str, position: list, C_W: int, C_H: int) -> list:
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (round(C_W * 0.8), round(C_H * 0.8)))
    surface = image.convert_alpha()
    rect = surface.get_rect(center = position)
    return [image, surface, rect]


def print_image(img_list: list, screen_surface) -> list:
    image, surface, rect = img_list
    screen_surface.blit(surface, rect)
    pass


def move(mouse_pos: list, rect_board:list, centers_board: list, C_W: int, C_H: int, current_player: str) -> list:
    for row in range(3):
        for col in range(3):
            rect = rect_board[row][col]
            if rect.collidepoint(mouse_pos):
                if scoreboard[row][col] == "":
                    if current_player == 'x':
                        img = load_image(r"gallery\cross.png", centers_board[row][col], C_W, C_H)
                    else:
                        img = load_image(r"gallery\circle.png", centers_board[row][col], C_W, C_H)
                    scoreboard[row][col] = current_player
                    return img, current_player
    return None, current_player


def winning(current_player: str) -> bool:
    for i in scoreboard:
        if i.count(current_player) == 3:
            return True
    for i in range(3):
        if scoreboard[0][i] == scoreboard[1][i] == scoreboard[2][i] == current_player:
            return True
    
    if scoreboard[0][0] == scoreboard[1][1] == scoreboard[2][2] == current_player:
        return True
    if scoreboard[0][2] == scoreboard[1][1] == scoreboard[2][0] == current_player:
        return True
    return False


def text_glow(text, font, text_color, outline_color, screen, pos):
    base = font.render(text, True, text_color)
    outline = font.render(text, True, outline_color)
    x,y = pos

    for dx in range(-8, 8):
        for dy in range(-8, 0):
            screen.blit(outline, (x + dx, y + dy))
    screen.blit(base, (x, y))


def load_button(image_path: str, position: list, width: int, height: int) -> list:
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (width, height))
    surface = image.convert_alpha()
    rect = surface.get_rect(center = position)
    return [image, surface, rect]

def reset_score() -> None:
    global scoreboard
    scoreboard = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]


music_on = True
sound_on = True

def music_loop(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1) #zapętlone


def toggle_music():
    global music_on
    music_on = not music_on
    if music_on:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()

def is_music_on():
    return music_on


def click_sound_load(sound_file):
    global click_sound
    click_sound = pygame.mixer.Sound(sound_file)
    click_sound.set_volume(0.5)

def toggle_sound():
    global sound_on
    sound_on = not sound_on


def play_click_sound():
    if sound_on:
        click_sound.play()

def is_sound_on():
    return sound_on



