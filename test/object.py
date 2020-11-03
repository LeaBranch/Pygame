import random
import parameters as p

class Object:
    def __init__(self, x, y, w, speed, image):
        self.x = x
        self.y = y
        self.w = w
        self.speed = speed
        self.image = image

    def move(self):
        if (self.x  >= -self.w): # в зоне видимости
            p.screenMode.blit(self.image, (self.x, self.y))
            self.x -= self.speed # перемещаем по экрану
            return True
        else:
            self.x = p.width + 100 + random.randrange(-50, 60) # кактус вне зоны видимости
            return False

    def return_self(self, distance, y, w, image):
        self.x = distance
        self.y = y
        self.w = w
        self.image = image
        p.screenMode.blit(self.image, (self.x, self.y))


# =======================================================
    # def draw_array(self, array):
    #     for cactus in array:
    #         self.move()