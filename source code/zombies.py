from pico2d import *
import random

zomby = None

class Zomby:
    PIXEL_PER_METER = (10.0 / 0.15)           # 10 pixel 15 cm
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    RUN_SPEED_KMPH = 1.3                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None
    WALK, ATTACK, DIE, OVER = 1, 2, 3, 4

    def __init__(self):
        self.walk_image = load_image('z_walk.png')
        self.attack_image = load_image('z_eating.png')
        self.die_image = load_image('z_die.png')
        self.x, self.y = 800, (random.randint(0, 4)*100)+50
        self.walk_frame = random.randint(0, 5)
        self.eat_frame = 0
        self.die_frame = 0
        self.dir = -1
        self.state = self.WALK
        self.atk = 10
        self.hp = 50
        self.life_time = 0.0
        self.total_frames = 0.0

    def update(self, frame_time):
        distance = Zomby.RUN_SPEED_PPS * frame_time
        self.total_frames += Zomby.FRAMES_PER_ACTION * Zomby.ACTION_PER_TIME * frame_time
        self.walk_frame = int(self.total_frames) % 8
        self.eat_frame = int(self.total_frames) % 5
        self.die_frame = int(self.total_frames) % 8
        if(self.state == self.WALK):
            if(self.x >= 30):
                self.x -= distance

    def draw(self, frame_time):
        if self.state == self.WALK:
            self.walk_image.clip_draw(self.walk_frame*150, 0, 150, 150, self.x, self.y)
        if self.state == self.ATTACK:
            self.attack_image.clip_draw(self.eat_frame*150, 0, 150, 150, self.x, self.y)
        if self.state == self.DIE:
            self.die_image.clip_draw(self.die_frame*200, 0, 200, 200, self.x, self.y)
            if(self.die_frame == 1):
                self.die_frame = 2

    def get_bb(self):
        return self.x-40, self.y-50, self.x+40, self.y+50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
