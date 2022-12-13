import pygame
from objects import Cat, Box, Box_Background, Box_Upside_down, Box_Upside_down_Background, Heart_right, Heart_left

def first_level(lifes_given):
    pygame.init()
    '''База'''
    game_over = False
    clock = pygame.time.Clock()
    fps = 120
    dt = pygame.time.get_ticks()
    '''Задаем цвет и размер окна игры'''
    size = width, height = 1000, 800
    screen = pygame.display.set_mode(size)
    green = 170, 250, 170

    '''Начальное положение 1)стрелы 2)кота 3)уровня'''
    y, dy = 20, 5
    x_cat, y_cat = 215, 450
    vx_cat, vy_cat = 0, 0
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
                    vx_cat = 9-y_click/25
                    vy_cat = -1.25
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    level += 1
            screen.fill(green)
            f1 = pygame.font.Font(None, 36)
            text1 = f1.render('Рекоммендансьён: зеленая зона', 1, (0, 150, 100))
            text2 = f1.render('Впрочем, учатся на ошибках:)', 1, (0, 150, 100))
            screen.blit(text1, (10, 500))
            screen.blit(text2, (10, 530))
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
            box_background = Box_Background(screen, 800, height-180, 375, 70)
            box_background.output() 
            cat = Cat(screen, x_cat, y_cat, lifes_given)
            cat.output()
            box = Box(screen, 800, height, 375, 180) #  x_box, y_box, width, height
            box.output()

            scale = pygame.transform.scale(pygame.image.load('images\\scale.PNG'), (20, 150))
            scale_space = scale.get_rect(bottomright=(65, 200))
            screen.blit(scale, scale_space)

            '''Двигаем кота'''
            x_cat += vx_cat
            y_cat -= vy_cat

            '''Определяем пересечение областей кота и коробки'''
            # Rect.contains(Rect)
            # if box.rect.contains(cat.rect):
            if ((box.rect.centerx - cat.rect.centerx)**2 + (box.rect.centery - cat.rect.centery)**2)**0.5 < 50:
                level += 1
                clock.tick(fps)
                pygame.display.flip()
            elif cat.rect.centerx >= width or cat.rect.bottom == height:
                lifes_given -= 1
                pygame.display.update()
                first_level(lifes_given)
                game_over = True
            else:
                clock.tick(fps)
                pygame.display.flip()
        else:
            game_over = True
            break
    pass


def second_level(lifes_given, state):
    '''База'''
    game_over = state
    clock = pygame.time.Clock()
    fps = 60
    '''Задаем цвет и размер окна игры'''
    size = width, height = 1000, 800
    screen = pygame.display.set_mode(size)
    pink = 255, 190, 170

    '''Начальное положение 1)стрелы 2)кота 3)уровня'''
    y, dy = 20, 5
    x_cat, y_cat = 215, 450
    vx_cat, vy_cat = 0, 0
    global level
    level = 2

    while not game_over:
        if lifes_given != 0 and level == 2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    y_click = y
                    print(y_click)  # 50-200
                    vx_cat = 9-y_click/25
                    vy_cat = -1.25
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    level += 1
            screen.fill(pink)
            f1 = pygame.font.Font(None, 36)
            text1 = f1.render('Говорят, у кошки есть 9 жизней', 1, (210, 50, 50))
            text2 = f1.render('Тут однако 6. Прямо как номер одного общежития', 1, (210, 50, 50))
            screen.blit(text1, (300, 200))
            screen.blit(text2, (300, 230))
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
            box_background = Box_Background(screen, 800, height-144, 300, 56)
            box_background.output() 
            cat = Cat(screen, x_cat, y_cat, lifes_given)
            cat.output()
            box = Box(screen, 800, height, 300, 144)
            box.output()

            scale = pygame.transform.scale(pygame.image.load('images\\scale.PNG'), (20, 150))
            scale_space = scale.get_rect(bottomright=(65, 200))
            screen.blit(scale, scale_space)

            '''Двигаем кота'''
            x_cat += vx_cat
            y_cat -= vy_cat

            # Определяем пересечение областей кота и коробки
            # Rect.contains(Rect)
            if ((box.rect.centerx - cat.rect.centerx)**2 + (box.rect.centery - cat.rect.centery)**2)**0.5 < 60:
                level += 1
                clock.tick(fps)
                pygame.display.flip()
            elif cat.rect.right >= width or cat.rect.bottom == 800:
                lifes_given -= 1
                pygame.display.flip()
                second_level(lifes_given, False)
                game_over = True
            else:
                clock.tick(fps)
                pygame.display.flip()
        else:
            game_over = True
            break
    pass

