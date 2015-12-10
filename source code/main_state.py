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

plants_index = 0
missiles_index = 0
flowers_index = 0
sun_collection_index = 0
potatoes_index = 0
bombs_index = 0
enemy_index = 0
tool_num = 0
mouse_x, mouse_y = 0, 0
gold = 0
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

def click():
    global plants, flowers, potatoes, bombs, missiles, sun_collection
    global plants_index, flowers_index, potatoes_index, bombs_index, missiles_index, sun_collection_index
    global plant_, flower_, potato_, bomb_
    global gold, tool_num
    global mouse_x, mouse_y
    # 땅 영역
    if 0 < mouse_x < 800 and 90 < mouse_y < 600:
        if tool_num == 1: # 좌표 설정, 배열값 설정

            plants.append(Plant1())
            Plant1().newSet(mouse_x, mouse_y)
            plants_index += 1
            plant_ = True

            missile = Attack()
            missile.x = Plant1().x + 20
            missile.y = Plant1().y + 10
            missiles.append(missile)
            missiles_index += 1

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
    global back, attack, plant, flower, enemy, potato, bomb
    global plants, flowers, potatoes, bombs, missiles, sun_collection
    global plants_index, flowers_index, potatoes_index, bombs_index, missiles_index, sun_collection_index
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
        elif event.type ==SDL_KEYDOWN:
            if event.key == SDLK_1:
                plants.append(Plant1())
                plants_index += 1
                plant_ = True
                missiles.append(Attack())
                missiles_index += 1
            if event.key == SDLK_2:
                flowers.append(Flower())
                flowers_index += 1
                flower_ = True
            if event.key == SDLK_3:
                potatoes.append(Potato())
                potatoes_index += 1
                potato_ = True
            if event.key == SDLK_4:
                bombs.append(Bomb())
                bombs_index += 1
                bomb_ = True

        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, event.y
        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            click()

def update(frame_time):
    global back, hp_time
    global plants, flowers, potatoes, bombs, missiles, sun_collection
    if back.get_start == True:
        if plant_ == True:
            for plant in plants:
                plant.update(frame_time)
                for attack in missiles:
                    attack.update(frame_time, plant.x)

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
        for zomby in enemy:
            if plant_ == True:
                for plant in plants:
                    if collide(zomby, plant):
                        zomby.state = zomby.ATTACK
                        if zomby.attack == True:
                            if plant.returnHP() == False:
                                plant.hp -= zomby.atk
                                zomby.attack = False
                            else:
                                plants.remove(plant)
                    else:
                        zomby.state = zomby.WALK

                    for attack in missiles:
                        if collide(attack, zomby):
                            attack.show = False
                            attack.x = plant.x+10
                            zomby.hp -= attack.atk
                            if zomby.returnHP() == True:
                                zomby.state = zomby.DIE
                                enemy.remove(zomby)

            if flower_ == True:
                for flower in flowers:
                    if collide(flower, zomby):
                        zomby.state = zomby.ATTACK
                        if zomby.attack == True:
                            if flower.returnHP() == False:
                                flower.hp -= zomby.atk
                                zomby.attack = False
                            else:
                                flowers.remove(flower)
                    else:
                        zomby.state = zomby.WALK

            if potato_ == True:
                for potato in potatoes:
                    if collide(potato, zomby):
                        zomby.state = zomby.ATTACK
                        if zomby.attack == True:
                            if potato.returnHP() == False:
                                potato.hp -= zomby.atk
                                zomby.attack = False
                            else:
                                potatoes.remove(potato)

            if bomb_ == True:
                for bomb in bombs:
                    if collide(bomb, zomby): # 범위 내에 있는 좀비 사망
                        for zomby in enemy:
                            if explosion(bomb, zomby):
                                zomby.state = zomby.DIE
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




