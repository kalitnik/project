import pygame
from objects import Cat, Box, Heart_right, Heart_left


def first_level(lifes_given):
    pygame.init()

    '''База'''
    game_over = False
    clock = pygame.time.Clock()
    fps = 60
    '''Задаем цвет и размер окна игры'''
    size = width, height = 1000, 800
    screen = pygame.display.set_mode(size)
    green = 150, 255, 150

    '''Начальное положение 1)стрелы 2)кота 3)уровня'''
    y, dy = 20, 5
    x_cat, y_cat = 70, 450
    vx_cat, vy_cat, stop = 0, 0, 1
    global level
    level = 1

    while not game_over:
        if lifes_given != 0 and level == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    y_click = y
                    print(y_click)  # 50-200
                    vx_cat = y_click/20
                    vy_cat = -1.25
            screen.fill(green)
            # Шесть жизней
            x_heart, y_heart = 945, 5
            if lifes_given >= 1:
                heart1_r = Heart_right(screen, x_heart, y_heart)
                heart1_r.output()
            if lifes_given > 1:
                heart1_l = Heart_left(screen, x_heart-25, y_heart)
                heart1_l.output()
            if lifes_given > 2:
                heart2_r = Heart_right(screen, x_heart-50, y_heart)
                heart2_r.output()
            if lifes_given > 3:
                heart2_l = Heart_left(screen, x_heart-75, y_heart)
                heart2_l.output()
            if lifes_given > 4:
                heart2_r = Heart_right(screen, x_heart-100, y_heart)
                heart2_r.output()
            if lifes_given == 6:
                heart2_l = Heart_left(screen, x_heart-125, y_heart)
                heart2_l.output()

            '''Рисуем и двигаем стрелку'''
            pygame.draw.polygon(screen, (255, 0, 255), [(20, y+20), (40, y+10), (20, y), (20, y+20)])
            y += dy
            if y > 200 or y < 20:
                dy *= -1
            '''Рисуем коробку, кота, шкалу'''
            cat = Cat(screen, x_cat, y_cat, lifes_given)
            cat.output()
            box = Box(screen, 800, height, 375, 250) #  x_box, y_box, width, height
            box.output()

            scale = pygame.transform.scale(pygame.image.load('images\\scale.PNG'), (20, 150))
            scale_space = scale.get_rect(bottomright=(65, 200))
            screen.blit(scale, scale_space)

            '''Двигаем кота'''
            x_cat += vx_cat*stop
            y_cat -= vy_cat*stop

            '''Определяем пересечение областей кота и коробки'''
            # Rect.contains(Rect)
            if box.rect.contains(cat.rect):
                level += 1
                stop *= 0
                clock.tick(fps)
                pygame.display.flip()
                game_over = True
            elif cat.rect.right == width or cat.rect.bottom == height:
                lifes_given -= 1
                pygame.display.flip()
                first_level(lifes_given)
            else:
                clock.tick(fps)
                pygame.display.flip()
        else:
            game_over = True
            break
    pass


def second_level(lifes_given, state):
    pygame.init()
    '''База'''
    game_over = state
    clock = pygame.time.Clock()
    fps = 60
    '''Задаем цвет и размер окна игры'''
    size = width, height = 1000, 800
    screen = pygame.display.set_mode(size)
    color = 255, 150, 150

    '''Начальное положение 1)стрелы 2)кота 3)уровня'''
    y, dy = 20, 5
    x_cat, y_cat = 70, 450
    vx_cat, vy_cat, stop = 0, 0, 1
    level = 2

    while not game_over:
        if lifes_given != 0 and level == 2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    y_click = y
                    print(y_click)  # 50-200
                    vx_cat = y_click/20
                    vy_cat = -1.25
            screen.fill(color)
            # Шесть жизней
            x_heart, y_heart = 945, 5
            if lifes_given >= 1:
                heart1_r = Heart_right(screen, x_heart, y_heart)
                heart1_r.output()
            if lifes_given > 1:
                heart1_l = Heart_left(screen, x_heart-25, y_heart)
                heart1_l.output()
            if lifes_given > 2:
                heart2_r = Heart_right(screen, x_heart-50, y_heart)
                heart2_r.output()
            if lifes_given > 3:
                heart2_l = Heart_left(screen, x_heart-75, y_heart)
                heart2_l.output()
            if lifes_given > 4:
                heart2_r = Heart_right(screen, x_heart-100, y_heart)
                heart2_r.output()
            if lifes_given == 6:
                heart2_l = Heart_left(screen, x_heart-125, y_heart)
                heart2_l.output()

            '''Рисуем и двигаем стрелку'''
            pygame.draw.polygon(screen, (255, 0, 255), [(20, y+20), (40, y+10), (20, y), (20, y+20)])
            y += dy
            if y > 200 or y < 20:
                dy *= -1
            '''Рисуем коробку, кота, шкалу'''
            cat = Cat(screen, x_cat, y_cat, lifes_given)
            cat.output()
            box = Box(screen, 800, height, 300, 200)
            box.output()

            scale = pygame.transform.scale(pygame.image.load('images\\scale.PNG'), (20, 150))
            scale_space = scale.get_rect(bottomright=(65, 200))
            screen.blit(scale, scale_space)

            '''Двигаем кота'''
            # if cat.rect.centerx == width:
            #     vx_cat *= -1
            x_cat += vx_cat*stop
            y_cat -= vy_cat*stop

            # Определяем пересечение областей кота и коробки
            # Rect.contains(Rect)
            if box.rect.contains(cat.rect):
                level += 1
                stop *= 0
                clock.tick(fps)
                pygame.display.flip()
                game_over = True
            elif cat.rect.right == width or cat.rect.bottom == height:
                lifes_given -= 1
                pygame.display.flip()
                second_level(lifes_given, False)
            else:
                clock.tick(fps)
                pygame.display.flip()
        else:
            game_over = True
            pygame.quit()
            break
    pass


first_level(6)
pygame.quit()
if level == 2:
    state = False
else:
    state = True

second_level(6, state)
print('finish')