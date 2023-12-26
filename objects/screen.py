import pygame

class Screen():
    def __init__(self, width=1300, height=700):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        image = pygame.image.load('images/screen.jpg')
        self.screen_image = pygame.transform.scale(image, (width, height))
        pygame.display.set_caption('Video Game')
        self.clock = pygame.time.Clock()