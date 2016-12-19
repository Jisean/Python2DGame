import json
import os

from pico2d import *


import game_framework



name = "Terrain"



class Terrain:
    image = None

    def __init__(self,tilenum,x,y):
        self.tilenum = tilenum
        self.x = x
        self.y = y
        self.sx = x
        self.sy = y
        if self.tilenum == 1 :
            if self.image == None:
                self.image = load_image('Tile1.png')
        if self.tilenum  == 2:
            if self.image == None:
                self.image = load_image('Tile2.png')
        if self.tilenum == 3:
            if self.image == None:
                self.image = load_image('Tile3.png')
        if self.tilenum == 4:
            if self.image == None:
                self.image = load_image('Tile4.png')
        if self.tilenum == 5:
            if self.image == None:
                self.image = load_image('Tile5.png')

    def update(self,frame_time):
        self.sx = self.x - self.bg.window_left/2
        self.sy = self.y - self.bg.window_bottom/2

    def draw(self):

        self.image.draw(self.sx, self.sy)
        ##self.image.draw(self.x, self.y)

    def get_bb(self):
        if self.tilenum == 1 :
            return self.sx - 48, self.sy - 20, self.sx + 48, self.sy + 20
        if self.tilenum == 2 :
            return self.sx - 40, self.sy - 20, self.sx + 40, self.sy
        if self.tilenum == 3:
            return self.sx - 368, self.sy - 70, self.sx + 368 , self.sy -20
        if self.tilenum == 4:
            return self.sx - 204, self.sy + 80, self.sx + 204, self.sy + 113
        if self.tilenum == 5:
            return self.sx - 96, self.sy + 20 , self.sx + 96, self.sy + 50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def set_background(self,bg):
        self.bg = bg
