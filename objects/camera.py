from game_object import Game_Object
import global_vars
import math

def lerp(a, b, t):
    return a+(b-a)*t

class Camera(Game_Object):
    def __init__(self, x=0, y=0, object_lock=None, smoothing=False):
        super().__init__(x,y,0,0)
        self.x = x
        self.y = y
        self.display_x = 0
        self.display_y = 0
        self.object_lock = object_lock
        self.smoothing = smoothing

    def update(self):
        super().update()
        if self.object_lock == False: return

        if isinstance(self.object_lock, Game_Object):
                
            x = int(self.object_lock.rect.centerx)
            y = int(self.object_lock.rect.centery)
        
        elif isinstance(self.object_lock, list):
            length = len(self.object_lock)
            x = 0
            y = 0
            for obj in self.object_lock:
                x += obj.p.x
                y += obj.p.y
            x //= length
            y //= length
        
        if self.smoothing:
            self.x = lerp(self.x, x, 0.1)
            self.y = lerp(self.y, y, 0.05)
        else:
            self.x = x
            self.y = y

        self.display_x = int(self.x - global_vars.resolution[0] // 2)
        self.display_y = int(self.y - global_vars.resolution[1] // 2)