from pico2d import *
import gfw
import gobj

health = 100
pistol_ammo = 17
shotgun_ammo = 20
weapon = 1


class Arg:
    def __init__(self):
        pass
    def update(self):
        global health
        HP = health

class LaserBullet:
    SIZE = 40
    def __init__(self, x, y, speed):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = x, y
        self.dx = speed
        self.dy = speed
        self.image = gfw.image.load('res/bullet.png')
        self.power = 100

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):

        global action
        if action == 6: #U
            self.y += self.dy * gfw.delta_time
        elif action == 7: #D
            self.y -= self.dy * gfw.delta_time
        elif action == 2: #UR
            self.x += self.dx * gfw.delta_time
            self.y += self.dy * gfw.delta_time
        elif action == 0: #DR
            self.x += self.dx * gfw.delta_time
            self.y -= self.dy * gfw.delta_time
        elif action == 4: #R
            self.x += self.dx * gfw.delta_time
        elif action == 3: #UL
            self.x -= self.dx * gfw.delta_time
            self.y += self.dy * gfw.delta_time
        elif action == 1: #DL
            self.x -= self.dx * gfw.delta_time
            self.y -= self.dy * gfw.delta_time
        elif action == 5: #L
            self.x -= self.dx * gfw.delta_time

        if self.y > get_canvas_height() + LaserBullet.SIZE:
            self.remove()

    def remove(self):
        gfw.world.remove(self)

    def get_bb(self):
        hw = self.image.w // 2
        hh = self.image.h // 2
        return self.x - hw, self.y - hh, self.x + hw, self.y + hh

class ShotgunShell:
    SIZE = 50
    def __init__(self, x, y, speed):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = x, y
        self.dx = speed
        self.dy = speed
        self.image = gfw.image.load('res/shell.png')
        self.power = 200

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):

        global action
        if action == 6: #U
            self.y += self.dy * gfw.delta_time
        elif action == 7: #D
            self.y -= self.dy * gfw.delta_time
        elif action == 2: #UR
            self.x += self.dx * gfw.delta_time
            self.y += self.dy * gfw.delta_time
        elif action == 0: #DR
            self.x += self.dx * gfw.delta_time
            self.y -= self.dy * gfw.delta_time
        elif action == 4: #R
            self.x += self.dx * gfw.delta_time
        elif action == 3: #UL
            self.x -= self.dx * gfw.delta_time
            self.y += self.dy * gfw.delta_time
        elif action == 1: #DL
            self.x -= self.dx * gfw.delta_time
            self.y -= self.dy * gfw.delta_time
        elif action == 5: #L
            self.x -= self.dx * gfw.delta_time

        if self.y > get_canvas_height() + ShotgunShell.SIZE:
            self.remove()

    def remove(self):
        gfw.world.remove(self)

    def get_bb(self):
        hw = self.image.w // 2
        hh = self.image.h // 2
        return self.x - hw, self.y - hh, self.x + hw, self.y + hh    

class Hud:
    def __init__(self):
        self.image_hud = gfw.image.load('res/HUD.png')
        self.image_bar = gfw.image.load('res/BarHud.png')
        self.image_num = gfw.image.load('res/num.png')
        self.image_numsmall = gfw.image.load('res/numsmall.png')
        self.death = load_wav('res/sound/sfx/dspldeth.wav')
        self.death.set_volume(50)

    def enter(self):
        self.time = 0
        
    def draw(self):
        global health
        global weapon
        global pistol_ammo
        global shotgun_ammo
        x = 0


        hp1d = health % 10
        hp2d = health // 10
        hp3d = health // 100

        ammo1d = pistol_ammo % 10
        ammo2d = pistol_ammo // 10
        ammo3d = pistol_ammo // 100

        shell1d = shotgun_ammo % 10
        shell2d = shotgun_ammo // 10
        shell3d = shotgun_ammo // 100

        if health >= 80:
            x = 0
        elif health >= 50:
            x = 1
        elif health >= 20:
            x = 2
        elif health > 0:
            x = 3
        else:
            x = 4
        
        x = x * 200
        #print(health)
        self.image_bar.draw(400,33)
        self.image_hud.clip_draw(x, 0, 200, 200, 400, 30)
        self.image_num.clip_draw(hp1d * 200, 0, 200, 200, 255, 33)
        self.image_num.clip_draw(hp2d * 200, 0, 200, 200, 230, 33)
        self.image_num.clip_draw(hp3d * 200, 0, 200, 200, 205, 33)

        if weapon == 1:
            self.image_num.clip_draw(ammo1d * 200, 0, 200, 200, 150, 33)
            self.image_num.clip_draw(ammo2d * 200, 0, 200, 200, 125, 33)
            self.image_num.clip_draw(ammo3d * 200, 0, 200, 200, 100, 33)
        elif weapon == 2:
            self.image_num.clip_draw(shell1d * 200, 0, 200, 200, 150, 33)
            self.image_num.clip_draw(shell2d * 200, 0, 200, 200, 125, 33)
            self.image_num.clip_draw(shell3d * 200, 0, 200, 200, 100, 33)

        self.image_numsmall.clip_draw(ammo1d * 100, 0, 100, 100, 650, 48)
        self.image_numsmall.clip_draw(ammo2d * 100, 0, 100, 100, 640, 48)
        self.image_numsmall.clip_draw(ammo3d * 100, 0, 100, 100, 630, 48)

        self.image_numsmall.clip_draw(shell1d * 100, 0, 100, 100, 650, 38)
        self.image_numsmall.clip_draw(shell2d * 100, 0, 100, 100, 640, 38)
        self.image_numsmall.clip_draw(shell3d * 100, 0, 100, 100, 630, 38)

        if health <= 0:
            self.death.play(1)
            delay(2)
            gfw.quit()
        

    def update(self):
        pass

