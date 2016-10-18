import random
import json
import os

from pico2d import *

import game_framework



name = "Background"



class Background:
    image = None
    ScrollX = 0
    ScrollY = 0
    LeftKey = False
    RightKey = False

    def __init__(self):
        self.x, self.y = 100,300
        self.speed = 0
        self.left = 0

        if Background.image == None:
            Background.image = load_image('Stage1BG.png')

    def handle_inputs(self, event, x):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            self.LeftKey = True
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            self.LeftKey = False
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            self.RightKey = True
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            self.RightKey = False
    def update(self):
        global LeftKey,RIghtKey, ScrollX
        if self.LeftKey == True:
            self.ScrollX += 20
        if self.RightKey == True:
            self.ScrollX -= 20


    def draw(self):
        global ScrollX
        for self.x in range(0,4):
            #self.image.draw(400 + self.ScrollX *1, self.y)
            if 0 == self.x % 2:
                self.image.draw((self.ScrollX * 0.1) + 800 * self.x, 300)
            else:
                self.image.draw((self.ScrollX * 0.1) + 800 * self.x, 300)