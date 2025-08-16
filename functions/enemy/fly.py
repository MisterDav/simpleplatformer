import pygame
import math
import global_vars

from vtypes.vector2 import Vector2
from functions.helper import collision

def init(self):
    self.fly_speed = 1
    self.wait_timer = 60
    self.fly_timer = 0
    self.locked_on_to = None

def update(self):
    
    # If it's in the wait period, then only decrement the timer.
    if self.wait_timer > 0:
        self.wait_timer -= 1
        return

    if self.locked_on_to == None:
        # When the timer is up, then try to fly toward the player.
        player = global_vars.sprite_groups["player"].sprites()[0]
        dist = self.p.distance(player.p)
        if dist < 10000:
            self.fly_timer = 100
            self.locked_on_to = player
    else:
        if self.fly_timer > 0:
            self.fly_timer -= 1
            self.p -= self.p.direction(self.locked_on_to.p) * self.fly_speed