class PistolRun:
    @staticmethod
    def get(player):
        if not hasattr(PistolRun, 'singleton'):
            PistolRun.singleton = PistolRun()
            PistolRun.singleton.player = player
        return PistolRun.singleton

    def __init__(self):
        self.image_idle = gfw.image.load('res/marine.png')
        self.death = load_wav('res/sound/sfx/dspldeth.wav')
        self.death.set_volume(50)

    def enter(self):
        self.time = 0
        self.fidx = 0

    def exit(self):
        pass

    def draw(self):
        x = self.fidx * 100
        y = action * 100
        self.image_idle.clip_draw(x, y, 100, 100, *self.player.pos)

    def update(self):
        self.time += gfw.delta_time
        dx, dy = self.player.delta

        if dx != 0:
            if dx < 0:
                self.player.dir = -1
            elif dx > 0:
                self.player.dir = 1

        x, y = self.player.pos
        x += dx * self.player.speed_move * gfw.delta_time
        y += dy * self.player.speed_move * gfw.delta_time

        px,py = x,y
        bg_l, bg_b, bg_r, bg_t = self.player.get_bb()
        x = clamp(bg_l, x, bg_r)
        y = clamp(bg_b, y, bg_t)

        self.player.pos = x, y

        frame = self.time * 8#(self.player.speed_move * 0.1)
        self.fidx = int(frame) % 8

    def updateDelta(self, ddx, ddy):
        dx, dy = self.player.delta
        dx += ddx
        dy += ddy
        self.player.updateAction(dx, dy, ddx, ddy)
        self.player.delta = dx, dy

    def updateAction(self, dx, dy, ddx, ddy):
        global action
        #global health
        #global health
        #if health <= 0:
            #self.death.play(1)
            #end_game()
        if dx == 0 and dy > 0:
            action = 6 #U
            #health += 1
        if dx == 0 and dy < 0:
            action = 7 #D
        if dx > 0 and dy > 0:
            action = 2 #UR
        if dx > 0 and dy < 0:
            action = 0 #DR
        if dx > 0 and dy == 0:
            action = 4 #R
        if dx < 0 and dy > 0:
            action = 3 #UL
        if dx < 0 and dy < 0:
            action = 1 #DL
        if dx < 0 and dy == 0:
            action = 5 #L

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Player.KEYDOWN_MAP:
            self.player.updateDelta(*Player.KEYDOWN_MAP[pair])
        elif pair in Player.KEYUP_MAP:
            self.player.updateDelta(*Player.KEYUP_MAP[pair])
        elif pair == Player.KEYDOWN_x:
            global pistol_ammo
            if pistol_ammo > 0:
                self.player.set_state(PistolFire)
        elif pair == Player.KEYDOWN_2:
            global weapon
            weapon = 2
            self.player.set_state(ShotgunRun)
        #elif pair == Player.KEYDOWN_z:
            #self.player.set_state(DashState)
        #elif pair == Player.KEYDOWN_z:
            #self.player.set_state(DashState)

