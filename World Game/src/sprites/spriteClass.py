import pygame as pg

class Sprite(pg.sprite.Sprite):

    global spriteList
    spriteList = []

    def __init__(self, surface=type(pg.Surface), name=str(), img=pg.image, pos=tuple(), size=tuple() or None, state=str(), type=str()):
        pg.sprite.Sprite.__init__(self)

        self.typeList = ["entity", "object", "tile"]
        self.surface = surface
        self.name = name
        self.collapse = True
        self.state = state
        self.pos = pos

        self.posX, self.posY = self.pos[0], self.pos[1]

        if type in self.typeList:
            self.type = type
        else:
            print("This type seems to not exist")
            return

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.posX, self.posY)

        spriteList.append(self)

    def draw(self):
        self.surface.blit(self.image, self.rect)

    def update(self):
        self.rect.topleft = (self.posX, self.posY)
