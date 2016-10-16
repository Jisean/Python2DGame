import random
import json
import os

from pico2d import *

import game_framework
import title_state
import Player



name = "MainState"

player = None
grass = None
font = None



class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



def enter():
    global player,grass
    player = Player.Player()
    grass = Grass()
    pass


def exit():
    global player, grass
    del(player)
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
    pass


def update():
    player.update()
    delay(0.04)
    pass


def draw():
    clear_canvas()
    grass.draw()
    player.draw()
    update_canvas()
    pass





