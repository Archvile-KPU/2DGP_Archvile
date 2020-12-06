from pico2d import *
import gfw
from player import Player
from player import Hud
from background import FixedBackground
from player import LaserBullet
from player import Arg

canvas_width = 800
canvas_height = 600

def enter():
    gfw.world.init(['bg', 'player', 'hud', 'bullet', 'bullet1', 'bullet2', 'bullet3', 'bullet4', 'bullet5'])
    
    bg = FixedBackground('e1m1_over.png')
    gfw.world.add(gfw.layer.bg, bg)
    
    global player
    player = Player()
    global hud
    hud = Hud()
    player.pos = bg.center
    player.bg =bg
    bg.target = player
    gfw.world.add(gfw.layer.player, player)
    gfw.world.add(gfw.layer.hud, hud)

def exit():
    pass

def update():
    gfw.world.update()

    #if Arg.HP < 0:
        #end_game()
        

def draw():
    gfw.world.draw()

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    if e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    player.handle_event(e)

if __name__ == '__main__':
    gfw.run_main()
