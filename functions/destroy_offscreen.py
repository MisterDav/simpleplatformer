import global_vars

def init(self):
    pass

def update(self):
    tile_id, tile_flags = global_vars.current_map.get_tile_raw_pos(*self.p.tuple())
    if tile_id == -1:
        self.kill()