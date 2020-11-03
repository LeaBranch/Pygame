import random
from sounds import *
from images import *
from bullet import *
import parameters as p


class Bird():
    def __init__(self, away_y):
        self.x = random.randrange(550, 730)
        self.y = away_y
        self.w = 55
        self.h = 40
        self.away_y = away_y
        self.speed = 3
        self.dest_y = self.speed * random.randrange(20, 70)
        self.IMGcount = 0
        self.cooldown_hide = 0
        self.come = True
        self.go_away = False
        self.cd_shoot = 0
        self.birdBullets = []

    def draw(self):
        if (self.IMGcount == 30):
            self.IMGcount = 0

        p.screenMode.blit(birdIMG[self.IMGcount // 5], (self.x, self.y))
        self.IMGcount += 1

        if (self.come and (self.cooldown_hide == 0)):
            return 1
        elif self.go_away:
            return 2
        elif (self.cooldown_hide > 0):
            self.cooldown_hide -= 1
        return 0

    def show(self):
        if (self.y < self.dest_y):
            self.y += self.speed
        else:
            self.come = False
            self.dest_y = self.away_y

    def hide(self):
            if (self.y > self.dest_y):
                self.y -= self.speed
            else:
                self.come = True
                self.go_away = False
                self.x = random.randrange(550, 730)
                self.dest_y = self.speed * random.randrange(20, 70)
                self.cooldown_hide = 80

    def checkDamage(self, bullet):
        if (self.x <= bullet.x <= (self.x + self.w)):
            if (self.y <= bullet.y <= (self.y + self.h)):
                self.go_away = True

    def shoot(self):
        if not self.cd_shoot:
            pygame.mixer.Sound.play(bulletSound)
            newBullet = Bullet(self.x, self.y)
            newBullet.findPath(((p.dino_x + p.dino_w) // 2), (p.dino_y + p.dino_h))

            self.birdBullets.append(newBullet)
            self.cd_shoot = 200
        
        else:
            self.cd_shoot -= 1

        for bullet in self.birdBullets:
            if (not bullet.move_to(reverse = True)):
                self.birdBullets.remove(bullet)