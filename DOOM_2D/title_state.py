import gfw
from pico2d import *
import game_state

def enter():
    global image
    image = load_image('res/Doom_title_wide.png')
    global titlemusic
    titlemusic = load_wav('res/d-intro.wav')
    titlemusic.set_volume(50)
    titlemusic.play(1)
    

def update():
    pass

def draw():
    image.draw(400, 300)
    

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        global titlemusic
        titlemusic.set_volume(0)
        gfw.push(game_state)
def exit():
    global image
    del image

def pause():
    pass
def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()
