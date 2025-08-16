import pygame
import global_vars
from vtypes.vector2 import Vector2

class Map():
    def __init__(self, size, tile_map, map_path=None, parallax_backgrounds=[], p_lock_x = False, p_lock_y = True):

        self.tile_map = pygame.image.load(tile_map)
        self.tile_map_size = Vector2(self.tile_map.get_width(), self.tile_map.get_height()) / size
        self.tile_size = Vector2(size, size)
        self.tile_flags = {
            0: global_vars.collision_flag,
            10: global_vars.collision_flag,
            11: global_vars.collision_flag,
            26: global_vars.collision_flag,
            27: global_vars.collision_flag,
            28: global_vars.collision_flag,
            42: global_vars.hazard_flag | global_vars.collision_flag
        }

        self.parallax_backgrounds = []
        for bg_img in parallax_backgrounds:
            loaded_img = pygame.image.load(bg_img[0])
            #a = bg_img[1] * 15
            #loaded_img.fill((a,a,a,25), special_flags=pygame.BLEND_SUB)
            self.parallax_backgrounds.append( (loaded_img.convert_alpha(), bg_img[1]) )

        self.surface = pygame.Surface( (size, size) , pygame.SRCALPHA)
        self.map = []

        self.p_lock_x = int(not p_lock_x)
        self.p_lock_y = int(not p_lock_y)

    def update(self): 

        # Display parallax background
        screen_size = global_vars.resolution
        if global_vars.camera != None:
            cam = global_vars.camera
            for a in self.parallax_backgrounds:
                global_vars.screen.blit(a[0], (
                        int(cam.display_x / -a[1]) % screen_size[0] * self.p_lock_x,
                        int(cam.display_y / -a[1]) % screen_size[1] * self.p_lock_y,
                    )
                )
                global_vars.screen.blit(a[0], (
                        (int(cam.display_x / -a[1]) % screen_size[0] - screen_size[0]) * self.p_lock_x,
                        (int(cam.display_y / -a[1]) % screen_size[1] - screen_size[1]) * self.p_lock_y,
                    )
                )


        # Display the map.
        for y in range( len(self.map) ):
            for x in range( len(self.map[y])):
                self.surface.fill((0,0,0,0))
                id_pos = self.map[y][x]

                if id_pos == 0:
                    continue
                id_x = (id_pos % self.tile_map_size.x) * -self.tile_size.x
                id_y = (id_pos // self.tile_map_size.y) * -self.tile_size.y
                self.surface.blit(self.tile_map, (id_x, id_y))

                if global_vars.camera:
                    global_vars.screen.blit( self.surface, 
                        ( (x*8)-global_vars.camera.display_x, (y*8)-global_vars.camera.display_y ) 
                    )
                else:
                    global_vars.screen.blit( self.surface, (x*8, y*8) )
    
    def get_tile(self, x, y):
        #print(x,y)
        if y >= len(self.map) or y < 0: return -1, global_vars.collision_flag
        if x >= len(self.map[y]) or x < 0: return -1, global_vars.collision_flag
        tile_flags = 0x00
        tile_id = self.map[y][x]
        if tile_id in self.tile_flags.keys():
            tile_flags = self.tile_flags[tile_id]
        return tile_id, tile_flags

    def get_tile_raw_pos(self, x, y):
        return self.get_tile(int(x // self.tile_size.x), int(y // self.tile_size.y))

    def set_collision_pts(self, *collisions):
        for k,v in collisions.items():
            self.collision[k] = v

    def load_map(self, path):
        with open(path,"r") as file:
            new_map = []
            for y in file.readlines():
                new_line = []
                for x in y.replace("\n","").split(","):
                    if int(x) == -1: new_line.append(0)
                    else: new_line.append(int(x))
                new_map.append(new_line)
        self.map = new_map

    def save_map(self, path):
        pass

