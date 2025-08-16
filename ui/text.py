import pygame
import global_vars

class Text():
    def __init__(self, text, x, y):
        self.x = x
        self.y = y
        self.text = text
        self.surface = global_vars.font.render(text, False, (0,0,0)) 

    def update(self):
        screen.blit(text_surface, (self.x, self.y))