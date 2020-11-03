from sounds import *
from effects import *
from parameters import screenMode

class Button:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.inactiveColor = (13, 162, 58)
        self.activeColor = (23, 204, 58)
        self.drawEffects = False
        self.clearEffects = False
        self.rect_h = 10
        self.rect_w = w

    def draw(self, x, y, message, action = None, font_size = 30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if (x < mouse[0] < (x + self.w)) and (y < mouse[1] < y + self.h):
            if (click[0] == 1):
                pygame.mixer.Sound.play(buttonSound)
                pygame.time.delay(300) # временная задержка
                if (action is not None):
                    if (action == quit):
                        pygame.quit()
                        quit()
                    else: action()
                else: 
                    return True

        self.draw_beautiful_rect(mouse[0], mouse[1], x, y)
        printText(message = message, x = x+10, y = y+10, font_size = font_size)

    def draw_beautiful_rect(self, ms_x, ms_y, x, y):
        if (x <= ms_x <= (x + self.w)) or (y <= ms_y <= (y + self.h)):
            self.drawEffects = True

        if self.drawEffects:
            if (ms_x < x) or (ms_x > (x + self.w)) or (ms_y < y) or (ms_y > (y + self.h)):
                self.clearEffects = True
                self.drawEffects = False

            if (self.rect_h < self.h):
                self.rect_h += (self.h - 10) // 40

        if (self.clearEffects and not self.drawEffects):
            if (self.rect_h > 10):
                self.rect_h -= (self.h - 10) // 40
            else:
                self.clearEffects = False

        draw_y = y + self.h - self.rect_h
        pygame.draw.rect(screenMode, self.activeColor, (x, draw_y, self.rect_w, self.rect_h))
