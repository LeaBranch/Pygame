import parameters as p
import pygame
from images import light


need_input = False
input_text = '|'
input_tick = 30


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

def get_input():
    global need_input, input_text, input_tick

    input_rect = pygame.Rect(20, 400, 250, 70)

    pygame.draw.rect(p.screenMode, (255, 255, 255), input_rect)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # keys = pygame.key.get_pressed()


    if (input_rect.collidepoint(mouse[0], mouse[1]) and click[0]):
        need_input = True

    if (need_input):
        for event in pygame.event.get():
            if (need_input and event.type == pygame.KEYDOWN):
                input_text = input_text.replace("|", '')
                input_tick = 30

                if (event.type == pygame.K_RETURN):
                    need_input = False
                    input_text = ''
                elif (event.type == pygame.K_BACKSPACE):
                    input_text = input_text[:-1]
                else:
                    if (len(input_text) < 10):
                        input_text += event.unicode
                input_text += "|"

    if (len(input_text)):
        printText(message = input_text, x = input_rect.x+10, y = input_rect.y+10, font_size = 50)

    input_tick -= 1
    if (input_tick == 0):
        input_text = input_text[:-1]
    if (input_tick == -30):
        input_text += "|"
        input_tick = 30