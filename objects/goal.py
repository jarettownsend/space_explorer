import pygame

class Goal():
    def __init__(self, x, y, width=100, height=100):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        actual_image = pygame.image.load('images/goal.png')
        self.image = pygame.transform.scale(actual_image, (width, height))
        self.rect = pygame.Rect(x, y, width, height)