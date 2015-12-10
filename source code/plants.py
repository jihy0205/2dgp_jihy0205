from pico2d import *
import random

plant = None
flower = None
attack1 = None
isAttack = True
dist = 0
count = 0
life_time = 0.0
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6

class Plant1:
    PIXEL_PER_METER = (10.0 / 0.15)           # 10 pixel 15 cm
    RUN_SPEED_KMPH = 3.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    def __init__(self):
        self.x = 0
        self.y = 0
        self.frame = 0
        self.image = load_image('plant1.png')
        self.hp = 50
        self.isTrue = False
        self.life_time = 0.0
        self.total_frames = 0.0
        self.createX = 0
        self.createY = 0

    def newSet(self, mouse_x, mouse_y):
        self.createX = int(mouse_x / 100)
        self.createY = int(mouse_y / 100)

        self.initX = self.createX * 100 + 50
        self.initY = self.createY * 100 + 50

    def returnHP(self):
        if self.hp != 0:
            return False
        return True

    def update(self, frame_time):
        self.total_frames += FRAMES_PER_ACTION * ACTION_PER_TIME * frame_time

        self.frame = int(self.total_frames + 1) % 8

    def draw(self, frame_time):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def get_bb(self):
        return self.x-30, self.y-40, self.x+30, self.y+40

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Flower:
    PIXEL_PER_METER = (10.0 / 0.15)           # 10 pixel 15 cm
    RUN_SPEED_KMPH = 3.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    def __init__(self):
        self.x, self.y = 250, 450
        self.frame = 0
        self.hp=50
        self.image = load_image('flower.png')
        self.life_time = 0.0
        self.total_frames = 0.0

    def returnHP(self):
        if self.hp != 0:
            return False
        return True

    def update(self, frame_time):
        self.life_time += frame_time
        self.total_frames += FRAMES_PER_ACTION * ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames + 1)% 8
        print("flower: ", self.hp)

    def draw(self, frame_time):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

    def get_bb(self):
        return self.x-30, self.y-40, self.x+30, self.y+40

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Potato:
    PIXEL_PER_METER = (10.0 / 0.15)           # 10 pixel 15 cm
    RUN_SPEED_KMPH = 3.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    def __init__(self):
        self.x, self.y = 250, 350
        self.frame = 0
        self.hp=200
        self.image = load_image('potato.png')
        self.life_time = 0.0
        self.total_frames = 0.0

    def returnHP(self):
        if self.hp != 0:
            return False
        return True

    def update(self, frame_time):
        self.life_time += frame_time
        self.total_frames += FRAMES_PER_ACTION * ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames + 1)% 4
        print("Potato: ", self.hp)

    def draw(self, frame_time):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

    def get_bb(self):
        return self.x-30, self.y-40, self.x+30, self.y+40

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Bomb:
    PIXEL_PER_METER = (10.0 / 0.15)           # 10 pixel 15 cm
    RUN_SPEED_KMPH = 3.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    def __init__(self):
        self.x, self.y = 250, 150
        self.frame =0
        self.image = load_image('bomb.png')
        self.left = self.x - 180
        self.bottom = self.y - 170
        self.right = self.x + 180
        self.top = self.y + 170
        self.life_time = 0.0
        self.total_frames = 0.0

    def update(self, frame_time):
        self.life_time += frame_time
        self.total_frames += FRAMES_PER_ACTION * ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames+ 1) % 4

    def explosion_bb(self):
        return self.left, self.bottom, self.right, self.top

    def draw(self, frame_time):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

    def get_bb(self):
        return self.x-20, self.y-20, self.x+20, self.y+20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Attack:
    PIXEL_PER_METER = (10.0 / 0.15)           # 10 pixel 15 cm
    RUN_SPEED_KMPH = 15.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    def __init__(self):
        self.image = load_image('attack.png')
        self.frame =0
        self.initX = 0
        self.initY = 0
        self.x, self.y = self.initX + 10, self.initY + 20
        self.dir = 1
        self.atk = 10
        self.show = True
        self.total_frames = 0.0

    def newSet(self, mouse_x, mouse_y):
        createX = int(mouse_x / 100)
        createY = int(mouse_y / 100)

        self.initX = createX * 100 + 50
        self.initY = createY * 100 + 50

    def update(self, frame_time, plant_x):
        global life_time
        distance = Attack.RUN_SPEED_PPS * frame_time
        self.total_frames += FRAMES_PER_ACTION * ACTION_PER_TIME * frame_time

        if self.show == True:
            if(self.x < 700):
                self.x += distance
            else:
                self.x = plant_x+10
                self.show = False
        else:
            life_time += frame_time
            if life_time >= 1.5:
                life_time = 0.0
                self.show = True

    def showCheck(self, show):
        self.show = show

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x-13, self.y-13, self.x+13, self.y+13

    def draw_bb(self):
        draw_rectangle(*self.get_bb())