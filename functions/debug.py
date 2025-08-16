import pygame

def init(self):
    self.dbg_movement_factor = 0.3

def update(self):
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP]: self.p.y -= self.dbg_movement_factor
    if pressed_keys[pygame.K_DOWN]: self.p.y += self.dbg_movement_factor
    if pressed_keys[pygame.K_LEFT]: self.p.x -= self.dbg_movement_factor
    if pressed_keys[pygame.K_RIGHT]: self.p.x += self.dbg_movement_factor
    if pressed_keys[pygame.K_z]: self.dbg_movement_factor = 0.6
    else: self.dbg_movement_factor = 0.3