import random
import json
import os
import time


from pico2d import *

import game_framework
from MonsterBullet import MonsterBullet


name = "Hunter"
bulletContainer = []

class Hunter:
    image = None

    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPPED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPPED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    (LEFT_ATT,RIGHT_ATT, RIGHT_STAND,LEFT_STAND) = (0,1,2,3)



    def __init__(self,x,y):
        self.x, self.y = x , y
        self.startx, self.starty = x, y
        self.sx = x
        self.sy = y
        self.frame = random.randint(0,4)
        self.state = self.LEFT_STAND
        self.life_time = 0.0
        self.total_frames = 0.0
        self.sound1 = load_wav('HunterAtt.wav')
        self.sound1.set_volume(32)
        self.sound2 = load_wav('HunterAttFire.wav')
        self.sound2.set_volume(32)

        self.dir = 1
        if Hunter.image == None:
            self.image = load_image('Mob2.png')

    def update(self,frame_time):

        self.life_time += frame_time
        distance = self.RUN_SPEED_PPS * frame_time
        self.total_frames += self.FRAMES_PER_ACTION * self.ACTION_PER_TIME * frame_time

        self.frames()

        self.sx = self.x - self.bg.window_left / 2
        self.sy = self.y - self.bg.window_bottom / 2

        if self.player.x < self.sx:
            self.dir = -1
            if self.player.x + 200 < self.sx:
                self.state = self.LEFT_STAND
            else:
                self.state = self.LEFT_ATT

        else:
            self.dir = 1
            if self.player.x - 200 > self.sx:
                self.state = self.RIGHT_STAND
            else:
                self.state = self.RIGHT_ATT

        for bullet in bulletContainer:
            bullet.update(frame_time)
            if bullet.x > 800 or bullet.x < 0 or bullet.y > 600 :
                bulletContainer.remove(bullet)


        #delay(0.02)

    def frames(self):
        if self.state == self.RIGHT_STAND or self.state == self.LEFT_STAND:
            self.frame = int(self.total_frames) % 13

        elif self.state == self.RIGHT_ATT or self.state == self.LEFT_ATT :
            self.frame = int(self.total_frames) % 17
            if self.frame == 0 :
                self.sound1.play(1)
            if self.frame == 8 :
                self.sound2.play(1)
                if self.state == self.LEFT_ATT :
                    bulletContainer.append(MonsterBullet(self.sx - 30, self.sy, self.dir))
                elif self.state == self.RIGHT_ATT:
                    bulletContainer.append(MonsterBullet(self.sx + 30, self.sy, self.dir))


    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.sx, self.sy,90,90)
        for bullet in bulletContainer:
            bullet.draw()

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.sx - 30, self.sy - 50, self.sx + 30, self.sy + 20

    def set_background(self, bg):
        self.bg = bg

    def set_player(self, player):
        self.player = player

    def get_Bullet(self):
        return bulletContainer
