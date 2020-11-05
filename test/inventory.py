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
        self.whole_inventory = [None] * 8

        self.start_cell = 0
        self.end_cell = 0

    def getAmount(self, name):
        try:
            return self.resourse[name].amount
        except KeyError:
            return -1

    def increase(self, name):
        try:
            self.resourse[name].amount +=1
            self.update()
            # print(self.whole_inventory)
        except KeyError:
            print("Error increading!")

    def update(self):
        for name, resourse in self.resourse.items():
            if (resourse.amount != 0) and (resourse not in self.whole_inventory) and (resourse not in self.inventory_panel):
                self.whole_inventory.insert(self.whole_inventory.index(None), resourse)
                self.whole_inventory.remove(None)

    def draw(self):
        x = 35
        y = 75
        side = 80
        step = 100

        pygame.draw.rect(screenMode, (182, 195, 206), (x-20, y-20, 420, 220))

        for cell in self.whole_inventory:
            pygame.draw.rect(screenMode, (200, 215, 227), (x, y, side, side))
            
            if (cell is not None):
                screenMode.blit(cell.image, (x + 15, y + 5))
                printText("x " + str(cell.amount), x+30, y+60, font_size = 15)

            x += step

            if (x > 350):
                x = 35
                y += step

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

    def set_start_cell(self, ms_x, ms_y):
        start_x = 35
        start_y = 75
        step = 100
        side = 80

        for y in range(0, 2):
            for x in range(0, 4):
                cell_x = start_x + x * step
                cell_y = start_y + y * step

                if (cell_x <= ms_x <= (cell_x + side)) and (cell_y <= ms_y <= (cell_y + side)):
                    self.start_cell = y * 4 + x
                    return

        start_x = 200
        start_y = 510

        for x in range(0, 4):
            cell_x = start_x + x * step
            cell_y = start_y

            if (cell_x <= ms_x <= (cell_x + side)) and (cell_y <= ms_y <= (cell_y + side)):
                self.start_cell = 8 + x
                self.swap_cells()
                return

    def set_end_cell(self, ms_x, ms_y):
        start_x = 35
        start_y = 75
        step = 100
        side = 80

        for y in range(0, 2):
            for x in range(0, 4):
                cell_x = start_x + x * step
                cell_y = start_y + y * step

                if (cell_x <= ms_x <= (cell_x + side)) and (cell_y <= ms_y <= (cell_y + side)):
                    self.end_cell = y * 4 + x
                    self.swap_cells()
                    return

        start_x = 200
        start_y = 510

        for x in range(0, 4):
            cell_x = start_x + x * step
            cell_y = start_y

            if (cell_x <= ms_x <= (cell_x + side)) and (cell_y <= ms_y <= (cell_y + side)):
                self.end_cell = 8 + x
                self.swap_cells()
                return


    def swap_cells(self):
        if (self.end_cell < 8):
            temp = self.whole_inventory[self.end_cell]
            if (self.start_cell < 8):
                self.whole_inventory[self.end_cell] = self.whole_inventory[self.start_cell]
                self.whole_inventory[self.start_cell] = temp
            else:
                self.start_cell -= 8
                self.whole_inventory[self.end_cell] = self.inventory_panel[self.start_cell]
                self.inventory_panel[self.start_cell] = temp
        
        else:
            self.end_cell -= 8
            temp = self.inventory_panel[self.end_cell]
            if (self.start_cell < 8):
                self.inventory_panel[self.end_cell] = self.whole_inventory[self.start_cell]
                self.whole_inventory[self.start_cell] = temp
            else:
                self.start_cell -= 8
                self.inventory_panel[self.end_cell] = self.inventory_panel[self.start_cell]
                self.inventory_panel[self.start_cell] = temp


inventory = Inventory()