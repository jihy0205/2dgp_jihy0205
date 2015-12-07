from pico2d import *
import random

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
        pass
    def update(self):
        pass
    def draw(self):
        pass
    def get_bb(self):
        pass
    def draw_bb(self):
        pass