import parameters as p
import pygame
from images import light

def printText(message, x, y, font_color = (0, 0, 0), font_type = "./assets/fonts/PingPong.ttf", font_size = 30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    p.screenMode.blit(text, (x, y))

def draw_mouse():
    global mouseCounter, need_draw_click
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    mouseSize = [10, 12, 16, 20, 28, 34, 40, 45, 48, 54, 58]

    if (click[0] or click[1]):
        p.need_draw_click = True

    if p.need_draw_click:
        draw_x = mouse[0] - mouseSize[p.mouseCounter // 2]
        draw_y = mouse[1] - mouseSize[p.mouseCounter // 2]

        p.screenMode.blit(light[p.mouseCounter], (draw_x, draw_y))
        p.mouseCounter += 1

        if (p.mouseCounter == 10):
            p.mouseCounter = 0
            p.need_draw_click = False