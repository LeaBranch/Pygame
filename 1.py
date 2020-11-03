import sys, pygame
pygame.init() # инициализация

size = width, height = 800, 600 # размеры приложения
speed = [1, 1] # координаты для скорости(?)
black = 0, 0, 0 # цвет фона

screen = pygame.display
screenMode = screen.set_mode(size) # создаёт экран с размерами
screen.set_caption("Ball") # задаёт заголовок

# текстуры пули
bulletIMG = pygame.image.load("./assets/textures/shot.png")
# bulletIMG = pygame.transform.scale(bulletIMG, (30, 9)) # подгоняем картинку под нужный размер

# ball = pygame.image.load("intro_ball.gif") # добавляем текстуру
ballrect = bulletIMG.get_rect() # создаём объект

while(1): # рабочий цикл
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() # закрываем приложение по нажатию красной кнопки

    # ballrect = ballrect.move(speed) # движение (меняем координаты на противоположные)
    # if ballrect.left < 0 or ballrect.right > width:
    #     speed[0] = -speed[0] # по х
    # if ballrect.top < 0 or ballrect.bottom > height:
    #     speed[1] = -speed[1] # по у

    screenMode.fill(black) # закрасить экран
    screenMode.blit(bulletIMG, (100,100)) # наложить текстуру на объект
    pygame.display.flip() # ОБНОВИТЬ ЭКРАН
