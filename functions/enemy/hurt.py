import global_vars

def init(self):
    self.attack = 4

def update(self):
    player = global_vars.sprite_groups["player"].sprites()[0]
    dist = self.p.distance(player.p)
    if dist <= 7:
        player.hurt(self, self.attack)