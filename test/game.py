# import parameters as p

import sys

import bird as bird
import images as img
from button import *
from object import *
from effects import *
from states import *
from bullet import *
from save import *

class Game():
    
    def __init__(self):
        p.screen.set_caption("Run, Dino! Run!") # задаёт заголовок
        # pygame.display.set_icon("./assets/backgrounds/icon.png") # добавляет иконку

        pygame.mixer.music.load("./assets/sounds/background.mp3") # фоновая музыка
        pygame.mixer.music.set_volume(0.2) # установка громкости

        self.cactus_options = [27, 474, 37, 447, 32, 445]
        self.dinoCounter = 0
        self.health = 2
        self.make_jump = False
        self.jump_counter = 30
        self.jump_num = 0
        self.scores = 0
        self.maxScores = 0
        self.maxAbove = 0
        self.cooldown = 0
        self.dino_num = 0
        self.land_num = 0
        self.game_state = GameState()
        self.saveData = Save()
        # self.bird = bird.Bird()
        # self.Bullet = Bullet()

    def start(self):
        while(True):
            if (self.game_state.check(State.MENU)):
                self.showMenu()

            elif (self.game_state.check(State.START)):
                self.chooseTheme()
                self.chooseHero()
                self.start_game()

            elif (self.game_state.check(State.CONTINUE)):
                self.maxScores = self.saveData.get("max")
                self.land_num = self.saveData.get("land")
                self.dino_num = self.saveData.get("dino")
                self.start_game()

            elif (self.game_state.check(State.QUIT)):
                self.saveData.save("max", self.maxScores)
                self.saveData.save("dino", self.dino_num)
                self.saveData.save("land", self.land_num)
                break


    def showMenu(self):
        pygame.mixer.music.load("./assets/sounds/Big_Slinker.mp3") # фоновая музыка
        pygame.mixer.music.set_volume(0.3) # установка громкости
        pygame.mixer.music.play(1)
        
        startButton = Button(288, 70)
        continueButton = Button(225, 70)
        quitButton = Button(120, 70)


        show = True
        while(show): # рабочий цикл
            for event in pygame.event.get():
                if (event.type == pygame.QUIT): sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_F1]:
                sys.exit()

            pygame.mixer.music.stop()

            screenMode.blit(img.menuBackground, (0, 0))

            if (startButton.draw(270, 200, "Start game", font_size = 50)):
                self.game_state.change(State.START)
                return
           
            if (continueButton.draw(300, 300, "Continue", font_size = 50)):
                self.game_state.change(State.CONTINUE)
                return     

            if (quitButton.draw(350, 400, "Quit", font_size = 50)):
                self.game_state.change(State.QUIT)
                return 


            draw_mouse()

            p.screen.update()
            p.clock.tick(60)

    def start_game(self):        
        # pygame.mixer.music.play(-1)

        while self.game_cycle():
            self.scores = 0
            self.make_jump = False
            self.jump_counter = 30
            p.dino_y = p.height - p.dino_h - 100
            self.health = 2
            self.cooldown = 0

    def game_cycle(self):
        game = True

        cactusArr = [] # создание кактусов
        self.create_cactusArr(cactusArr) # заполнение массива
        self.create_cactusArr(cactusArr)
        self.create_cactusArr(cactusArr)

        stone, cloud = self.open_random_objects()

        heart = Object(p.width, 280, 30, 4, img.healthIMG)

        bird1 = bird.Bird(-80)
        bird2 = bird.Bird(-109)
        allBirds = [bird1 , bird2]

        allBullets = []

        while(game): # рабочий цикл
            for event in pygame.event.get():
                if (event.type == pygame.QUIT): sys.exit() # закрываем приложение по нажатию красной кнопки

            keys = pygame.key.get_pressed()
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()        

            img.setTheme(self.land_num)
            screenMode.blit(img.land, (0, 0))

            if keys[pygame.K_F10]:
                sys.exit()

            if keys[pygame.K_SPACE]: # прыжок динозавра
                self.make_jump = True 
                if (0 < self.jump_counter < 27):
                    if (not self.jump_num):
                        self.jump_num += 1
                        self.jump_counter = 30

            if self.make_jump:
                self.jump()

            self.draw_cactusArr(cactusArr) # рисуем кактусы
            self.moveObjects(cloud) # рисуем камни и облака 

            self. countScores(cactusArr) # считаем очки и добавляем их

            printText("Scores: " + str(self.scores), 600, 10)

            self.drawDino() # рисуем динозавра

            if not self.cooldown:
                if click[0]:
                    pygame.mixer.Sound.play(bulletSound)
                    addBullet = Bullet(p.dino_x + p.dino_w, p.dino_y + 28)
                    addBullet.findPath(mouse[0], mouse[1])

                    allBullets.append(addBullet)
                    self.cooldown = 50
            else:
                printText("Cooldown time: " + str(self.cooldown // 10), 482, 40)
                self.cooldown -= 1

            for bullet in allBullets:
                if not bullet.move_to():
                    allBullets.remove(bullet)

            
            self.draw_birds(allBirds)
            self.check_birds_damage(allBullets, allBirds)
            
            if keys[pygame.K_ESCAPE]: # пауза
                self.paused()
            
            heart.move()
            self.heartPlus(heart)

            if (self.checkCollision(cactusArr)):# or (self.checkCollision(bird.birdBullets, for_bird = True)): # если коллизия - -здоровье
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(fallSound)
                game = False

            self.showHealth()

            draw_mouse()

            p.screen.update()
            p.clock.tick(60)
        return self.game_over()

    def game_over(self):
        if (self.scores > self.maxScores):
            self.maxScores = self.scores

        stopped = True
        while stopped:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT): sys.exit() # закрываем приложение по нажатию красной кнопки

            printText("Game over. Press Enter to play again, or Esc to exit", 15, 300)
            printText("Max scores: " + str(self.maxScores), 300, 350)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                return True

            if keys[pygame.K_F10]:
                sys.exit()

            if keys[pygame.K_ESCAPE]:
                self.game_state.change(State.QUIT)
                return False

            p.screen.update()
            p.clock.tick(15)



    @staticmethod
    def paused():
        paused = True

        pygame.mixer.music.pause() # остановка музыки

        while paused:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT): sys.exit() # закрываем приложение по нажатию красной кнопки

            printText("Paused. Press Enter to continue", p.width/5, p.height/2)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                paused = False

            if keys[pygame.K_F10]:
                sys.exit()

            p.screen.update()
            p.clock.tick(15)
        pygame.mixer.music.unpause() # включение музыки

    @staticmethod
    def cactusDistance(array):
        maximum = max(array[0].x, array[1].x, array[2].x)
        
        if (maximum < p.width):
            distance = p.width
            if ((distance - maximum) < 50):
                distance += 250
        else:
            distance = maximum

        choice = random.randrange(0, 5)
        if (choice == 0):
            distance += random.randrange(10, 15)
        else:
            distance += random.randrange(200, 350)

        return distance

    @staticmethod
    def open_random_objects():
        choice = random.randrange(0, 2)
        imgStone = img.stoneIMG[choice]

        choice = random.randrange(0, 2)
        imgCloud = img.cloudIMG[choice]
        
        stone = Object(p.width, p.height-80, 10, 4, imgStone)
        cloud = Object(p.width, 80, 70, 2, imgCloud)

        return stone, cloud

    @staticmethod
    def moveObjects(cloud):
        check = cloud.move()
        if (not check):
            choice = random.randrange(0, 2)
            imgCloud = img.cloudIMG[choice]
            cloud.return_self(p.width, random.randrange(10, 200), cloud.w, imgCloud)

    @staticmethod
    def draw_birds(birds):
        for bird in birds:
            action = bird.draw()
            if (action == 1):
                bird.show()
            elif (action == 2):
                bird.hide()
            else:
                bird.shoot()

    @staticmethod
    def check_birds_damage(bullets, birds):
        for bird in birds:
            for bullet in bullets:
                bird.checkDamage(bullet)

    def chooseHero(self):
        hero_1 = Button(185, 70)
        hero_2 = Button(165, 70)
        hero_3 = Button(88, 70)

        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT): sys.exit() # закрываем приложение по нажатию красной кнопки

            p.screenMode.fill((255, 255, 255))

            printText("Choose dino color", 150, 100, font_size = 60)

            if (hero_1.draw(290, 200, "Orange", font_size = 50)):
                    img.setHero(1)
                    self.dino_num = 1
                    return

            if (hero_2.draw(300, 300, "Purple", font_size = 50)):
                    img.setHero(2)
                    self.dino_num = 2
                    return

            if (hero_3.draw(340, 400, "Red", font_size = 50)):
                    img.setHero(3)
                    self.dino_num = 3
                    return
            
            p.screen.update()
            p.clock.tick(60)  

    def chooseTheme(self):
        theme_1 = Button(255, 70)
        theme_2 = Button(300, 70)

        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT): sys.exit() # закрываем приложение по нажатию красной кнопки

            p.screenMode.fill((255, 255, 255))

            if (theme_1.draw(270, 200, "Day theme", font_size = 50)):
                    img.setTheme(1)
                    self.land_num = 1
                    return

            if (theme_2.draw(245, 300, "Night theme", font_size = 50)):
                    img.setTheme(2)
                    self.land_num = 2
                    return
            
            p.screen.update()
            p.clock.tick(60) 

    def jump(self):
        if (self.jump_counter >= -30):
            if (self.jump_counter == 30):
                pygame.mixer.Sound.play(jumpSound)
            if (self.jump_counter == -26):
                pygame.mixer.Sound.play(fallSound)

            p.dino_y -= self.jump_counter / 2.5
            self.jump_counter -= 1 

        else: 
            if (p.dino_y < 400):
                p.dino_y = min (400, p.dino_y - (self.jump_counter / 2.5))
                self.jump_counter -= 1 
            else:
                self.jump_num = 0
                self.jump_counter = 30
                self.make_jump = False

    def create_cactusArr(self, array):
        choice = random.randrange(0, 3)
        IMG_1 = img.cactusIMG[choice]
        w = self.cactus_options[choice * 2]
        h = self.cactus_options[choice * 2 + 1]
        array.append(Object(p.width + 20, h, w, 4, IMG_1))

    def draw_cactusArr(self, array):
        for cactus in array:
            check = cactus.move()
            if not check:
                self.objectReturn(array, cactus)

    def objectReturn(self, objects, obj):
        distance = self.cactusDistance(objects)

        choice = random.randrange(0, 3)
        img_1 = img.cactusIMG[choice]
        w = self.cactus_options[choice * 2]
        h = self.cactus_options[choice * 2 + 1]

        obj.return_self(distance, h, w, img_1)

    def drawDino(self):
        if (self.dinoCounter == 25): 
            self.dinoCounter = 0

        img.setHero(self.dino_num)
        screenMode.blit(img.dino[self.dinoCounter // 5], (p.dino_x, p.dino_y))
        self.dinoCounter += 1

    def checkCollision(self, barriers, for_bird = False):
        for barrier in barriers:
            if (barrier.y == 474): # little cactus
                if not self.make_jump: # если не сделан прыжок, проверяем по х
                    if (barrier.x <= (p.dino_x + p.dino_w - 35) <= (barrier.x + barrier.w)):
                        if self.checkHealth(): 
                            self.objectReturn(barriers, barrier)
                            return False
                        else:
                            return True


                elif (self.jump_counter >= 0): # первая половина прыжка
                    if ((p.dino_y + p.dino_h - 5) >= barrier.y): # проверка по у
                        if (barrier.x <= (p.dino_x + p.dino_w - 35) <= (barrier.x + barrier.w)): # проверка по х
                            if self.checkHealth(): 
                                self.objectReturn(barriers, barrier)
                                return False
                            else:
                                return True

                else: # вторая половина прыжка
                    if ((p.dino_y + p.dino_h - 10) >= barrier.y): # проверка по у
                        if (barrier.x <= p.dino_x <= (barrier.x + barrier.w)):
                            if self.checkHealth(): 
                                self.objectReturn(barriers, barrier)
                                return False
                            else:
                                return True

            else: # others cactuses
                if not self.make_jump: # если не сделан прыжок, проверяем по х
                    if (barrier.x <= (p.dino_x + p.dino_w - 25) <= (barrier.x + barrier.w)):
                            if self.checkHealth(): 
                                self.objectReturn(barriers, barrier)
                                return False
                            else:
                                return True

                elif (self.jump_counter == 10): # начало первой половины прыжка
                    if ((p.dino_y + p.dino_h - 5) >= barrier.y): # если столкновение по у
                        if (barrier.x <= (p.dino_x + p.dino_w - 5) <= (barrier.x + barrier.w)): # проверяем по х
                            if self.checkHealth(): 
                                self.objectReturn(barriers, barrier)
                                return False
                            else:
                                return True

                elif (self.jump_counter >= -1): # начало второй половины прыжка
                    if ((p.dino_y + p.dino_h - 5) >= barrier.y): # если столкновение по у
                        if (barrier.x <= (p.dino_x + p.dino_w - 35) <= (barrier.x + barrier.w)): # проверка по х
                            if self.checkHealth(): 
                                self.objectReturn(barriers, barrier)
                                return False
                            else:
                                return True

                    else:
                        if ((p.dino_y + p.dino_h - 10) >= barrier.y): # проверка по у
                            if (barrier.x <= (p.dino_x + 5) <= (barrier.x + barrier.w)): # проверка по х
                                if self.checkHealth(): 
                                    self.objectReturn(barriers, barrier)
                                    return False
                                else:
                                    return True
            # if for_bird: 
            #     if (p.dino_x <= barrier.x <= (p.dino_x + p.dino_w)):
            #         if (p.dino_y <= barrier.y <= (p.dino_y + p.dino_h)):
            #             if self.checkHealth(): 
            #                     barriers.remove(barrier)
            #                     return False
            #             else:
            #                 return True

        # if for_bird:
        #     for bullet in bird.birdBullets:
        #         if (not bullet.move_to(reverse = True)):
        #             self.birdBullets.remove(bullet)

        return False

    def countScores(self, barriers):
        aboveCactus = 0

        if (-20 <= self.jump_counter < 25): # считаем сколько кактусов перепрыгнули
            for barrier in barriers:
                if ((p.dino_y + p.dino_h - 5) <= barrier.y):
                    if (barrier.x <= p.dino_x <= (barrier.x + barrier.w)):
                        aboveCactus += 1
                    elif (barrier.x <= (p.dino_x + p.dino_w) <= (barrier.x + barrier.w)):
                        aboveCactus += 1
            self.maxAbove = max(aboveCactus, self.maxAbove)

        else: # добавляем очки
            if (self.jump_counter == -30):
                self.scores += self.maxAbove
                self.maxAbove = 0

    def showHealth(self):
        show = 0
        x = 20
        while (show != self.health):
            screenMode.blit(img.healthIMG, (x, 20))
            x += 40
            show += 1

    def checkHealth(self):
        self.health -= 1
        if (self.health == 0):
            pygame.mixer.Sound.play(lossSound)
            return False
        else:
            pygame.mixer.Sound.play(fallSound)
            return True

    def heartPlus(self, heart):
        if (heart.x <= -heart.w):
            distance = p.width + random.randrange(500, 1700)
            heart.return_self(distance, heart.y, heart.w, img.healthIMG)

        if (p.dino_x <= heart.x <= (p.dino_x + p.dino_w)):
            if (p.dino_y <= heart.y <= (p.dino_y + p.dino_h)):
                pygame.mixer.Sound.play(heartSound)
                if (self.health < 5):
                    self.health += 1

                distance = p.width + random.randrange(500, 1700)
                heart.return_self(distance, heart.y, heart.w, img.healthIMG)

    def checkDamage(self, bullet):
        if (self.x <= bullet.x <= (self.x + self.w)):
            if (self.y <= bullet.y <= (self.y + self.h)):
                self.go_away = True
