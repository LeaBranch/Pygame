from parameters import *
from images import bulletIMG

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 8
        self.speed_y = 0
        self.dist_x = 0
        self.dist_y = 0

    def move(self):
        self.x += self.speed_x
        if (self.x  <= width):
            screenMode.blit(bulletIMG, (self.x, self.y))
            return True
        else:
            return False

    def findPath(self, dest_x, dest_y):
        self.dest_x = dest_x
        self.dest_y = dest_y

        delta_x = dest_x - self.x
        count_up = delta_x // self.speed_x

        if (self.y >= dest_y):
            delta_y = self.y - dest_y
            self.speed_y = delta_y / count_up
        else:
            delta_y = dest_y - self.y
            self.speed_y = -(delta_y / count_up)

    def move_to(self, reverse = False):
        if not reverse:
            self.x += self.speed_x
            self.y -= self.speed_y
        else:
            self.x -= self.speed_x
            self.y += self.speed_y

        if (self.x <= width) and (not reverse):
            screenMode.blit(bulletIMG, (self.x, self.y))
            return True
        elif (self.x >= 0) and (reverse):
            screenMode.blit(bulletIMG, (self.x, self.y))
            return True
        else:
            return False