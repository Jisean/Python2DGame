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
from Hunter import Hunter
from Boss import Boss



name = "MainState"

player = None
background = None
font = None
bgm = None
mobsound = None
bosssound1 = None
bosssound2 = None
monstercon = []
terraincon = []
huntercon = []
bosscon = []
timer = 0



def enter():
    global player, terrain, background, monstercon, terraincon, font, huntercon, boss, timer, bgm, mobsound, bosssound1, bosssound2
    font = load_font('ComicSans.ttf')
    bgm = load_music('stage.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()

    mobsound = load_wav('monsterdead.wav')
    mobsound.set_volume(32)

    bosssound1 = load_wav('bosshit.wav')
    bosssound1.set_volume(32)

    bosssound2 = load_wav('bossdie.wav')
    bosssound2.set_volume(32)

    terrain_data_file = open('terrain_data.txt')
    terrain_data = json.load(terrain_data_file)
    terrain_data_file.close()

    player = Player.Player()
    background = Background.Background()

    background.set_center_object(player)
    player.set_background(background)
    player.set_font(font)

    for terrain_num in terrain_data :
        terrain = Terrain(terrain_data[terrain_num]['num'],terrain_data[terrain_num]['x'],terrain_data[terrain_num]['y'])
        terrain.set_background(background)
        terraincon.append(terrain)

    monstercon = [Monster(300+(80*i), (240-(20*i))) for i in range(4)]
    for monster in monstercon:
        monster.set_background(background)

    hunter1 = Hunter(650,170)
    hunter1.set_background(background)
    hunter1.set_player(player)

    hunter2 = Hunter(1200, 210)
    hunter2.set_background(background)
    hunter2.set_player(player)

    huntercon.append(hunter1)
    huntercon.append(hunter2)

    boss = Boss(2350,380)
    boss.set_background(background)
    boss.set_player(player)
    boss.set_font(font)
    bosscon.append(boss)


    pass


def exit():
    global player, terraincon, background, monstercon, font, huntercon, boss, bgm
    bgm.stop()
    del(bgm)
    del(player)
    del(background)
    del(terraincon)
    del(monstercon)
    del(huntercon)
    del(font)
    if boss != None :
        del(boss)
    pass


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            player.handle_inputs(event)
            background.handle_inputs(event)
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
                mobsound.play(1)
                player.score += 20
        for hunter in huntercon:
            if collide(hunter, bullet):
                player.get_Bullet().remove(bullet)
                huntercon.remove(hunter)
                mobsound.play(1)
                player.score += 50
        for boss in bosscon:
            if collide(boss, bullet) :
                player.get_Bullet().remove(bullet)
                boss.HP -= 1
                bosssound1.play(1)
                if(boss.HP <=0) :
                    bosssound2.play(1)
                    bosscon.remove(boss)
                    player.score += 500

    for hunter in huntercon:
        for mobbullet in hunter.get_Bullet() :
            if collide(player,mobbullet) :
                hunter.get_Bullet().remove(mobbullet)
                player.HP -= 1
                if player.HP <=0 :
                    player.HP = 10
                    player.x, player.y = 100, 150
                    player.score -= 50
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
    for hunter in huntercon:
        hunter.update(frame_time)

    for boss in bosscon:
        boss.update(frame_time)
        for mobbullet in boss.get_Bullet() :
            if collide(player,mobbullet) :
                boss.get_Bullet().remove(mobbullet)
                player.HP -= 1
                if player.HP <=0 :
                    player.HP = 10
                    player.x, player.y = 100, 150
                    player.score -= 50


    delay(0.04)
    pass


def draw(frame_time):
    clear_canvas()
    background.draw()
    for terrain in terraincon:
        terrain.draw()
    player.draw()
    for mob in monstercon:
        mob.draw()
    for hunter in huntercon:
        hunter.draw()
    for boss in bosscon:
        boss.draw()
    update_canvas()
    pass





