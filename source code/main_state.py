import random
import json
import os

from pico2d import *

import game_framework
import title_state
from plants import *
from zombies import *


name = "MainState"

back = None
isAttack = True


class Background:
    def __init__(self):
        self.image = load_image('background.png')

    def draw(self):
        self.image.draw(400, 300)




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
        attack.draw_bb()

    #충돌박스 그리기
    plant.draw_bb()
    flower.draw_bb()
    potato.draw_bb()
    bomb.draw_bb()

    update_canvas()
    delay(0.07)

def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if(left_a > right_b):return False
    if(right_a < left_b):return False
    if(top_a < bottom_b):return False
    if(bottom_a > top_b):return False

    return True



