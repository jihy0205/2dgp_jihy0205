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
<<<<<<< HEAD
# 생성여부변수
plant_ = False
flower_ = False
potato_ = False
bomb_ = False
#
plants = None
flowers = None
zombies = None
potatoes = None
bombs = None

matrix = [[0 for col in range(5)] for row in range(7)]

gameover_image = None
=======
isAttack = True

>>>>>>> origin/master

class Background:
    def __init__(self):
        self.image = load_image('background.png')
        self.gameover_image = load_image('over.png')

    def draw(self):
        self.image.draw(400, 300)

<<<<<<< HEAD
=======

#def get_frame_time():

#    global current_time

#    frame_time = get_time() - current_time
#    current_time += frame_time
#    return frame_time

>>>>>>> origin/master
def enter():
    global back, attack, plant, flower, enemy, zomby, potato, bomb
    global unit_1, unit_2, unit_3, unit_4
    back = Background()
<<<<<<< HEAD
=======
    plant = Plant1()
>>>>>>> origin/master
    flower = Flower()
    plant = Plant1()
    zomby = Zomby()
    enemy = [Zomby() for i in range(6)]
    attack=Attack()
    potato = Potato()
    bomb = Bomb()
    unit_1 = []
    unit_2 = []
    unit_3 = []
    unit_4 = []

def exit():
    global back, plant, attack, flower, enemy, zomby, potato, bomb
    del(plant)
    del(back)
    del(flower)
    del(zomby)
    del(attack)
    del(potato)
    del(bomb)

def pause():
    pass


def resume():
    pass

def handle_events(frame_time):
    global isAttack
    global back, attack, plant, flower, enemy, zomby, potato, bomb
    global plant_, flower_, potato_, bomb_

    events = get_events()
    for event in events:
<<<<<<< HEAD
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
=======
        if event.type ==SDL_QUIT:
            game_framework.quit()


def update():
#    frame_time = get_frame_time()
>>>>>>> origin/master
    global isAttack
    if plant_ == True:
        plant.update(frame_time)
        attack.update(frame_time)
    if flower_ == True:
        flower.update(frame_time)

    if potato_ == True:
        potato.update(frame_time)
    if bomb_ == True:
        bomb.update(frame_time)
    for zomby in enemy:
        zomby.update()

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
                pass


def draw(frame_time):
    global isAttack
    clear_canvas()
    back.draw()
<<<<<<< HEAD
    if plant_ == True:
        plant.draw(frame_time)
        plant.draw_bb()
        attack.draw(frame_time)
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
        zomby.draw()
        zomby.draw_bb()
=======
    plant.draw()
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

>>>>>>> origin/master
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




