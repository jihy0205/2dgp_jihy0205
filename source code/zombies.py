from pico2d import *
import random

zomby = None

class Zomby:

    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 3.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    image = None
    def __init__(self):
        self.image = load_image('z_walk.png')
        self.x, self.y = 750, 370
        self.frame =0
        self.dir = -1
        self.total_frames = 0.0

    def update(self):
        distance = Zomby.RUN_SPEED_PPS
        self.total_frames += 1.0
        self.frame = (self.frame + 1) % 8
        self.x -= 2
        self.total_frames += Zomby.FRAMES_PER_ACTION * Zomby.ACTION_PER_TIME
        self.frame = (self.frame+1)%9

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
