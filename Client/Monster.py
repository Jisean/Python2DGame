import random
import json
import os


from pico2d import *

import game_framework


name = "Monster"


class Monster:
    image = None

    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPPED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPPED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    (LEFT, RIGHT) = (0,1)



    def __init__(self,x,y):
        self.x, self.y = x , y
        self.startx, self.starty = x, y
        self.sx = x
        self.sy = y
        self.frame = random.randint(0,4)
        self.state = self.RIGHT
        self.life_time = 0.0
        self.total_frames = 0.0

        self.dir = 1
        if Monster.image == None:
            Monster.image = load_image('Mob1.png')

    def update(self,frame_time):

        self.life_time += frame_time
        distance = self.RUN_SPEED_PPS * frame_time
        self.total_frames += self.FRAMES_PER_ACTION * self.ACTION_PER_TIME * frame_time

        self.frame = int(self.total_frames) % 4
        self.x += (self.dir * 5)

        self.sx = self.x - self.bg.window_left / 2
        self.sy = self.y - self.bg.window_bottom / 2

        if self.x > self.startx + 200:
            self.dir = -1
            self.x = self.startx + 200
            self.state = self.LEFT
        elif self.x < self.startx - 200:
            self.dir = 1
            self.x = self.startx - 200
            self.state = self.RIGHT

        #delay(0.02)

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.sx, self.sy)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.sx - 20, self.sy - 20, self.sx + 20, self.sy + 20

    def set_background(self, bg):
        self.bg = bg
