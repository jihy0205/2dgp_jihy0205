from pico2d import *
import random

plant = None
flower = None
attack1 = None
attack_x=0
isAttack = False
dist = 0
count =0
attack_y=0


class Plant1:
    def __init__(self):
        self.x, self.y = 250, 350
        self.frame = 0
        self.image = load_image('plant1.png')
        self.count =0

    def update(self):
        global isAttack
        global count
        self.frame = (self.frame + 1) % 8
        count += 5
        if (count==50):
            count=0
            isAttack = True

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def get_bb(self):
        return self.x-30, self.y-40, self.x+30, self.y+40

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Flower:
    def __init__(self):
        self.x, self.y = 250, 450
        self.frame = 0
        self.image = load_image('flower.png')

    def update(self):
        self.frame = (self.frame + 1)% 8

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

    def get_bb(self):
        return self.x-30, self.y-40, self.x+30, self.y+40

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Potato:
    def __init__(self):
        self.x, self.y = 250, 250
        self.frame = 0
        self.image = load_image('potato.png')

    def update(self):
        self.frame = (self.frame + 1)% 4

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

    def get_bb(self):
        return self.x-30, self.y-40, self.x+30, self.y+40

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Bomb:
    def __init__(self):
        self.x, self.y = 250, 150
        self.frame =0
        self.image = load_image('bomb.png')

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

    def get_bb(self):
        return self.x-20, self.y-20, self.x+20, self.y+20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Attack1:
    def __init__(self):
        self.image = load_image('attack.png')
        self.frame =0
        self.x, self.y = Plant1().x+30, Plant1().y+20

    def update(self):
        global isAttack
        global dist
        global count
        if (isAttack == True):
          self.x+=13
          dist += 5
          if(self.x > 700):
              isAttack = False
              self.x = Plant1().x+30
              dist = 0

        elif (isAttack == False):
            count += 7
            if(count > 130):
                isAttack = True
                count = 0

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x-13, self.y-13, self.x+13, self.y+13

    def draw_bb(self):
        draw_rectangle(*self.get_bb())