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

tool_num = 0
mouse_x, mouse_y = 0, 0
gold = 0
matrix = [[0 for col in range(6)] for row in range(8)]
sun_time = 0.0
zomby_time = 0.0
hp_time = 0.0
idx_x, idx_y = 0, 0
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
    global plants, flowers, potatoes, bombs, missiles, sun_collection
    back = Background()
    enemy = [Zomby() for i in range(6)]
    plants = []
    missiles = []
    flowers = []
    sun_collection = []
    potatoes = []
    bombs = []

def exit():
    global back, plants, flowers, potatoes, bombs, missiles, sun_collection, enemy
    global plant_, flower_, potato_, bomb_
    del(back)
    del(enemy)
    del(plants)
    del(flowers)
    del(potatoes)
    del(bombs)
    del(missiles)
    del(sun_collection)

def pause():
    pass

def resume():
    pass

def clickArea():
    global plants, flowers, potatoes, bombs, missiles, sun_collection
    global plant_, flower_, potato_, bomb_
    global gold, tool_num, idx_x, idx_y
    global mouse_x, mouse_y
    global matrix
    # 땅 영역
    if 0 < mouse_x < 800 and 90 < mouse_y < 600:
        idx_x = int(mouse_x / 100)
        idx_y = int(mouse_y / 100)
        if tool_num == 1: # 좌표 설정, 배열값 설정
            if matrix[idx_y][idx_x] == 0:
                new_plant1 = Plant1()
                new_plant1.newSet(mouse_x, 599 - mouse_y)
                plants.append(new_plant1)

                new_missile = Attack()
                new_missile.newSet(mouse_x, 599 - mouse_y)
                missiles.append(new_missile)
                plant_ = True
                matrix[idx_y][idx_x] = 1
                tool_num = 0
            else:
                return False

        elif tool_num == 2:
            if matrix[idx_y][idx_x] == 0:
                new_flower = Flower()
                new_flower.newSet(mouse_x, 599 - mouse_y)
                flowers.append(new_flower)
                flower_ = True
                matrix[idx_y][idx_x] = 1
                tool_num = 0
            else:
                return False

        elif tool_num == 3:
            if matrix[idx_y][idx_x] == 0:
                new_potato = Potato()
                new_potato.newSet(mouse_x, 599 - mouse_y)
                potatoes.append(new_potato)
                potato_ = True
                matrix[idx_y][idx_x] = 1
                tool_num = 0
            else:
                return False

        elif tool_num == 4:
            if matrix[idx_y][idx_x] == 0:
                new_bomb = Bomb()
                new_bomb.newSet(mouse_x, 599 - mouse_y)
                bombs.append(new_bomb)
                bomb_ = True
                matrix[idx_x][idx_y] = 1
                tool_num = 0
            else:
                return False

        #삭제
        elif tool_num == 5:
            pass

    #UI 영역
    else:
        if 100 < mouse_x < 160 and 0 < mouse_y < 80:
            tool_num = 1
        elif 160 < mouse_x < 220 and 0 < mouse_y < 80:
            tool_num = 2
        elif 220 < mouse_x < 280 and 0 < mouse_y < 80:
            tool_num = 3
        elif 280 < mouse_x < 340 and 0 < mouse_y < 80:
            tool_num = 4
        elif 500 < mouse_x < 580 and 0 < mouse_y < 85:
            tool_num = 5
        else: tool_num = 0

    print('x, y: ', mouse_x, mouse_y)
    print('tool: ', tool_num)

def handle_events(frame_time):
    global plant_, flower_, potato_, bomb_
    global mouse_x, mouse_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            plant_ = False
            flower_ = False
            potato_ = False
            bomb_ = False
            game_framework.change_state(title_state)
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, event.y
        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            clickArea()

def update(frame_time):
    global back, hp_time
    global plants, flowers, potatoes, bombs, missiles, sun_collection
    if back.get_start == True:
        if plant_ == True:
            for plant in plants:
                plant.update(frame_time)
            for attack in missiles:
                attack.update(frame_time)

        if flower_ == True:
            for flower in flowers:
                flower.update(frame_time)

        if potato_ == True:
            for potato in potatoes:
                potato.update(frame_time)

        if bomb_ == True:
            for bomb in bombs:
                bomb.update(frame_time)

        for zomby in enemy:
            zomby.update(frame_time)
            if zomby.x <= 50:    # 게임 패배
                back.get_start = False

    #충돌체크
        if plant_ == True:
            for plant in plants:
                for zomby in enemy:
                    if collide(zomby, plant):
                        zomby.state = zomby.ATTACK
                        if zomby.attack == True:
                            if plant.returnHP() == False:
                                plant.hp -= zomby.atk
                                zomby.attack = False
                            else:
                                zomby.state = zomby.WALK
                                idx = plants.index(plant)
                                plants.remove(plant)
                                del missiles[idx]
                    else:
                        zomby.state = zomby.WALK

                for attack in missiles:
                    for zomby in enemy:
                        if collide(attack, zomby):
                            attack.show = False
                            attack.x = attack.initX
                            attack.y = attack.initY
                            zomby.hp -= attack.atk
                            if zomby.returnHP() == True:
                                zomby.state = zomby.DIE
                                enemy.remove(zomby)

        if flower_ == True:
            for flower in flowers:
                for zomby in enemy:
                    if collide(flower, zomby):
                        zomby.state = zomby.ATTACK
                        if zomby.attack == True:
                            if flower.returnHP() == False:
                                flower.hp -= zomby.atk
                                zomby.attack = False
                            else:
                                zomby.state = zomby.WALK
                                flowers.remove(flower)
                    else:
                        zomby.state = zomby.WALK

        if potato_ == True:
            for potato in potatoes:
                for zomby in enemy:
                    if collide(potato, zomby):
                        zomby.state = zomby.ATTACK
                        if zomby.attack == True:
                            if potato.returnHP() == False:
                                potato.hp -= zomby.atk
                                zomby.attack = False
                            else:
                                zomby.state = zomby.WALK
                                potatoes.remove(potato)
                    else:
                        zomby.state = zomby.WALK

        if bomb_ == True:
            for zomby in enemy:
                for bomb in bombs:
                    if collide(bomb, zomby): # 범위 내에 있는 좀비 사망
                        enemy.remove(zomby)
                        for zomby in enemy:
                            if explosion(bomb, zomby):
                                enemy.remove(zomby)
                        bombs.remove(bomb)

def draw(frame_time):
    global plants, flowers, potatoes, bombs, missiles, sun_collection
    global plant_, flower_, potato_, bomb_
    clear_canvas()
    back.draw()
    if plant_ == True:
        for plant in plants:
            plant.draw(frame_time)
            plant.draw_bb()
        for attack in missiles:
            if attack.show == True:
                attack.draw()
                attack.draw_bb()
    if flower_ == True:
        for flower in flowers:
            flower.draw(frame_time)
            flower.draw_bb()
    if potato_ == True:
        for potato in potatoes:
            potato.draw(frame_time)
            potato.draw_bb()
    if bomb_ == True:
        for bomb in bombs:
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




