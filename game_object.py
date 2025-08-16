import pygame
import importlib
import global_vars
import math
from vtypes.vector2 import Vector2

class Animation():
    def __init__(self, spritesheet_path, visible_rect, animation, default_animation):
        self.surface = pygame.Surface(visible_rect, pygame.SRCALPHA)
        self.animation_data = animation
        self.animation_name = default_animation
        self.frame = 0
        self.time_scale = 0.1
        self.spritesheet = pygame.image.load(spritesheet_path).convert_alpha()
        self.flip_x = False
        self.flip_y = False
        self.tint = (0,0,0,0)

    def update(self):
        return_frame = None
        animation = self.animation_data[self.animation_name]
        animation_len = len(animation)
        self.frame += self.time_scale
        self.frame %= animation_len
        #print(self.frame)
        ax = animation[int(self.frame)][0]
        ay = animation[int(self.frame)][1]
        self.surface.fill((0,0,0,0))
        self.surface.blit(self.spritesheet, (ax*-1,ay*-1))
        self.surface.fill(self.tint, special_flags = pygame.BLEND_ADD)
        self.tint = (0,0,0,0)
        return self.surface
        
    def change_animation(self, animation):
        if animation == self.animation_name: return
        self.frame = 0
        self.animation_name = animation
    def pause_animation(self): pass
    def add_animation(self, animation:dict): pass
    def play_animation(self): pass
    def change_time_scale(self, time): pass

class Game_Object(pygame.sprite.Sprite):
    def __repr__(self):
        return f"{hex(id(self))}\n"\
               f"xy:{self.rect.topleft}"

    def __init__(self, x, y, rx, ry, group=None, spritesheet=None, animation=None, start_anim = "default"):
        pygame.sprite.Sprite.__init__(self, global_vars.sprite_groups["all_sprites"])

        if group != None:
            if group in list(global_vars.sprite_groups.keys()):
                global_vars.sprite_groups[group].add(self)
            else:
                new_group = pygame.sprite.Group()
                global_vars.sprite_groups[group] = new_group
                global_vars.sprite_groups[group].add(self)

        self.p = Vector2(x,y)
        self.respawn_pos = Vector2(x,y)
        self.v = Vector2(0,0)
        self.a = Vector2(0,0)

        self.rect = pygame.Rect( (x,y), (rx,ry) )
        self.tasks = []
        self.functions = []
        self.function_variables = {}
        
        if animation == None or spritesheet == None:
            self.animation = None
        else:
            self.animation = Animation(spritesheet, (rx,ry), animation, start_anim)

    def get_pos_camera(self, x, y):
        return x - global_vars.camera.display_x, y - global_vars.camera.display_y

    def respawn(self):
        self.p = self.respawn_pos

    def update(self):

        for function in self.functions:
            function(self)

        if self.animation != None:
            self.rect.topleft = self.p.tuple()
            frame = self.animation.update()
            frame = pygame.transform.flip(frame, self.animation.flip_x, self.animation.flip_y)
            disp_x = int(self.rect.topleft[0])
            disp_y = int(self.rect.topleft[1])
            if global_vars.camera != None:
                disp_x, disp_y = self.get_pos_camera(disp_x,disp_y)
            global_vars.screen.blit(frame, (disp_x, disp_y))

    def add_to_group(self, group): pass
    def remove_from_group(self, group): pass

    def add_function(self, *functions):
        for function in functions:
            module = importlib.import_module(f"functions.{function}")
            if not module.update in self.functions:
                module.init(self)
                self.functions.append(module.update)
    def remove_function(self, *functions):
        for function in functions:
            module = importlib.import_module(f"functions.{function}")
            if module in self.functions:
                del self.functions[ self.functions.index(module) ]

def load_game_objects(directory="objects"):
    pass