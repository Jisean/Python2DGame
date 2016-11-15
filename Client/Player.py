import random
import json
import os

from pico2d import *

import game_framework
from Bullet import Bullet


name = "Player"
bulletContainer =[]


class Player:
    image = None

    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPPED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPPED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    (LEFT_FALL,RIGHT_FALL,
     LEFT_JUMP, RIGHT_JUMP, LEFT_DOWN, RIGHT_DOWN,
     LEFT_UPATT, RIGHT_UPATT,LEFT_UP, RIGHT_UP,
     LEFT_ATT, RIGHT_ATT, LEFT_RUN,
     RIGHT_RUN, LEFT_STAND, RIGHT_STAND) = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

    MOVE = False
    UPSIDE = False
    DOWNSIDE = False
    ATT = False
    POSLEFT = False
    POSRIGHT = False
    PUSHLEFT = False
    PUSHRIGHT = False
    JUMP = False
    FALLING = False


    def __init__(self):
        self.x, self.y = 100, 240
        self.jumpacc = 5
        self.speed = 10
        self.frame = random.randint(0, 27)
        self.POSRIGHT = True
        self.MOVE = False
        self.state = self.RIGHT_STAND
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 1
        if Player.image == None:
            Player.image = load_image('Player.png')

    def handle_inputs(self,event):
        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            self.MOVE = True
            self.PUSHLEFT = True
            self.PUSHRIGHT = False
            self.POSLEFT = True
            self.POSRIGHT = False
            self.dir = -1
                # 왼이동
        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            self.MOVE = True
            self.PUSHLEFT = False
            self.PUSHRIGHT = True
            self.POSLEFT = False
            self.POSRIGHT = True
            self.dir = 1
                #오른이동
        elif(event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            self.MOVE = False
            self.PUSHLEFT = False
            self.PUSHRIGHT = False
                #왼이동후 정지
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            self.MOVE = False
            self.PUSHLEFT = False
            self.PUSHRIGHT = False
                #오른이동후 정지
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_z):
             self.ATT = True
                #공격
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_z):
            self.ATT = False
                #공격후 정지
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            self.UPSIDE = True
                #위 보기
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            self.UPSIDE = False
                #위 보기 정지
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            self.DOWNSIDE = True
                #숙이기
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            self.DOWNSIDE = False
                #숙이기 정지
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE) :
            self.JUMP = True
            self.frame = 0;
                #점프

    def states(self):
        if self.MOVE == True:
            if self.POSLEFT == True:
                self.state = self.LEFT_RUN
            elif self.POSRIGHT == True:
                self.state = self.RIGHT_RUN
        elif self.MOVE == False:
            if self.POSLEFT == True:
                if self.UPSIDE == True:
                    self.state = self.LEFT_UP
                elif self.DOWNSIDE == True:
                    self.state = self.LEFT_DOWN
                elif self.UPSIDE == False or self.DOWNSIDE == False:
                    self.state = self.LEFT_STAND
            elif self.POSRIGHT == True:
                if self.UPSIDE == True:
                    self.state = self.RIGHT_UP
                elif self.DOWNSIDE == True:
                    self.state = self.RIGHT_DOWN
                elif self.UPSIDE == False or self.DOWNSIDE == False:
                    self.state = self.RIGHT_STAND

        if self.ATT == True:
            if self.POSLEFT == True:
                if self.UPSIDE == True:
                    self.state = self.LEFT_UPATT
                elif self.UPSIDE == False:
                    self.state = self.LEFT_ATT
            elif self.POSRIGHT == True:
                if self.UPSIDE == True:
                    self.state = self.RIGHT_UPATT
                elif self.UPSIDE == False:
                    self.state = self.RIGHT_ATT

        if self.JUMP == True:
            if self.POSLEFT == True:
                self.state = self.LEFT_JUMP
            elif self.POSRIGHT == True:
                self.state = self.RIGHT_JUMP

            if self.frame > 7 :
                self.JUMP = False
                self.FALLING = True
        if self.FALLING == True:
            if self.POSLEFT == True:
                self.state = self.LEFT_FALL
            elif self.POSRIGHT == True:
                self.state = self.RIGHT_FALL

    def frames(self):
        if self.state == self.RIGHT_STAND or self.state == self.LEFT_STAND:
            self.frame = int(self.total_frames) % 27
        elif self.state == self.RIGHT_RUN:
            self.frame = int(self.total_frames) % 8
            self.x = min(800, self.x + self.speed)
        elif self.state == self.LEFT_RUN:
            self.frame = int(self.total_frames) % 8
            self.x = max(0, self.x - self.speed)
        elif self.state == self.LEFT_ATT or self.state == self.RIGHT_ATT or self.state == self.LEFT_UPATT or self.state == self.RIGHT_UPATT:
            self.frame = int(self.total_frames) % 2
            if(self.frame == 1):
                bulletContainer.append(Bullet(self.x, self.y, self.dir))
        elif self.state == self.LEFT_UP or self.state == self.RIGHT_UP or self.state == self.LEFT_DOWN or self.state == self.RIGHT_DOWN:
            self.frame = int(self.total_frames) % 1
        elif self.state == self.LEFT_JUMP or self.state == self.RIGHT_JUMP:
            self.frame = int(self.total_frames) % 9
            self.jumpacc = self.jumpacc + 2
            self.y = self.y + self.jumpacc
            if self.PUSHRIGHT == True:
                self.x = min(800, self.x + 10)
            elif self.PUSHLEFT == True:
                self.x = max(0, self.x - 10)

        elif self.state == self.LEFT_FALL or self.state == self.RIGHT_FALL:
            self.frame = int(self.total_frames) % 3
            self.y = max(240, self.y - self.jumpacc)
            if self.PUSHRIGHT == True:
                self.x = min(800, self.x + 10)
            elif self.PUSHLEFT == True:
                self.x = max(0, self.x - 10)



    def update(self, frame_time):
        self.states()
        if self.y == 240:
            self.FALLING = False
            self.jumpacc = 5

        for bullet in bulletContainer:
            bullet.update(frame_time)
            if bullet.GetPosX() > 800 or bullet.GetPosX() < 0 :
                bulletContainer.remove(bullet)

        self.life_time += frame_time
        distance = self.RUN_SPEED_PPS * frame_time
        self.total_frames += self.FRAMES_PER_ACTION * self.ACTION_PER_TIME * frame_time
        self.frames()
        #delay(0.02)

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)
        for bullet in bulletContainer:
            bullet.draw()

    def get_playerX(self):
        return self.x

    def get_playerY(self):
        return self.y

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def get_Bullet(self):
        return bulletContainer

