from game_object import Game_Object
from objects.item_container import Item_Container
from objects.particle import Afterimage

class Player(Game_Object):
    def __init__(self,x,y):
        
        animation = {
            "idle": [(0,0)],
            "move": [(8,0), (0,0), (16,0), (0,0)],
            "jump": [(24,0)],
            "fall": [(0,8)]
        }

        self.abilities = Item_Container(max_size = 3)

        super().__init__(x,y,8,8,group="player",spritesheet="assets/cloak_skull.png",animation=animation,start_anim="idle")
        self.add_function("platformer", "physics", "health", "respawn_debug")

    def update(self):
        super().update()