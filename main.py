import window
import map
import global_vars
from objects.player import Player
from objects.enemy import Enemy
from objects.camera import Camera
from objects.particle import Particle
from objects.item import Item

player = Player(48,128)
particle = Particle(48,128)
item = Item(128,88,0, attract = False)
global_vars.camera = Camera(player.p.x,player.p.y,object_lock=player,smoothing=True)
global_vars.current_map = map.Map(
    8, "assets/tilemap/sample.png", 
    parallax_backgrounds = [
        ("assets/background/parallax_test.png", 3)
    ]
)
global_vars.current_map.load_map("maps/test1-1.csv")

window.run()