import game_framework
import main_state
from pico2d import *


name = "TitleState"
image = None
start = None
esc = None
cursor = None
bgm = None
PosX = 100


def enter():
    global image, start, esc, cursor, bgm
    image = load_image('title.png')
    start = load_image('Start.png')
    esc = load_image('Exit.png')
    cursor = load_image('Cursor.png')
    bgm = load_music('menu.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()
    pass


def exit():
    global image, start, esc, cursor, bgm
    bgm.stop()
    del(image)
    del(start)
    del(esc)
    del(cursor)
    del(bgm)
    pass


def handle_events(frame_time):
    global PosX
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                if PosX == 100:
                    PosX = 530
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                if PosX == 530:
                    PosX = 100
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                if PosX == 100:
                    game_framework.change_state(main_state)
                elif PosX == 530:
                    game_framework.quit()
    pass


def draw(frame_time):
    global PosX
    clear_canvas()
    image.draw(400,300)
    start.draw(200,50)
    esc.draw(600,50)
    cursor.draw(PosX, 50)
    update_canvas()
    pass

def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass






