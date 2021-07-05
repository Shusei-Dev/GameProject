import pygame as pg

def importImage(path):
    image = pg.image.load(path).convert()
    return image
