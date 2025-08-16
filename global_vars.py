import pygame
from vtypes.vector2 import Vector2

clock = None
screen = None
current_map = None
camera = None

background = (0,0,0)
background = (41,173,255)

#font = pygame.font.SysFont("Comic Sans MS", 15)

tile_size = Vector2(8,8)
delta_time = 1
resolution = (0,0)
just_pressed = []
gravity = 0.15
collision_flag = 0b0000000000000001
hazard_flag = 0b0000000000000010
sprite_groups = {
    "all_sprites": pygame.sprite.Group()
}