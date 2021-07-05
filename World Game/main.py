import sys, os
import pygame as pg

from pygame.locals import *
from settings import *

from utils.utils import *
from src.sprites.spriteClass import *

class Game:

    def init(self):

        self.testSprite = Sprite(self.screen, "SpriteTest", importImage("res\grass_tile.png"), (0,0), None, "visible", "tile")


    def update(self):
        self.testSprite.posX += 5
        self.testSprite.update()


    def event(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.running = False
                pg.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                    pg.quit()
                    sys.exit()

    def draw(self, screen):
        #Clear the window
        screen.fill((0,0,0))
        #redraw
        self.testSprite.draw()
        #flip the display
        pg.display.flip()

    def run(self):
        pg.init()

        ds_info = pg.display.Info()
        x_pos_screen = 0
        y_pos_screen = 0
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x_pos_screen, y_pos_screen)

        self.m_width = ds_info.current_w
        self.m_height = ds_info.current_h

        self.fps = 60.0
        self.fpsClock = pg.time.Clock()

        self.screen = pg.display.set_mode((self.m_width, self.m_height), Settings.full_screen)

        pg.display.set_caption(Settings.name + " v" + Settings.version)

        self.running = True

        dt = 1 / self.fps * 1000

        self.init()

        while self.running:
            self.event()
            self.draw(self.screen)
            self.update()

            dt = self.fpsClock.tick(self.fps)


myGame = Game()
myGame.run()
