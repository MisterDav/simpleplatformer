from game_object import Game_Object
from vtypes.flist import FList
import random
import pygame
import global_vars
import math

class Particle(Game_Object):
    def __init__(
        self,x,y,
        angle_start=90,angle_end=180,
        speed=0.5,speed_change=0.0,
        num=25,
        color=(255,255,255,255),dc=(0,0,0,0),
        size=3,ds=-0.05,
        lifetime=100,
        emission_time=3
    ):

        super().__init__(x,y,0,0)
        self.x = x
        self.y = y
        self.rx_off = 0
        self.ry_off = 0
        self.speed = speed
        self.speed_change = speed_change
        self.angle_start = angle_start
        self.angle_end = angle_end
        self.num = num
        self.color = color
        self.dc = dc
        self.size = size
        self.ds = ds
        self.lifetime = lifetime

        self.spawn_timer = 0
        self.time_to_spawn = emission_time / num
    
        self.active_particle = []

    def add_new(self):
        if self.num != 0: self.num -= 1
        else: return
        rnd_x = random.uniform(-self.rx_off, self.rx_off) + self.x
        rnd_y = random.uniform(-self.ry_off, self.ry_off) + self.y
        rnd_a = random.uniform(self.angle_start, self.angle_end)
        ch_x = math.cos(math.radians(rnd_a))
        ch_y = -math.sin(math.radians(rnd_a))
        self.active_particle.append([rnd_x,rnd_y,self.size,rnd_a,self.speed,self.color,self.lifetime,(ch_x,ch_y)])

    def update(self):
        super().update()
        self.spawn_timer += 1
        if self.spawn_timer >= self.time_to_spawn:
            self.add_new()
        self.spawn_timer %= self.time_to_spawn

        delete_queue = []
        for x in range(len(self.active_particle)):
            particle = self.active_particle[x]

            # Changes the position based on the speed and pre-calculated angle.
            particle[0] += particle[7][0] * particle[4]
            particle[1] += particle[7][1] * particle[4]

            # Changes the speed, size, and color of the particle.
            particle[2] += self.ds
            particle[4] += self.speed_change
            # particle[5] # Doesn't do aynthing yet.

            # Display the particle.
            pygame.draw.circle(global_vars.screen, particle[5], self.get_pos_camera(particle[0], particle[1]), particle[2])

            # Decrements the lifetime of the particle.
            particle[6] -= 1
            if particle[6] <= 0:
                delete_queue.append(x)
        
        for d in delete_queue[::-1]:
            del self.active_particle[d]

        if self.num == 0 and len(self.active_particle) == 0:
            self.kill()

        pass


class Afterimage(Game_Object):
    def __init__(self,x,y,lifetime,object_afterimage,tint=(0,0,0,150),fade=False):
        self.x = x
        self.y = y
        self.lifetime = lifetime
        self.object = object_afterimage
        self.tint = tint
        self.fade = fade
        super().__init__(x,y,0,0)
    
    def update(self):

        if self.lifetime <= 0:
            self.kill()
        surface = self.object.animation.surface.copy()
        surface = pygame.transform.flip(surface, self.object.animation.flip_x, self.object.animation.flip_y)
        surface.fill(self.tint, special_flags=pygame.BLEND_RGBA_SUB)
        global_vars.screen.blit(surface,self.get_pos_camera(self.x,self.y))

        self.lifetime -= 1