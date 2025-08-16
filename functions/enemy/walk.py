import pygame
import math
import global_vars

from vtypes.vector2 import Vector2
from functions.helper import collision

def init(self):
    self.add_function("physics")
    self.movement_speed = 0.05
    self.direction = Vector2(1,0) * self.movement_speed

def update(self):
    self.a = Vector2(0, self.gravity) * global_vars.delta_time
    self.a += self.direction * global_vars.delta_time
    if (self.t_right and self.direction.x > 0) or (self.t_left and self.direction.x < 0):
        self.direction.x *= -1
    self.animation.flip_x = self.direction.x < 0
    pass