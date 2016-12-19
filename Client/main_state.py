import random
import json
import os

from pico2d import *

import game_framework
import title_state
import Player
import Background
from Terrain import Terrain
from Monster import Monster



name = "MainState"

player = None
background = None
font = None
monstercon = []
terraincon = []



def enter():
    global player, terrain, background, monstercon, terraincon, font
    font = load_font('ComicSans.ttf')
    terrain_data_file = open('terrain_data.txt')
    terrain_data = json.load(terrain_data_file)
    terrain_data_file.close()

    player = Player.Player()
    background = Background.Background()

    background.set_center_object(player)
    player.set_background(background)

    for terrain_num in terrain_data :
        terrain = Terrain(terrain_data[terrain_num]['num'],terrain_data[terrain_num]['x'],terrain_data[terrain_num]['y'])
        print(terrain_data[terrain_num])
        terrain.set_background(background)
        terraincon.append(terrain)

    monstercon = [Monster(100+(35*i), 240) for i in range(2)]
    for monster in monstercon:
        monster.set_background(background)
    pass


def exit():
    global player, terraincon, background, monstercon, font
    del(player)
    del(background)
    del(terraincon)
    del(monstercon)
    del(font)
    pass


def pause():
    pass


def resume():
    pass


def handle_events(frame_timezzz):
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

def update(frame_time):
    player.update(frame_time)
    background.update()
    for mob in monstercon:
        mob.update(frame_time)
    for bullet in player.get_Bullet():
        for mob in monstercon:
            if collide(mob, bullet):
                player.get_Bullet().remove(bullet)
                monstercon.remove(mob)
    for terrain in terraincon:
        terrain.update(frame_time)
        if collide(player,terrain) :
            if terrain.tilenum == 1 :
                player.y = terrain.y + 70
            if terrain.tilenum == 2 :
                player.y = terrain.y + 50
            if terrain.tilenum == 3:
                player.y = terrain.y + 30
            if terrain.tilenum == 4:
                player.y = terrain.y + 160
            if terrain.tilenum == 5:
                player.y = terrain.y + 100
            player.FALLING = False
            player.jumpacc = 5
    delay(0.04)
    pass


def draw(frame_time):
    clear_canvas()
    background.draw()
    for terrain in terraincon:
        terrain.draw()
        terrain.draw_bb()
    player.draw()
    player.draw_bb()
    font.draw(20,60,'x: %d' % player.x)
    font.draw(20,20,'y: %d' % player.y)
    for mob in monstercon:
        mob.draw()
    update_canvas()
    pass





