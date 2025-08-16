import pygame
import json
import importlib

import math
import map
import global_vars
import game_object
import ui


# Initialize all of the settings defined in settings.json
with open("settings.json", "r") as raw_winset:
    winset = json.loads( raw_winset.read() )
    window_resolution = tuple(winset["window_resolution"])
    internal_resolution = tuple(winset["internal_resolution"])
    global_vars.resolution = internal_resolution
    volume = winset["volume"]
    start_scene = winset["start_scene"]
    name = winset["name"]

# Initialize the pygame window from the given information.
pygame.init()
window = pygame.display.set_mode(window_resolution)
pygame.display.set_caption(name)
global_vars.screen = pygame.Surface(internal_resolution)
global_vars.clock = pygame.time.Clock()

def pfloor(op, points):
    power = pow(10, points)
    return math.floor(op*power)/power

def run():
    # Game loop
    running = True
    while running:

        global_vars.just_pressed = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                global_vars.just_pressed.append(event.key)

        global_vars.screen.fill(global_vars.background)

        pressed = pygame.key.get_pressed()
        global_vars.current_map.update()
        global_vars.sprite_groups["all_sprites"].update()
        global_vars.camera.update()

        scaled_display = pygame.transform.scale(global_vars.screen, window_resolution)
        window.blit(scaled_display, (0,0))
        pygame.display.flip()
        global_vars.delta_time = round((global_vars.clock.tick(60)/1000)*60, 1)


    pygame.quit()




if __name__ == "__main__":
    run()