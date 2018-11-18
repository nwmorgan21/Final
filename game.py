# This was made by Nate Morgan
# Thanks to Kids Can Code for the template I used
# Thanks to Corey Schaefer's python tutorials: "https://www.youtube.com/watch?v=ZDa-Z5JzLYM"

from random import *
import pygame as pg
from rooms import *
from characters import *
from settings import *

class Game:
    def __init__(self):
        # init game window, try:
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((screenwidth, screenheight))
        pg.display.set_caption("Slime Escape")
        self.clock = pg.time.Clock()
        self.running = True
        # init pygame and create...

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.player = Slime(greenslimeimg,greenslimespeed)
        self.all_sprites.add(self.player)
        #self.platform = Platform(370, screenheight/2, 20, screenheight/2)
        self.run()
        # create new player object

    def run(self):
        self.playing = True
        # game loop
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # runs the update method in every sprite
        self.all_sprites.update()

    def events(self):
        
        # listens for whether or not to quit
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        self.screen.fill(PURPLE)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def show_go_screen(self):
        pass

g = Game()

while g.running:
    g.show_go_screen()
    g.new()

pg.quit()


