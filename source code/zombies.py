from pico2d import *
import random

zomby = None

class Zomby:
    image = None
    def __init__(self):
        self.image = load_image('zombie_walking.png')
        self.x, self.y = 750, 370
        self.frame =0

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x -= 1

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Enemy1:
    image = None
    def __init__(self):
        self.x, self.y = 550, (random.randint(2, 5))*100
        self.frame = 0
        self.image = load_image('enemy2.png')

    def update(self):
        self.frame = (self.frame + 1)%8
        self.x -= 1

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
