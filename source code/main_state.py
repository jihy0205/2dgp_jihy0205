import random
import json
import os

from pico2d import *
import game_framework
import title_state
from plants import *
from zombies import *
from sun import *


name = "MainState"

back = None
# 생성여부변수
plant_ = False
flower_ = False
potato_ = False
bomb_ = False
#
plants = None
flowers = None
potatoes = None
bombs = None

matrix = [[0 for col in range(5)] for row in range(7)]

gameover_image = None

class Background:
    def __init__(self):
        self.image = load_image('background.png')
        self.gameover_image = load_image('over.png')

    def draw(self):
        self.image.draw(400, 300)

def enter():
    global back, attack, plant, flower, enemy, potato, bomb
    global unit_1, unit_2, unit_3, unit_4
    back = Background()
    flower = Flower()
    plant = Plant1()
    enemy = [Zomby() for i in range(6)]
    attack = Attack()
    potato = Potato()
    bomb = Bomb()
    unit_1 = []
    unit_2 = []
    unit_3 = []
    unit_4 = []

def exit():
    global back, plant, attack, flower, enemy, potato, bomb
    del(plant)
    del(back)
    del(flower)
    del(enemy)
    del(attack)
    del(potato)
    del(bomb)

def pause():
    pass


def resume():
    pass

def handle_events(frame_time):
    global back, attack, plant, flower, enemy, potato, bomb
    global plant_, flower_, potato_, bomb_

    events = get_events()
    for event in events:
        if (event.type, event.key) ==(SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(title_state)
        elif event.type ==SDL_KEYDOWN:
            if event.key == SDLK_1:
                plant = Plant1()
                plant.x, plant.y =  50, 350
                plant_ = True
                attack = Attack()
                attack.x, attack.y = plant.x, plant.y+20
            if event.key == SDLK_2:
                flower = Flower()
                flower_ = True
            if event.key == SDLK_3:
                potato = Potato()
                potato_ = True
            if event.key == SDLK_4:
                bomb = Bomb()
                bomb_ = True
            if event.key == SDLK_5:
                plant = Plant1()
                plant.x, plant.y = 350, 150
                plant_ = True
                attack = Attack()
                attack.x, attack.y = plant.x, plant.y+20

def update(frame_time):
    if plant_ == True:
        plant.update(frame_time)
        attack.show = True
        attack.update(frame_time, plant.x)
    if flower_ == True:
        flower.update(frame_time)
    if potato_ == True:
        potato.update(frame_time)
    if bomb_ == True:
        bomb.update(frame_time)
    for zomby in enemy:
        zomby.update(frame_time)

    #충돌체크
    for zomby in enemy:
        if plant_ == True:
            if collide(zomby, plant):
                zomby.state = zomby.ATTACK
                plant.hp -= zomby.atk
            if collide(attack, zomby):
                attack.x = plant.x+20
                zomby.hp -= attack.atk
                if(zomby.hp == 0):
                    zomby.state = zomby.DIE
                    enemy.remove(zomby)
        if flower_ == True:
            if collide(flower, zomby):
                zomby.state = zomby.ATTACK
                flower.hp -= zomby.atk
        if potato_ == True:
            if collide(potato, zomby):
                zomby.state = zomby.ATTACK
                potato.hp -= zomby.atk
        if bomb_ == True:
            if collide(bomb, zomby): # 범위 내에 있는 좀비 사망
                for zomby in enemy:
                    if explosion(bomb, zomby):
                        zomby.state = zomby.DIE
                        enemy.remove(zomby)


def draw(frame_time):
    clear_canvas()
    back.draw()
    if plant_ == True:
        plant.draw(frame_time)
        plant.draw_bb()
        attack.draw()
        attack.draw_bb()
    if flower_ == True:
        flower.draw(frame_time)
        flower.draw_bb()
    if potato_ == True:
        potato.draw(frame_time)
        potato.draw_bb()
    if bomb_ == True:
        bomb.draw(frame_time)
        bomb.draw_bb()
    for zomby in enemy:
        zomby.draw(frame_time)
        zomby.draw_bb()
    update_canvas()
    delay(0.07)

def explosion(a, b):
    left_a, bottom_a, right_a, top_a = a.explosion_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if(left_a > right_b):return False
    if(right_a < left_b):return False
    if(top_a < bottom_b):return False
    if(bottom_a > top_b):return False

    return True

def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if(left_a > right_b):return False
    if(right_a < left_b):return False
    if(top_a < bottom_b):return False
    if(bottom_a > top_b):return False

    return True




