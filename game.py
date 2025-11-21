import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np

pygame.init()
font = pygame.font.Font('arial.ttf', 25)

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3 
    DOWN = 4

    Point = namedtuple('Point',  'x, y')

    #colors
    WHITE = (255, 255, 255)
    RED = (200, 0,0)
    BLUE1 = (0, 0, 255)
    BLUE2 = (0,100,255)
    BLACK = (0,0,0)

    BLOCK_SIZE = 20
    SPEED = 40


class SnakeGameAI:
    def __init__(self):
        pass