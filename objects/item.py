import global_vars
from game_object import Game_Object
from vtypes.vector2 import Vector2

class Item(Game_Object):
    def __init__(self, x, y, id, attract=False, attract_dist=32, active=True):

        self.id = id
        self.attract = attract
        self.active = active
        self.attract_dist = attract_dist
        super().__init__(x,y,8,8,group="items",spritesheet="assets/items.png", animation={"default": [(id*8,0)]})
        
        self.add_function("physics")

    def update(self):

        if self.active:
            self.a = Vector2(0, self.gravity)
            player = global_vars.sprite_groups["player"].sprites()[0]
            dist = self.p.distance(player.p)
            if dist < 64 and self.attract:
                self.remove_function("physics")
                self.p -= self.p.direction(player.p) * 3

            if dist < 8:
                self.kill()
            super().update()