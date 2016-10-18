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


    def __init__(self):
        self.x, self.y = 400,300
        if Background.image == None:
            Background.image = load_image('Stage1BG.png')

    def draw(self):
        self.image.draw(self.x, self.y)