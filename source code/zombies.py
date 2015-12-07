from pico2d import *
import random

zomby = None

class Zomby:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    RUN_SPEED_KMPH = 3.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None
    gameover_image = None
    WALK, ATTACK, DIE, OVER = 1, 2, 3, 4

    def __init__(self):
        self.walk_image = load_image('z_walk.png')
        self.attack_image = load_image('z_eating.png')
        self.die_image = load_image('z_die.png')
        self.gameover_image = load_image('over.png')
        self.x, self.y = 800, (random.randint(0, 4)*100)+50
        self.walk_frame = random.randint(0, 5)
        self.eat_frame = 0
        self.die_frame = 0
        self.dir = -1
        self.total_frames = 0.0
        self.state = self.WALK
        self.atk = 10
        self.hp = 50

    def update(self, frame_time):
        distance = Zomby.RUN_SPEED_PPS
        self.total_frames += 1.0
        self.walk_frame = (self.walk_frame+1)%8
        self.eat_frame = (self.eat_frame+1)%5
        self.die_frame = (self.die_frame+1)%8
        if(self.state == self.WALK):
            self.x -= 2
        self.total_frames += Zomby.FRAMES_PER_ACTION * Zomby.ACTION_PER_TIME * frame_time


    def draw(self, frame_time):
        if self.state == self.WALK:
            self.walk_image.clip_draw(self.walk_frame*150, 0, 150, 150, self.x, self.y)
        if self.state == self.ATTACK:
            self.attack_image.clip_draw(self.eat_frame*150, 0, 150, 150, self.x, self.y)
        if self.state == self.DIE:
            self.die_image.clip_draw(self.die_frame*200, 0, 200, 200, self.x, self.y)
            if(self.die_frame == 1):
                self.die_frame = 2
        if self.state == self.OVER:
            self.gameover_image.draw(400, 300)

    def get_bb(self):
        return self.x-40, self.y-50, self.x+40, self.y+50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