class ShotgunRun:
    @staticmethod
    def get(player):
        if not hasattr(ShotgunRun, 'singleton'):
            ShotgunRun.singleton = ShotgunRun()
            ShotgunRun.singleton.player = player
        return ShotgunRun.singleton

    def __init__(self):
        self.image_idle = gfw.image.load('res/marine.png')
        #self.death = load_wav('res/sound/sfx/dspldeth.wav')
        #self.death.set_volume(50)

    def enter(self):
        self.time = 0
        self.fidx = 0

    def exit(self):
        pass

    def draw(self):
        x = self.fidx * 100
        y = action * 100
        self.image_idle.clip_draw(x, y, 100, 100, *self.player.pos)

    def update(self):
        self.time += gfw.delta_time
        dx, dy = self.player.delta

        if dx != 0:
            if dx < 0:
                self.player.dir = -1
            elif dx > 0:
                self.player.dir = 1

        x, y = self.player.pos
        x += dx * self.player.speed_move * gfw.delta_time
        y += dy * self.player.speed_move * gfw.delta_time

        px,py = x,y
        bg_l, bg_b, bg_r, bg_t = self.player.get_bb()
        x = clamp(bg_l, x, bg_r)
        y = clamp(bg_b, y, bg_t)

        self.player.pos = x, y

        frame = self.time * 8#(self.player.speed_move * 0.1)
        self.fidx = int(frame) % 8

    def updateDelta(self, ddx, ddy):
        dx, dy = self.player.delta
        dx += ddx
        dy += ddy
        self.player.updateAction(dx, dy, ddx, ddy)
        self.player.delta = dx, dy

    def updateAction(self, dx, dy, ddx, ddy):
        global action
        #global health
        #global health
        #if health <= 0:
            #self.death.play(1)
            #end_game()
        if dx == 0 and dy > 0:
            action = 6 #U
            #health += 1
        if dx == 0 and dy < 0:
            action = 7 #D
        if dx > 0 and dy > 0:
            action = 2 #UR
        if dx > 0 and dy < 0:
            action = 0 #DR
        if dx > 0 and dy == 0:
            action = 4 #R
        if dx < 0 and dy > 0:
            action = 3 #UL
        if dx < 0 and dy < 0:
            action = 1 #DL
        if dx < 0 and dy == 0:
            action = 5 #L

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Player.KEYDOWN_MAP:
            self.player.updateDelta(*Player.KEYDOWN_MAP[pair])
        elif pair in Player.KEYUP_MAP:
            self.player.updateDelta(*Player.KEYUP_MAP[pair])
        elif pair == Player.KEYDOWN_x:
            global pistol_ammo
            if shotgun_ammo > 0:
                self.player.set_state(ShotgunFire)
        elif pair == Player.KEYDOWN_1:
            global weapon
            weapon = 1
            self.player.set_state(PistolRun)
        #elif pair == Player.KEYDOWN_z:
            #self.player.set_state(DashState)
        #elif pair == Player.KEYDOWN_z:
            #self.player.set_state(DashState)


class PistolFire:
    @staticmethod
    def get(player):
        if not hasattr(PistolFire, 'singleton'):
            PistolFire.singleton = PistolFire()
            PistolFire.singleton.player = player
        return PistolFire.singleton

    def __init__(self):
        self.image_attack = gfw.image.load('res/shoottokill.png')
        self.pistol = load_wav('res/sound/sfx/dspistol.wav')
        self.pistol.set_volume(50)
    
    def enter(self):
        self.time = 0
        self.fidx = 0
        global health
        health -= 10
        global pistol_ammo
        pistol_ammo -= 1
        self.pistol.play(1)

        self.fire()

    def fire(self):
        x, y = self.player.pos
        bullet = LaserBullet(x, y, 400)
        gfw.world.add(gfw.layer.bullet, bullet)

    def exit(self):
        pass

    def draw(self):

        x = self.fidx * 100
        y = action * 100
        self.image_attack.clip_draw(x, y, 100, 100, *self.player.pos)
        if self.fidx == 3: #fire rate
            self.player.set_state(PistolRun)
        
    def update(self):
        self.time += gfw.delta_time
        dx, dy = self.player.delta

        if dx != 0:
            if dx < 0:
                self.player.dir = -1
            elif dx > 0:
                self.player.dir = 1

        x, y = self.player.pos
        x += dx * self.player.speed_move * gfw.delta_time
        y += dy * self.player.speed_move * gfw.delta_time

        self.player.pos = x, y

        frame = self.time * 8#(self.player.speed_move * 0.1)
        self.fidx = int(frame) % 8

    def updateDelta(self, ddx, ddy):
        dx, dy = self.player.delta
        dx += ddx
        dy += ddy
        #self.player.updateAction(dx, dy, ddx, ddy)
        self.player.delta = dx, dy
        
    def handle_event(self,e):
        pair = (e.type, e.key)
        if pair in Player.KEYDOWN_MAP:
            self.player.updateDelta(*Player.KEYDOWN_MAP[pair])
        elif pair in Player.KEYUP_MAP:
            self.player.updateDelta(*Player.KEYUP_MAP[pair])

