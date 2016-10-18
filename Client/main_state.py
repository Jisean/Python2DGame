import random
import json
import os

from pico2d import *

import game_framework
import title_state
import Player
import Background



name = "MainState"

player = None
background = None
grass = None
font = None



class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



def enter():
    global player, grass, background
    player = Player.Player()
    background = Background.Background()
    grass = Grass()
    pass


def exit():
    global player, grass, background
    del(player)
    del(background)
    del(grass)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            player.handle_inputs(event)
            background.handle_inputs(event,player.x)
    pass


def update():
    player.update()
    background.update()
    delay(0.04)
    pass


def draw():
    clear_canvas()
    background.draw()
    grass.draw()
    player.draw()
    update_canvas()
    pass





