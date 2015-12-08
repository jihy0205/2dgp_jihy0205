import random
import json
import os
import time

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

plants = None
flowers = None
potatoes = None
bombs = None
sun = None

matrix = [[0 for col in range(5)] for row in range(7)]
sun_time = 0.0
zomby_time = 0.0
hp_time = 0.0
gameover_image = None

class Background:
    def __init__(self):
        self.image = load_image('background.png')
        self.gameover_image = load_image('over.png')
        self.get_start = True

    def gameover(self):
        self.gameover_image.draw(400, 300)

    def draw(self):
        self.image.draw(400, 300)

def enter():
    global back, attack, plant, flower, enemy, potato, bomb, sun
    global unit_1, unit_2, unit_3, unit_4
    back = Background()
    flower = Flower()
    plant = Plant1()
    enemy = [Zomby() for i in range(6)]
    attack = Attack()
    potato = Potato()
    bomb = Bomb()
    sun = Sun()
    unit_1 = []
    unit_2 = []
    unit_3 = []
    unit_4 = []

def exit():
    global back, plant, attack, flower, enemy, potato, bomb, sun
    del(plant)
    del(back)
    del(flower)
    del(enemy)
    del(attack)
    del(potato)
    del(bomb)
    del(sun)

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
                plant.x, plant.y = 50, 350
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
    global back, hp_time
    if back.get_start == True:
        if plant_ == True:
            plant.update(frame_time)
            attack.update(frame_time, plant.x)
        if flower_ == True:
            flower.update(frame_time)
        if potato_ == True:
            potato.update(frame_time)
        if bomb_ == True:
            bomb.update(frame_time)
        for zomby in enemy:
            zomby.update(frame_time)
            if zomby.x <= 50:    # 게임 패배
                back.get_start = False

    #충돌체크
        for zomby in enemy:
            if plant_ == True:
                if collide(zomby, plant):
                    zomby.state = zomby.ATTACK
                    if zomby.attack == True:
                        if plant.hp != 0:
                            plant.hp -= zomby.atk
                            zomby.attack = False
                else:
                    zomby.state = zomby.WALK
                if collide(attack, zomby):
                    attack.show = False
                    attack.x = plant.x+10
                    zomby.hp -= attack.atk
                    if(zomby.hp == 0):
                        zomby.state = zomby.DIE
                        enemy.remove(zomby)
            if flower_ == True:
                if collide(flower, zomby):
                    zomby.state = zomby.ATTACK
                    if zomby.attack == True:
                        if flower.hp != 0:
                            flower.hp -= zomby.atk
                            zomby.attack = False
                else:
                    zomby.state = zomby.WALK
            if potato_ == True:
                if collide(potato, zomby):
                    zomby.state = zomby.ATTACK
                    if zomby.attack == True:
                        if potato.hp != 0:
                            potato.hp -= zomby.atk
                            zomby.attack = False
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
        if attack.show == True:
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
    if back.get_start == False:
        back.gameover()
    update_canvas()
    delay(0.05)

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




