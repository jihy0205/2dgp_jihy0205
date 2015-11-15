import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"

back = None
plant = None
flower = None
enemy = None
zomby = None
attack1 = None
IsAttack = False
attack_x=0
isAttack = False
dist = 0
count =0
attack_y=0

class Background:
    def __init__(self):
        self.image = load_image('background.png')

    def draw(self):
        self.image.draw(400, 300)



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

class Flower:
    def __init__(self):
        self.x, self.y = 250, 450
        self.frame = 0
        self.image = load_image('flower.png')

    def update(self):
        self.frame = (self.frame + 1)% 8

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Potato:
    def __init__(self):
        self.x, self.y = 250, 250
        self.frame = 0
        self.image = load_image('potato.png')

    def update(self):
        self.frame = (self.frame + 1)% 4

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Bomb:
    def __init__(self):
        self.x, self.y = 250, 150
        self.frame =0
        self.image = load_image('bomb.png')

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Attack1:
    def __init__(self):
        self.image = load_image('attack1.png')
        self.frame =0
        self.x, self.y = Plant1().x, Plant1().y

    def update(self):
        global isAttack
        global dist
        global count
        if (isAttack == True):
          self.x+=7
          dist += 5
          if(dist > 200):
              isAttack = False
              self.x = Plant1().x
              dist = 0

        elif (isAttack == False):
            count += 7
            if(count > 150):
                isAttack = True
                count = 0

    def draw(self):
        self.image.draw(self.x, self.y)

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

def enter():
    global back, attack, plant, flower, enemy, zomby, potato, bomb
    back = Background()
    plant = Plant1()
    enemy = Enemy1()
    flower = Flower()
    zomby = Zomby()
    attack=Attack1()
    potato = Potato()
    bomb = Bomb()

def exit():
    global back, plant, attack, flower, enemy, zomby, potato, bomb
    del(plant)
    del(back)
    del(enemy)
    del(flower)
    del(zomby)
    del(attack)
    del(potato)
    del(bomb)

def pause():
    pass


def resume():
    pass


def handle_events():
    global isAttack
    events = get_events()
    for event in events:
        if event.type ==SDL_QUIT:
            game_framework.quit()


def update():
    global isAttack
    plant.update()
    flower.update()
    zomby.update()
    attack.update()
    potato.update()
    bomb.update()

def draw():
    global isAttack
    clear_canvas()
    back.draw()
    plant.draw()
    #enemy.draw()
    flower.draw()
    zomby.draw()
    potato.draw()
    bomb.draw()
    if(isAttack == True):
        attack.draw()
    update_canvas()
    delay(0.07)




