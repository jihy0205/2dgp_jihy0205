from pico2d import *
import random
import game_framework

class Sun:
    PIXEL_PER_METER = (10.0 / 0.15)           # 10 pixel 15 cm
    RUN_SPEED_KMPH = 3.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    image = None

    def __init__(self):
        self.image = load_image('sun.png')
        self.font = load_font('ConsolaMangun.ttf', 10)
        self.x = random.randint(150, 450)
        self.y = 0
        self.frame = 0.0
        self.dir = -1
        self.total_frames = 0.0
        self.score = 0
        self.money = 0

    def update(self, frame_time):
        distance = Sun.RUN_SPEED_PPS * frame_time
        self.total_frames += Sun.FRAMES_PER_ACTION * Sun.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 2

        if(self.y <= 0):
            self.y -= distance

    def getMoney(self):
        return self.money

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

    def get_bb(self):
        return self.x - 20, self.y-20, self.x+20, self.y-20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())