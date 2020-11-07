import pygame

width, height = 800, 600 # размеры приложения

screen = pygame.display
screenMode = screen.set_mode((width, height)) # создаёт экран с размерами

clock = pygame.time.Clock()

mouseCounter = 0
need_draw_click = False

# параметры динозавра
dino_w = 60
dino_h = 100
dino_x = width // 3
dino_y = height - dino_h - 100

count = 0
away_y = 0

birdBullets = []