class ShotgunFire:
    @staticmethod
    def get(player):
        if not hasattr(ShotgunFire, 'singleton'):
            ShotgunFire.singleton = ShotgunFire()
            ShotgunFire.singleton.player = player
        return ShotgunFire.singleton

    def __init__(self):
        self.image_attack = gfw.image.load('res/shoottokill.png')
        self.shotgun = load_wav('res/sound/sfx/dsdshtgn.wav')
        self.shotgun.set_volume(50)
    
    def enter(self):
        self.time = 0
        self.fidx = 0
        global health
        health -= 10
        global shotgun_ammo
        shotgun_ammo -= 1
        self.shotgun.play(1)

        self.fire()

    def fire(self):
        x, y = self.player.pos
        bullet1 = ShotgunShell(x, y, 400)
        bullet2 = ShotgunShell(x+5, y+5, 400)
        bullet3 = ShotgunShell(x+5, y-5, 400)
        bullet4 = ShotgunShell(x-5, y+5, 400)
        bullet5 = ShotgunShell(x-5, y+5, 400)
        gfw.world.add(gfw.layer.bullet1, bullet1)
        gfw.world.add(gfw.layer.bullet2, bullet2)
        gfw.world.add(gfw.layer.bullet3, bullet3)
        gfw.world.add(gfw.layer.bullet4, bullet4)
        gfw.world.add(gfw.layer.bullet5, bullet5)

    def exit(self):
        pass

    def draw(self):

        x = self.fidx * 100
        y = action * 100
        self.image_attack.clip_draw(x, y, 100, 100, *self.player.pos)
        if self.fidx == 3: #fire rate
            self.player.set_state(ShotgunRun)
        
    def update(self):
        self.time += gfw.delta_time
        dx, dy = self.player.delta

        if dx != 0:
            if dx < 0:
                self.player.dir = -1
            elif dx > 0:
                self.player.dir = 1

        x, y = self.player.pos
        x += dx * self.player.speed_move * gfw.delta_time
        y += dy * self.player.speed_move * gfw.delta_time

        self.player.pos = x, y

        frame = self.time * 8#(self.player.speed_move * 0.1)
        self.fidx = int(frame) % 8

    def updateDelta(self, ddx, ddy):
        dx, dy = self.player.delta
        dx += ddx
        dy += ddy
        #self.player.updateAction(dx, dy, ddx, ddy)
        self.player.delta = dx, dy
        
    def handle_event(self,e):
        pair = (e.type, e.key)
        if pair in Player.KEYDOWN_MAP:
            self.player.updateDelta(*Player.KEYDOWN_MAP[pair])
        elif pair in Player.KEYUP_MAP:
            self.player.updateDelta(*Player.KEYUP_MAP[pair])
    

class Player:
    KEYDOWN_MAP = {
        (SDL_KEYDOWN, SDLK_LEFT):   (-1,  0),
        (SDL_KEYDOWN, SDLK_RIGHT):  ( 1,  0),
        (SDL_KEYDOWN, SDLK_DOWN):   ( 0, -1),
        (SDL_KEYDOWN, SDLK_UP):     ( 0,  1),
    }
    KEYUP_MAP = {
        (SDL_KEYUP, SDLK_LEFT):     ( 1,  0),
        (SDL_KEYUP, SDLK_RIGHT):    (-1,  0),
        (SDL_KEYUP, SDLK_DOWN):     ( 0,  1),
        (SDL_KEYUP, SDLK_UP):       ( 0, -1),
    }
    KEYDOWN_x = (SDL_KEYDOWN, SDLK_x)
    KEYDOWN_1 = (SDL_KEYDOWN, SDLK_1)
    KEYDOWN_2 = (SDL_KEYDOWN, SDLK_2)
    image = None

    def __init__(self):
        self.pos = 400, 300
        #self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.image_idle = gfw.image.load('res/marine.png')
        self.speed_move = 100
        self.time = 0
        self.fidx = 0
        global action
        self.target = None
        action = 7
        self.delta = 0, 0
        self.state = None
        self.set_state(PistolRun)
        global health
        health = 100
        self.E1M1_music = load_wav('res/sound/music_D1/d-e1m1.wav')
        self.E1M1_music.set_volume(50)
        self.E1M1_music.repeat_play()
        global center_x, center_y
        center_x = get_canvas_width() // 2
        center_y = get_canvas_height() // 2

    def set_state(self, klass):
        if self.state != None:
            self.state.exit()
        self.state = klass.get(self)
        self.state.enter()

    def get_bb(self):
        hw = 20
        hh = 40
        x,y = self.pos
        return x - hw, y - hh, x + hw, y + hh

    def draw(self):
        self.state.draw()

    def update(self):
        self.state.update()

    def updateDelta(self, ddx, ddy):
        self.state.updateDelta(ddx, ddy)

    def updateAction(self, dx, dy, ddx, ddy):
        self.state.updateAction(dx, dy, ddx, ddy)

    def handle_event(self, e):
        self.state.handle_event(e)
