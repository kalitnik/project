import pygame

class Cat():
    def __init__(self, screen, x_cat, y_cat, lifes):
        '''инициализация кота'''

        self.screen = screen
        if lifes == 6:
            self.image = pygame.image.load('images\cat_im.png')
        elif lifes == 5:
            self.image = pygame.image.load('images\cat_im_2.png')
        elif lifes == 4:
            self.image = pygame.image.load('images\cat_im_3.png')
        elif lifes == 3:
            self.image = pygame.image.load('images\cat_im_4.png')
        elif lifes == 2:
            self.image = pygame.image.load('images\cat_im_5.png')
        else:
            self.image = pygame.image.load('images\cat_im_6.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.right = x_cat
        self.rect.bottom = y_cat


    def output(self):
        '''рисует кота'''
        self.screen.blit(self.image, self.rect)



class Box():
    def __init__(self, screen, x_box, y_box, width, height):
        '''инициализация коробки'''

        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load('images\\box_down.png'), (width,height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = x_box
        self.rect.bottom = y_box


    def output(self):
        '''рисует коробкy'''
        self.screen.blit(self.image, self.rect)

class Box_Background():
    def __init__(self, screen, x_box, y_box, width, height):
        '''инициализация коробки'''

        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load('images\\box_up.png'), (width,height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = x_box
        self.rect.bottom = y_box

    def output(self):
        '''рисует коробкy'''
        self.screen.blit(self.image, self.rect)

class Box_Upside_down():
    def __init__(self, screen, x_box, y_box, width, height):
        '''инициализация коробки'''

        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load('images\\box_upside_down.png'), (width,height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = x_box
        self.rect.bottom = y_box

    def output(self):
        '''рисует коробкy'''
        self.screen.blit(self.image, self.rect)

class Box_Upside_down_Background():
    def __init__(self, screen, x_box, y_box, width, height):
        '''инициализация коробки'''

        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load('images\\box_upside_down_back.png'), (width,height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = x_box
        self.rect.bottom = y_box

    def output(self):
        '''рисует коробкy'''
        self.screen.blit(self.image, self.rect)

class Heart_right():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.image.load('images\\right.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #self.rect2 = self.image.get_rect(topleft = )
        self.rect.x = x
        self.rect.y = y

    def output(self):
        self.screen.blit(self.image, self.rect)
    #def out(self, x, y):
    #    self.screen.blit(self.image, self.rect2)


class Heart_left():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.image.load('images\left.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = x
        self.rect.y = y

    def output(self):
        self.screen.blit(self.image, self.rect)