import random
import json
import os
import time


from pico2d import *

import game_framework
from BossBullet import BossBullet


name = "Boss"
bulletContainer = []

class Boss:
    image = None

    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPPED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPPED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    (ATT,STAND) = (0,1)



    def __init__(self,x,y):
        self.x, self.y = x , y
        self.startx, self.starty = x, y
        self.sx = x
        self.sy = y
        self.frame = random.randint(0,42)
        self.state = self.STAND
        self.life_time = 0.0
        self.total_frames = 0.0
        self.HP = 30
        self.sound = load_wav('bossatt.wav')
        self.sound.set_volume(32)

        self.dir = 1
        if Boss.image == None:
            self.image = load_image('boss2.png')

    def update(self,frame_time):

        self.life_time += frame_time
        distance = self.RUN_SPEED_PPS * frame_time
        self.total_frames += self.FRAMES_PER_ACTION * self.ACTION_PER_TIME * frame_time

        self.frames()

        self.sx = self.x - self.bg.window_left / 2
        self.sy = self.y - self.bg.window_bottom / 2

        if self.player.x < self.sx:
            self.dir = -1
            if self.player.x + 600 < self.sx:
                self.state = self.STAND
            else:
                self.state = self.ATT

        for bullet in bulletContainer:
            bullet.update(frame_time)
            if bullet.x > 800 or bullet.x < 0 or bullet.y > 600 :
                bulletContainer.remove(bullet)


        #delay(0.02)

    def frames(self):
        if self.state == self.STAND :
            self.frame = int(self.total_frames) % 16

        elif self.state == self.ATT :
            self.frame = int(self.total_frames) % 42
            if self.frame == 18 :
                self.sound.play(1)
                bulletContainer.append(BossBullet(self.sx - 30, self.sy - 50, self.dir))
            if self.frame == 24 :
                bulletContainer.append(BossBullet(self.sx - 30, self.sy - 50, self.dir))
            if self.frame == 28 :
                bulletContainer.append(BossBullet(self.sx - 30, self.sy - 50, self.dir))
            if self.frame == 32 :
                bulletContainer.append(BossBullet(self.sx - 30, self.sy - 50, self.dir))


    def draw(self):
        self.image.clip_draw(self.frame * 150, self.state * 150, 150, 150, self.sx, self.sy, 300, 300)
        for bullet in bulletContainer:
            bullet.draw()
        if self.player.x + 600 < self.sx:
            self.font.draw(760,100," ")
        else:
            self.font.draw(650,40, "Boss HP :%d" % self.HP, (255, 0, 0))

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.sx - 100, self.sy - 250, self.sx + 150, self.sy + 200

    def set_background(self, bg):
        self.bg = bg

    def set_player(self, player):
        self.player = player

    def get_Bullet(self):
        return bulletContainer

    def set_font(self,font):
        self.font = font