def third_level(lifes_given, state):
    '''База'''
    game_over = state
    clock = pygame.time.Clock()
    fps = 60
    '''Задаем цвет и размер окна игры'''
    size = width, height = 1000, 800
    screen = pygame.display.set_mode(size)
    blue = 150, 150, 255

    '''Начальное положение 1)стрелы 2)кота 3)уровня'''
    y, dy = 20, 5
    x_cat, y_cat = 210, 450
    vx_cat, vy_cat = 0, 0
    global level
    level = 3

    while not game_over:
        if lifes_given != 0 and level == 3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    y_click = y
                    print(y_click)  # 50-200
                    vx_cat = 10-y_click/25
                    vy_cat = -4.5
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    level += 1
            screen.fill(blue)

            f1 = pygame.font.Font(None, 36)
            text1 = f1.render('Отзеркаливаемся от батута', 1, (40, 40, 120))
            screen.blit(text1, (200, 200))
            # батут
            batoot = pygame.image.load('images\батут.png')
            batoot_place = batoot.get_rect(bottomleft=(0,800))
            screen.blit(batoot,batoot_place)
            
            '''Рисуем коробку, кота, шкалу'''
            box = Box_Upside_down_Background(screen, 820, 250, 375, 80)
            box.output()
            cat = Cat(screen, x_cat, y_cat, lifes_given)
            cat.output()
            box = Box_Upside_down(screen, 820, 170, 375, 170)
            box.output()

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

            scale = pygame.transform.scale(pygame.image.load('images\\scale.PNG'), (20, 150))
            scale_space = scale.get_rect(bottomright=(65, 200))
            screen.blit(scale, scale_space)

            '''Двигаем кота'''
            if cat.rect.centery >= 700:
                vy_cat *= -1
            x_cat += vx_cat
            y_cat -= vy_cat

            # Определяем пересечение областей кота и коробки, кота и батута
            if ((box.rect.centerx - cat.rect.centerx)**2 + (box.rect.centery - cat.rect.centery)**2)**0.5 < 50:
                level += 1
                clock.tick(fps)
                pygame.display.flip()
            elif cat.rect.right >= width or cat.rect.centery <= 100:
                lifes_given -= 1
                pygame.display.flip()
                third_level(lifes_given, False)
                game_over = True
            else:
                clock.tick(fps)
                pygame.display.flip()
        else:
            game_over = True
            break
    pass

def fourth_level(lifes_given, state):
    pygame.init()
    '''База'''
    game_over = state
    clock = pygame.time.Clock()
    fps = 120
    '''Задаем цвет и размер окна игры'''
    size = width, height = 1000, 800
    screen = pygame.display.set_mode(size)
    lil = 230, 160, 255

    '''Начальное положение 1)стрелы 2)кота 3)уровня'''
    y, dy = 20, 5
    x_cat, y_cat = 550, 210
    vy_cat = 0
    x_box, dx_box = 800, 10
    global level
    level = 4

    while not game_over:
        if lifes_given != 0 and level == 4:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    y_click = y
                    print(y_click)  # 50-200
                    vy_cat = -(9-y_click/25)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    level += 1
            screen.fill(lil)

            f1 = pygame.font.Font(None, 36)
            text1 = f1.render('Самое время для многоходовочки', 1, (200, 80, 255))
            screen.blit(text1, (550, 500))
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
            '''Рисуем коробку, кота, шкалу, двигаем коробку'''
            box_background = Box_Background(screen, x_box, height-180, 375, 70)
            box_background.output() 
            cat = Cat(screen, x_cat, y_cat, lifes_given)
            cat.output()
            box = Box(screen, x_box, height, 375, 180) #  x_box, y_box, width, height
            box.output()
            x_box -= dx_box
            if x_box < 0 or x_box > 1000:
                dx_box *= -1

            scale = pygame.transform.scale(pygame.image.load('images\\scale.PNG'), (20, 150))
            scale_space = scale.get_rect(bottomright=(65, 200))
            screen.blit(scale, scale_space)

            '''Двигаем кота'''
            y_cat -= vy_cat

            '''Определяем пересечение областей кота и коробки'''
            if ((box.rect.centerx - cat.rect.centerx)**2 + (box.rect.centery - cat.rect.centery)**2)**0.5 < 60:
                level += 1
                clock.tick(fps)
                pygame.display.flip()
            elif cat.rect.bottom >= height:
                lifes_given -= 1
                pygame.display.update()
                fourth_level(lifes_given, False)
                game_over = True
            else:
                clock.tick(fps)
                pygame.display.flip()
        else:
            game_over = True
            break
    pass

def result(level):
    pygame.init()
    game_over = False
    size = 1000, 800
    screen = pygame.display.set_mode(size)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        if level == 5:
            screen.fill([255,255,255])

            f1 = pygame.font.Font(None, 36)
            text1 = f1.render('Congrats!', 1, (0, 0, 0))
            text2 = f1.render('You won!', 1, (0, 0, 0))
            screen.blit(text1, (500, 30))
            screen.blit(text2, (500, 700))

            picture_of_cat = pygame.image.load('images\won.png')
            place_of_cat = picture_of_cat.get_rect(center=[500,400])
            screen.blit(picture_of_cat, place_of_cat)
            pygame.display.update()
            pygame.time.delay(6000)
        else:
            screen.fill([255,255,255])
            f1 = pygame.font.Font(None, 36)
            text1 = f1.render('You lose :(', 1, (0, 0, 0))
            text2 = f1.render('Всё получится! Можешь попробовать снова', 1, (0, 0, 0))
            screen.blit(text1, (500, 30))
            screen.blit(text2, (220, 750))

            picture_of_cat = pygame.image.load('images\lose.png')
            place_of_cat = picture_of_cat.get_rect(center=[500,400])
            screen.blit(picture_of_cat, place_of_cat)
            pygame.display.update()
            pygame.time.delay(6000)
        game_over = True
        break
first_level(6)

if level == 2:
    state = False
else:
    state = True
second_level(6, state)

if level == 3:
    state = False
else:
    state = True
third_level(6, state)  

if level == 4:
    state = False
else:
    state = True
fourth_level(6, state)  

result(level)
pygame.quit()
print('finish')