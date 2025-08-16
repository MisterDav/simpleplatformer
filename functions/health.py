from vtypes.vector2 import Vector2
import global_vars

def init(self):
    self.add_function("physics")
    self.hp = 100
    self.hurt_timer = 0
    self.invulnerable_timer = 0
    self.hurt_angle = Vector2(0,0)
    
    def hurt(self, obj, factor):
        if self.invulnerable_timer > 0: return
        self.invulnerable_timer = 60
        self.hp -= factor
        self.hurt_timer = 5
        self.hurt_angle = self.p.direction(obj.p)
    
    self.hurt = hurt.__get__(self)

def update(self):
    if self.hurt_timer > 0:
        self.animation.tint = (255,255,255,255)
        self.hurt_timer -= 1
        self.v += self.hurt_angle * 50
    if self.invulnerable_timer > 0:
        self.invulnerable_timer -= 1