from pico2d import *
import random

plant = None
flower = None
attack1 = None
<<<<<<< HEAD
isAttack = True
dist = 0
count = 0

class Plant1:
    PIXEL_PER_METER = (10.0 / 0.15)           # 10 pixel 15 cm
    RUN_SPEED_KMPH = 3.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    def __init__(self):
        self.x, self.y = 0, 0
        self.frame = 0
        self.image = load_image('plant1.png')
        self.count =0
        self.hp=50
        self.isTrue = False

    def update(self, frame_time):
        self.frame = (self.frame + 1) % 8
        print("plant: %f" % (frame_time))

    def draw(self, frame_time):
=======
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
>>>>>>> origin/master
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def get_bb(self):
        return self.x-30, self.y-40, self.x+30, self.y+40

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Flower:
<<<<<<< HEAD
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

    def update(self, frame_time):
        self.frame = (self.frame + 1)% 8
        print("flower: %f" %(frame_time))

    def draw(self, frame_time):
=======

    def __init__(self):
        self.x, self.y = 250, 450
        self.frame = 0
        self.image = load_image('flower.png')

    def update(self):
        self.frame = (self.frame + 1)% 8

    def draw(self):
>>>>>>> origin/master
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

    def get_bb(self):
        return self.x-30, self.y-40, self.x+30, self.y+40

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Potato:
<<<<<<< HEAD
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

    def update(self, frame_time):
        self.frame = (self.frame + 1)% 4
        print("Potato: %f" %(frame_time))

    def draw(self, frame_time):
=======


    def __init__(self):
        self.x, self.y = 250, 250
        self.frame = 0
        self.image = load_image('potato.png')

    def update(self):
        self.frame = (self.frame + 1)% 4

    def draw(self):
>>>>>>> origin/master
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

    def get_bb(self):
        return self.x-30, self.y-40, self.x+30, self.y+40

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Bomb:
<<<<<<< HEAD
    PIXEL_PER_METER = (10.0 / 0.15)           # 10 pixel 15 cm
    RUN_SPEED_KMPH = 3.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
=======

>>>>>>> origin/master
    def __init__(self):
        self.x, self.y = 250, 150
        self.frame =0
        self.image = load_image('bomb.png')
<<<<<<< HEAD
        self.left = self.x - 150
        self.bottom = self.y - 150
        self.right = self.x + 150
        self.top = self.y + 150

    def update(self, frame_time):
        self.frame = (self.frame + 1) % 4
        print("bomb: %f" % (frame_time))

    def explosion(self):
        return self.left, self.bottom, self.right, self.top

    def draw(self, frame_time):
=======

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
>>>>>>> origin/master
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

    def get_bb(self):
        return self.x-20, self.y-20, self.x+20, self.y+20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

<<<<<<< HEAD
class Attack:
    def __init__(self):
        self.image = load_image('attack.png')
        self.frame =0
        self.x, self.y = Plant1().x+10, Plant1().y+20
        self.dir = 1
        self.atk = 10

    def update(self, frame_time):
        pass

    def draw(self, frame_time):
=======
class Attack1:

    PIXEL_PER_METER = (10.0 / 0.15)           # 10 pixel 15 cm
    RUN_SPEED_KMPH = 3.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.image = load_image('attack.png')
        self.frame =0
        self.x, self.y = Plant1().x+30, Plant1().y+20
        self.dir = 1
        self.total_frames = 0.0

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
>>>>>>> origin/master
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x-13, self.y-13, self.x+13, self.y+13

    def draw_bb(self):
        draw_rectangle(*self.get_bb())