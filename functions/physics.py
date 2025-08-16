import pygame
import math
import global_vars

from vtypes.vector2 import Vector2
from functions.helper import collision

def init(self):
    self.v = Vector2(0,0)
    self.a = Vector2(0,0)
    self.friction = -0.01
    self.a_cap = 3
    self.v_cap = Vector2(1, 3)
    self.gravity = global_vars.gravity
    self.grounded = False

    self.t_above = False
    self.t_left = False
    self.t_right = False
    self.t_under = False

def update(self):

    # Apply velocity from acceleration
    self.a = self.a.min(self.a_cap)
    self.a = self.a.max(-self.a_cap)
    self.a += self.v * self.friction

    self.v.x *= pow(0.90, global_vars.delta_time)
    if self.a.magnitude() < 0.01:
        self.a = Vector2(0,0)
    
    # Update position from velocity
    self.v = self.v.min(self.v_cap)
    self.v = self.v.max(-self.v_cap)
    self.v += self.a
    if self.v.magnitude() < 0.05:
        self.v = Vector2(0,0)
    
    self.p += self.v

    self.t_under = collision.check_point(self, 2, 8) or collision.check_point(self, 6, 8)
    if self.t_under: 
        self.v.y = 0
        self.a.y = 0
        self.grounded = True
        collision.snap_to_tile(self,0,-1)
    self.t_above = collision.check_point(self, 4, 1)
    if self.t_above:
        collision.snap_to_tile(self,0,1)
        self.v.y = 0
        self.a.y = 0
    self.t_right = collision.check_point(self, 8, 6) or collision.check_point(self, 8, 2)
    if self.t_right: 
        collision.snap_to_tile(self,-1,0)
        self.v.x = 0
    self.t_left = collision.check_point(self, 0, 6) or collision.check_point(self, 0, 2)
    if self.t_left: 
        collision.snap_to_tile(self,1,0)
        self.v.x = 0