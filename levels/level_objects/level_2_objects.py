import pygame
from objects.player import Player
from objects.wall import Wall
from objects.spike import Spike
from objects.goal import Goal

# Player Attributes
player = Player(125, 625)

# Spike Attributes
spike_list = []
spike_def = [
    #[x, y, x_velocity, y_velocity]
    [100,500,150,0],
    [100,200,150,0],
    [250,350,150,0],
    [400,200,150,0],
    [400,300,150,0],
    [400,400,150,0],
    [550,250,150,0],
    [550,350,150,0],
    [550,450,150,0],
    [700,450,150,0],
    [750,400,150,0],
    [800,350,150,0],
    [850,300,150,0],
    [900,250,150,0],
    [950,200,150,0],
    [1000,150,150,0],
    [1050,100,150,0],
]
for spike in spike_def:
    spike = Spike(spike[0], spike[1],spike[2],spike[3])
    spike_list.append(spike)

# Wall Attributes
wall_list = []
wall_def = [
    # [x, y]
    [0,0],
    [0,100],
    [0,200],
    [0,300],
    [0,400],
    [0,500],
    [0,600],
    [300,600],
    [300,500],
    [300,400],
    [300,300],
    [300,200],
    [100,0],
    [200,0],
    [300,0],
    [400,0],
    [500,0],
    [600,0],
    [700,0],
    [800,0],
    [900,0],
    [1000,0],
    [600,100],
    [600,200],
    [600,300],
    [600,400],
    [400,600],
    [500,600],
    [600,600],
    [700,600],
    [800,600],
    [900,600],
    [1000,600],
    [1100,600],
    [1200,0],
    [1200,100],
    [1200,200],
    [1200,300],
    [1200,400],
    [1200,500],
    [1200,600],
]
for wall in wall_def:
    wall = Wall(wall[0], wall[1])
    wall_list.append(wall)

# Goal Attributes
Goal = Goal(1100, 0)