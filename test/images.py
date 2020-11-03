import pygame

pygame.init()

icon = pygame.image.load("./assets/backgrounds/icon.png")
menuBackground = pygame.image.load("./assets/backgrounds/Menu.jpg")

land = pygame.image.load("./assets/backgrounds/Land1.jpg")
cactusIMG = [pygame.image.load("./assets/textures/cactuses/2.png"), pygame.image.load("./assets/textures/cactuses/3.png"), pygame.image.load("./assets/textures/cactuses/4.png")]

stoneIMG = [pygame.image.load("./assets/textures/Stone0.png"), pygame.image.load("./assets/textures/Stone1.png")]

cloudIMG = [pygame.image.load("./assets/textures/Cloud0.png"), pygame.image.load("./assets/textures/Cloud1.png")]
# подгоняем картинку под нужный размер
cloudIMG[0] = pygame.transform.scale(cloudIMG[0], (93, 51))
cloudIMG[1] = pygame.transform.scale(cloudIMG[1], (120, 56))

# текстуры динозавра
dino = 0

dinoIMG_1 = [pygame.image.load("./assets/textures/dino/1.png"), 
pygame.image.load("./assets/textures/dino/2.png"), 
pygame.image.load("./assets/textures/dino/3.png"), 
pygame.image.load("./assets/textures/dino/4.png"), 
pygame.image.load("./assets/textures/dino/5.png")]

dinoIMG_2 = [pygame.image.load("./assets/textures/dino/6.png"), 
pygame.image.load("./assets/textures/dino/7.png"), 
pygame.image.load("./assets/textures/dino/8.png"), 
pygame.image.load("./assets/textures/dino/9.png"), 
pygame.image.load("./assets/textures/dino/10.png")]

dinoIMG_3 = [pygame.image.load("./assets/textures/dino/11.png"), 
pygame.image.load("./assets/textures/dino/12.png"), 
pygame.image.load("./assets/textures/dino/13.png"), 
pygame.image.load("./assets/textures/dino/14.png"), 
pygame.image.load("./assets/textures/dino/15.png")]

# текстуры птицы
birdIMG = [pygame.image.load("./assets/textures/bird/Bird0.png"), 
pygame.image.load("./assets/textures/bird/Bird1.png"), 
pygame.image.load("./assets/textures/bird/Bird2.png"), 
pygame.image.load("./assets/textures/bird/Bird3.png"), 
pygame.image.load("./assets/textures/bird/Bird4.png"), 
pygame.image.load("./assets/textures/bird/Bird5.png")]
# # подгоняем картинку под нужный размер
# birdIMG[0] = pygame.transform.scale(birdIMG[0], (53, 41))
# birdIMG[1] = pygame.transform.scale(birdIMG[1], (53, 33))
# birdIMG[2] = pygame.transform.scale(birdIMG[2], (53, 25))
# birdIMG[3] = pygame.transform.scale(birdIMG[3], (53, 39))
# birdIMG[4] = pygame.transform.scale(birdIMG[4], (53, 33))
# birdIMG[5] = pygame.transform.scale(birdIMG[5], (53, 29))

# текстуры здоровья
healthIMG = pygame.image.load("./assets/textures/heart.png")
healthIMG = pygame.transform.scale(healthIMG, (30, 30))

# текстуры пули
bulletIMG = pygame.image.load("./assets/textures/shot.png")
bulletIMG = pygame.transform.scale(bulletIMG, (30, 9))

# текстуры нажатия
light = [pygame.image.load("./assets/textures/Light0.png"), pygame.image.load("./assets/textures/Light1.png"), 
pygame.image.load("./assets/textures/Light2.png"), pygame.image.load("./assets/textures/Light3.png"), 
pygame.image.load("./assets/textures/Light4.png"), pygame.image.load("./assets/textures/Light5.png"),
pygame.image.load("./assets/textures/Light6.png"), pygame.image.load("./assets/textures/Light7.png"), 
pygame.image.load("./assets/textures/Light8.png"), pygame.image.load("./assets/textures/Light9.png"), 
pygame.image.load("./assets/textures/Light10.png")]

def setTheme(num):
    global land
    land = pygame.image.load(r"./assets/backgrounds/Land{}.jpg".format(num))

def setHero(num):
    global dino
    if (num == 1):
        dino = dinoIMG_1
    elif (num == 2):
        dino = dinoIMG_2
    elif (num == 3):
        dino = dinoIMG_3
    