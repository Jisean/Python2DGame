import random
import json
import os

from pico2d import *

import game_framework
import title_state
import Player
import Background
from Monster import Monster



name = "MainState"

player = None
background = None
grass = None
font = None
monstercon = []



class Grass:
    def __init__(self):
        self.image = load_image('stagetile.png')

    def draw(self):
        self.image.draw(400, 300)



def enter():
    global player, grass, background,monstercon
    player = Player.Player()
    background = Background.Background()
    grass = Grass()
    monstercon = [Monster(100+(35*i), 240) for i in range(2)]
    pass


def exit():
    global player, grass, background, monstercon
    del(player)
    del(background)
    del(grass)
    del(monstercon)
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

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def update():
    player.update()
    background.update()
    for mob in monstercon:
        mob.update()
    for bullet in player.get_Bullet():
        for mob in monstercon:
            if collide(mob, bullet):
                player.get_Bullet().remove(bullet)
                monstercon.remove(mob)
    delay(0.04)
    pass


def draw():
    clear_canvas()
    background.draw()
    grass.draw()
    player.draw()
    for mob in monstercon:
        mob.draw()
    update_canvas()
    pass





