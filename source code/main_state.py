import random
import json
import os
import time

from pico2d import *
import game_framework
import title_state
import stage2
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

clear_count = 2
dead_count = 0
zombie_count = 1
tool_num = 0
mouse_x, mouse_y = 0, 0
gold = 100000
matrix = [[0 for col in range(8)] for row in range(8)]
sun_time = 0.0
clear_time = 0.0
zombie_start = 0.0
zombie_end = 0.0
sun_start = 0.0
sun_end = 0.0
hp_time = 0.0
idx_x, idx_y = 0, 0
gameover_image = None
clear_image = None



class Background:
    def __init__(self):
        self.image = load_image('background.png')
        self.gameover_image = load_image('over.png')
        self.clear_image = load_image('clear.png')
        self.get_start = True
        self.get_clear = False
        self.font = load_font('ConsolaMalgun.ttf', 20)

    def gameover(self):
        self.gameover_image.draw(400, 300)

    def clear(self):
        self.clear_image.draw(400, 300)

    def draw(self):
        self.image.draw(400, 300)
        self.font.draw(33, 510, '%d'% gold)

def enter():
    global back, attack, plant, flower, enemy, potato, bomb, sun
    global plants, flowers, potatoes, bombs, missiles, sun_list, flower_sun, sun_area
    global zombie_start, sun_start
    back = Background()
    enemy = [Zombie()]
    plants = []
    missiles = []
    flowers = []
    sun_list = []
    potatoes = []
    bombs = []
    flower_sun = []
    sun_area = []

    zombie_start = time.time()
    sun_start = time.time()

def exit():
    global back, plants, flowers, potatoes, bombs, missiles, sun_list, enemy, flower_sun, sun_area
    global plant_, flower_, potato_, bomb_
    del(back)
    del(enemy)
    del(plants)
    del(flowers)
    del(potatoes)
    del(bombs)
    del(missiles)
    del(sun_list)
    del(flower_sun)
    del(sun_area)

def pause():
    pass

def resume():
    pass

def clickArea():
    global plants, flowers, potatoes, bombs, missiles, sun_list, flower_sun
    global plant_, flower_, potato_, bomb_
    global gold, tool_num, idx_x, idx_y
    global mouse_x, mouse_y
    global matrix

    # 땅 영역
    if 0 < mouse_x < 800 and 90 < mouse_y < 600:
        idx_x = int(mouse_x / 100)
        idx_y = int(mouse_y / 100)
        if tool_num == 1: # 좌표 설정, 배열값 설정
            if gold >= 100:
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
                    gold -= 100
                else:
                    return False

        elif tool_num == 2:
            if gold >= 50:
                if matrix[idx_y][idx_x] == 0:
                    new_flower = Flower()
                    new_flower.newSet(mouse_x, 599 - mouse_y)
                    flowers.append(new_flower)

                    new_flower_sun = FlowerSun()
                    new_flower_sun.newSet(mouse_x, 599 - mouse_y)
                    flower_sun.append(new_flower_sun)
                    flower_ = True
                    matrix[idx_y][idx_x] = 1
                    tool_num = 0
                    gold -= 50
                else:
                    return False

        elif tool_num == 3:
            if gold >= 50:
                if matrix[idx_y][idx_x] == 0:
                    new_potato = Potato()
                    new_potato.newSet(mouse_x, 599 - mouse_y)
                    potatoes.append(new_potato)
                    potato_ = True
                    matrix[idx_y][idx_x] = 1
                    tool_num = 0
                    gold -= 50
                else:
                    return False

        elif tool_num == 4:
            if gold >= 125:
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

def clickSun():
    global sun_list, gold
    global mouse_x, mouse_y
    for sun in sun_list:
        left, bottom, right, top = sun.get_bb()
        if left < mouse_x < right and bottom < mouse_y < top:
            sun_list.remove(sun)
            gold += 25

def handle_events(frame_time):
    global plant_, flower_, potato_, bomb_, back
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
            clickSun()

