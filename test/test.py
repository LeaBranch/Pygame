import sys, pygame, random

sky = 31, 133, 222 # цвет фона
ground = 131, 73, 4 # цвет земли



# счётчики

choice = False
# print("choice = ", choice)


# def staff():
    # def chooseHero():
    #     global width, height, choice

    #     lx, ly = width/2-100, height/2-40

    #     choice = True
    #     print("choice = ", choice)
    #     choose1 = Button(70, 70) # lx+50, ly-20
    #     choose2 = Button(70, 70)
    #     choose3 = Button(70, 70)
    #     ok = Button(70, 70)

    #     # while(choice):
    #     if(choice):
    #         Back = pygame.draw.rect(screenMode, (13, 100, 58), (230, 200, 340, 370))
            
    #         # отрисовка кнопок(radiobutton)        
    #         choose1.draw(350, 240, "V", chooseFunc, 50)
    #         choose2.draw(lx+50, ly+90, " ", chooseFunc, 50)
    #         choose3.draw(lx+50, ly+210, " ", chooseFunc, 50)
    #         ok.draw(lx, ly+250, "OK", ok, 50)
            
    #         # загрузка изображений
    #         dino1 = screenMode.blit(pygame.image.load("./assets/textures/dino/1.png"), (lx+155, ly-45))
    #         dino2 = screenMode.blit(pygame.image.load("./assets/textures/dino/6.png"), (lx+155, ly+80))
    #         dino3 = screenMode.blit(pygame.image.load("./assets/textures/dino/11.png"), (lx+155, ly+200))
            
    #         screen.update()
    #         # pygame.time.delay(5000) # временная задержка
    #         # pygame.time.wait(5000)

        
    # def chooseFunc():
    #     # ok.draw(lx, ly+250, "OK", ok, 50)
    #     print("chooseFunc")

    # def okFunc():
    #     global choice
    #     choice = False
    #     print("choice = ", choice)

def damage(bullet):
    global dino_x, dino_y, dino_w, dino_h
    if (dino_x <= bullet.x <= (dino_x + dino_w)):
        print("hi")
        if (dino_y <= bullet.y <= (dino_y + dino_h)):
            if checkHealth():
                bullets.remove(bullet)


showMenu()

pygame.quit()
quit()
