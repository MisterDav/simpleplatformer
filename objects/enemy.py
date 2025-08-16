from game_object import Game_Object

class Enemy(Game_Object):
    def __init__(self,x,y):
        
        animation = {
            "idle": [(0,0)],
            "move": [(8,0), (0,0), (16,0), (0,0)],
            "jump": [(24,0)],
            "fall": [(0,8), (8,8), (16,8), (24,8)]
        }

        super().__init__(x,y,8,8,group="enemy",spritesheet="assets/cloak_skull.png",animation=animation,start_anim="idle")
        self.add_function("health", "enemy.walk", "enemy.hurt")