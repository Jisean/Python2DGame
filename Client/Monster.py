import random
import json
import os


from pico2d import *

import game_framework


name = "Monster"


class Monster:
    image = None
    (LEFT, RIGHT) = (0,1)



    def __init__(self,x,y):
        self.x, self.y = x , y
        self.frame = random.randint(0,4)
        self.state = self.RIGHT
        self.dir = 1
        if Monster.image == None:
            Monster.image = load_image('Mob1.png')

    def update(self):
        self.frame = (self.frame + 1) % 4
        self.x += (self.dir * 5)
        if self.x > 800:
            self.dir = -1
            self.x = 800
            self.state = self.LEFT
        elif self.x < 0:
            self.dir = 1
            self.x = 0
            self.state = self.RIGHT

        delay(0.02)

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
