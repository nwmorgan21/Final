import pygame as pg
from pygame.sprite import Sprite
from settings import *

class Slime(Sprite):
    def __init__(self,image,speed):
        Sprite.__init__(self)
        self.image = pg.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = (screenwidth / 2, screenheight / 2)
        self.moving = False
        #self.ability = ability
        self.vx = 0
        self.vy = 0
        self.Leftpressed = False
        self.Rightpressed = False
        self.Uppressed = False
        self.Downpressed = False
        self.speed = speed

    def update(self):
        print(self.rect.center)
        self.vx = 0
        self.vy = 0
        self.moving = False
        # print("right side :" + str(self.rect.right))
        # print("left side :" + str(self.rect.left))
        # print("top side :" + str(self.rect.top))
        # print("bottom side :" + str(self.rect.bottom))


        if self.Leftpressed == True or self.Rightpressed == True or self.Uppressed == True or self.Downpressed == True:
            self.moving = True

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.moving == False:
            self.Leftpressed = True

            self.Rightpressed = False
            self.Uppressed = False
            self.Downpressed = False

        elif keys[pg.K_RIGHT] and self.moving == False:
            self.Leftpressed = False

            self.Rightpressed = True

            self.Uppressed = False
            self.Downpressed = False

        elif keys[pg.K_UP] and self.moving == False:
            self.Leftpressed = False
            self.Rightpressed = False

            self.Uppressed = True

            self.Downpressed = False
            
        elif keys[pg.K_DOWN] and self.moving == False:
            self.Leftpressed = False
            self.Rightpressed = False
            self.Uppressed = False

            self.Downpressed = True

        if self.Leftpressed == True:
            self.moveleft()

        if self.Rightpressed == True:
            self.moveright()
    
        if self.Uppressed == True:
            self.moveup()

        if self.Downpressed == True:
            self.movedown()

        self.rect.x += self.vx
        self.rect.y += self.vy

    def moveleft(self):
        if self.rect.left == 0:
            self.moving = False
            self.Leftpressed = False
            self.vx = 0
        elif self.rect.left > 0:
            self.vx = -self.speed

    def moveright(self):
        if self.rect.right == screenwidth:
            self.moving = False
            self.Rightpressed = False
            self.vx = 0
        elif self.rect.right < screenwidth:
            self.vx = self.speed

    def moveup(self):
        if self.rect.top == 0:
            self.moving = False
            self.Uppressed = False
            self.vy = 0
        elif self.rect.top > 0:
            self.vy = -self.speed

    def movedown(self):
        if self.rect.bottom == screenheight:
            self.moving = False
            self.Downpressed = False
            self.vy = 0
        elif self.rect.right < screenheight:
            self.vy = self.speed


class Platform(Sprite):
    def __inti__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Endblock(Sprite):
    def __inti__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Coin(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
