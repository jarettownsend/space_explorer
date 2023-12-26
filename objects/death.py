import pygame
from objects.colors import *

class death():
    def __init__ (self):
        self.count = 0
        self.counter_surface = pygame.Surface((150, 50))
        self.counter_surface.fill(BLACK)