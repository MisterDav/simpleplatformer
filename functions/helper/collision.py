import math
import global_vars
from vtypes.vector2 import Vector2

def check_point(self, off_x, off_y):
    point_position = self.p + Vector2(off_x, off_y)
    tile_id, tile_flags = global_vars.current_map.get_tile_raw_pos(*point_position.tuple())
    #global_vars.screen.set_at((point_position.floor()).tuple(), (255,255,0,255))
    #print(tile_flags)
    return tile_flags & global_vars.collision_flag == 0

def snap_to_tile(self,x,y):
    size_x = global_vars.tile_size.x
    size_y = global_vars.tile_size.y

    if x == 1: self.p.x = math.ceil(self.p.x/size_x)*size_x
    elif x == -1: self.p.x = math.floor(self.p.x/size_x)*size_x
    if y == 1: self.p.y = math.ceil(self.p.y/size_y)*size_y
    elif y == -1: self.p.y = math.floor(self.p.y/size_y)*size_y