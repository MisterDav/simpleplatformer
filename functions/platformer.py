import pygame
import math
import global_vars

from vtypes.vector2 import Vector2
from functions.helper import collision

def init(self): 
    self.add_function("physics") # Add the required physics dependencies 

    self.c_left = pygame.K_LEFT
    self.c_right = pygame.K_RIGHT
    self.c_jump = pygame.K_z
    self.c_dash = pygame.K_x

    self.jump_timer_max = 5
    self.coyote_timer_max = 3
    self.buffer_timer_max = 5

    self.move_factor = 0.1
    self.jump_factor = 0.55
    self.air_penalty = 1
    self.jump_timer = self.jump_timer_max
    self.coyote_timer = self.coyote_timer_max
    self.buffer_timer = 0
    self.holding_jump = False
    self.buffer_jump = False


def update(self):
    # Apply gravity
    if not self.holding_jump:
        self.a = Vector2(0, self.gravity) * global_vars.delta_time
    else:
        self.a = Vector2(0, self.gravity / 1.5) * global_vars.delta_time

    # Apply acceleration for the player's movement.
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[self.c_left]:
        self.a.x += -self.move_factor*self.air_penalty * global_vars.delta_time
    elif pressed_keys[self.c_right]:
        self.a.x += self.move_factor*self.air_penalty * global_vars.delta_time
    if pressed_keys[self.c_jump] and \
    (self.grounded or self.jump_timer > 0 or self.coyote_timer > 0) and not \
    (self.holding_jump and not self.buffer_jump):
        self.grounded = False
        self.jump_timer -= global_vars.delta_time
        self.a.y += -self.jump_factor * global_vars.delta_time

    if not pressed_keys[self.c_jump] and self.jump_timer > 0 and self.coyote_timer <= 0:
        self.jump_timer = 0
        self.buffer_jump = False

    if self.t_above:
        self.jump_timer = 0
        self.buffer_jump = False
    
    if self.v.y > 0 and not self.holding_jump:
        if pressed_keys[self.c_jump]:
            self.buffer_jump = True
        else:
            self.buffer_jump = False
    if self.jump_timer <= 0 and self.v.y < 0:
        self.buffer_jump = False

    if self.jump_timer <= 0 or self.grounded:
        if pressed_keys[self.c_jump]:
            self.holding_jump = True
        else:
            self.holding_jump = False 


    if self.t_under:
        self.jump_timer = self.jump_timer_max
        self.coyote_timer = self.coyote_timer_max
    else:
        if self.coyote_timer > 0: self.coyote_timer -= global_vars.delta_time
        else: self_grounded = False

    if pressed_keys[self.c_dash] and self.grounded:
        self.move_factor = 0.2
        self.v_cap.x = 1.4
    elif not pressed_keys[self.c_dash] and self.grounded:
        self.jump_timer = self.jump_timer_max
        self.move_factor = 0.1
        self.v_cap.x = 1
    
    # Player animation
    if abs(self.v.x) <= 0.1 and abs(self.v.y) == 0: self.animation.change_animation("idle")
    elif abs(self.v.x) > 0.1 and abs(self.v.y) <= 0.1: self.animation.change_animation("move")
    elif self.v.y < -0.1: self.animation.change_animation("jump")
    elif self.v.y >= self.v_cap.y * 0.3: self.animation.change_animation("fall")

    if self.v.x < -0.1: self.animation.flip_x = True
    elif self.v.x > 0.1: self.animation.flip_x = False
    if not self.grounded: 
        self.air_penalty = 0.8
    else:
        self.air_penalty = 1