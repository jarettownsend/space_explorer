import pygame
from objects.death import death
from levels.homepage import homepage
from levels.level_1 import level_1
from levels.level_2 import level_2
from levels.level_3 import level_3
from levels.credits import credits


# pygame setup
pygame.init()

# Set up display
screen_width, screen_height = 1300, 700
screen = pygame.display.set_mode((screen_width, screen_height))
screen_image = pygame.image.load('images/background.png')
screen_image = pygame.transform.scale(screen_image, (screen_width, screen_height))
clock = pygame.time.Clock()
dt = 0

# Set up Death Counter
death = death()

# Play Levels

homepage(screen, screen_image, screen_width)
death = level_1(death, screen, screen_image, clock, dt, screen_width, screen_height)
death = level_2(death, screen, screen_image, clock, dt, screen_width, screen_height)
death = level_3(death, screen, screen_image, clock, dt, screen_width, screen_height)
credits(screen, screen_image, screen_width, death)

