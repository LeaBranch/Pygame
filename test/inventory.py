import pygame

from parameters import screenMode
from effects import printText

pygame.init()

class Resourse:
    def __init__(self, name, image_path):
        self.name = name
        self.amount = 0
        self.image = pygame.image.load(image_path)

class Inventory:
    def __init__(self):
        self.resourse = {
        "coal": Resourse("coal", "./assets/textures/Coal.png"),
        "emerald": Resourse("emerald", "./assets/textures/Emerald.png"),
        "ruby": Resourse("ruby", "./assets/textures/Ruby.png")
        }
        self.inventory_panel = [None] * 4
        self.whole_invntry = [None] * 8

    def getAmount(self, name):
        try:
            return self.resourse[name].amount
        except KeyError:
            return -1

    def increase(self, name):
        try:
            self.resourse[name].amount +=1
            self.update()
            # print(self.whole_invntry)
        except KeyError:
            print("Error increading!")

    def update(self):
        for name, resourse in self.resourse.items():
            if (resourse.amount != 0) and (resourse not in self.whole_invntry):
                self.whole_invntry.insert(self.whole_invntry.index(None), resourse)
                self.whole_invntry.remove(None)

    def draw(self):
        x = 35
        y = 75
        side = 80
        step = 100

        pygame.draw.rect(screenMode, (182, 195, 206), (x-20, y-20, 420, 220))

        for cell in self.whole_invntry:
            pygame.draw.rect(screenMode, (200, 215, 227), (x, y, side, side))
            
            if (cell is not None):
                screenMode.blit(cell.image, (x + 15, y + 5))
                printText("x " + str(cell.amount), x+30, y+60, font_size = 15)

            x += step

            if (x > 350):
                x = 35
                y += 100

    def draw_panel(self):
        x = 200
        y = 510
        side = 80
        step = 100

        for cell in self.inventory_panel:
            pygame.draw.rect(screenMode, (200, 215, 227), (x, y, side, side))
            
            if (cell is not None):
                screenMode.blit(cell.image, (x + 15, y + 5))
                printText("x " + str(cell.amount), x+30, y+60, font_size = 15)

            x += step


inventory = Inventory()