def newCreate():
    global zombie_start, zombie_end, sun_start, sun_end, zombie_count
    zombie_end = time.time()
    sun_end = time.time()

    if int(zombie_end - zombie_start) == random.randint(10, 15):
        if zombie_count < clear_count:
            enemy.append(Zombie())
            zombie_count += 1
            zombie_start = time.time()

    if int(sun_end - sun_start) == random.randint(15, 20):
        new_sun = Sun()
        sun_area.append(new_sun.get_bb())
        sun_list.append(new_sun)
        sun_start = time.time()

def update(frame_time):
    global back, hp_time, zombie_count, clear_count, dead_count, clear_time
    global plants, flowers, potatoes, bombs, missiles, sun_list, flower_sun
    if back.get_start == True:
        newCreate()

        if plant_ == True:
            for plant in plants:
                plant.update(frame_time)
            for attack in missiles:
                attack.update(frame_time)

        if flower_ == True:
            for flower in flowers:
                flower.update(frame_time)
            for f_sun in flower_sun:
                f_sun.update(frame_time)

        if potato_ == True:
            for potato in potatoes:
                potato.update(frame_time)

        if bomb_ == True:
            for bomb in bombs:
                bomb.update(frame_time)

        for zombie in enemy:
            zombie.update(frame_time)
            if zombie.x <= 50:    # 게임 패배
                back.get_start = False

        for sun in sun_list:
            sun.update(frame_time)

    #충돌체크
        if plant_ == True:
            for plant in plants:
                for zombie in enemy:
                    if collide(zombie, plant):
                        zombie.state = zombie.ATTACK
                        if zombie.attack == True:
                            if plant.returnHP() == False:
                                plant.hp -= zombie.atk
                                zombie.attack = False
                            else:
                                zombie.state = zombie.WALK
                                idx = plants.index(plant)
                                plants.remove(plant)
                                del missiles[idx]

                for attack in missiles:
                    for zombie in enemy:
                        if collide(attack, zombie):
                            attack.show = False
                            attack.x = attack.initX
                            attack.y = attack.initY
                            zombie.hp -= attack.atk
                            if zombie.returnHP() == True:
                                zombie.state = zombie.DIE
                                dead_count += 1
                                enemy.remove(zombie)



        for flower in flowers:
            for zombie in enemy:
                if collide(flower, zombie):
                    zombie.state = zombie.ATTACK
                    if zombie.attack == True:
                        if flower.returnHP() == True:
                            flower.hp -= zombie.atk
                            zombie.attack = False
                        else:
                            zombie.state = zombie.WALK
                            flower_idx = flowers.index(flower)
                            del flower_sun[flower_idx]
                            flowers.remove(flower)

        if potato_ == True:
            for potato in potatoes:
                for zombie in enemy:
                    if collide(potato, zombie):
                        zombie.state = zombie.ATTACK
                        if zombie.attack == True:
                            if potato.returnHP() == False:
                                potato.hp -= zombie.atk
                                zombie.attack = False
                            else:
                                zombie.state = zombie.WALK
                                potatoes.remove(potato)

        if bomb_ == True:
            for zombie in enemy:
                for bomb in bombs:
                    if collide(bomb, zombie): # 범위 내에 있는 좀비 사망
                        enemy.remove(zombie)
                        for zombie in enemy:
                            if explosion(bomb, zombie):
                                dead_count += 1
                                enemy.remove(zombie)
                        bombs.remove(bomb)
        # 게임 승리
        if dead_count == clear_count:
            back.get_clear = True
            clear_time += frame_time
            if clear_time >= 1.5:
                back.get_clear = False
                clear_time = 0.0
                game_framework.change_state(stage2)

def draw(frame_time):
    global plants, flowers, potatoes, bombs, missiles, sun_list, flower_sun
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
        for f_sun in flower_sun:
            if f_sun.show == True:
                f_sun.draw()

    if potato_ == True:
        for potato in potatoes:
            potato.draw(frame_time)
            potato.draw_bb()

    if bomb_ == True:
        for bomb in bombs:
            bomb.draw(frame_time)
            bomb.draw_bb()

    for zombie in enemy:
        zombie.draw(frame_time)
        zombie.draw_bb()

    for sun in sun_list:
        sun.draw()
        sun.draw_bb()

    if back.get_start == False:
        back.gameover()

    if back.get_clear == True:
        back.clear()
        back.get_clear = False

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




