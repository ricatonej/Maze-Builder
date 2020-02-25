"""
@author: Johnny Ricatone
@filename: maze.py

This is essentially the file in which you make a maze.
All of it is handled behind the scenes, mazes are a 2D array with 1 or 0, 0 being a wall, and 1
being valid "floorspace"

Pygame is required for graphics, but otherwise not necessary.
"""

graphics = True
try:
    import pygame
except ImportError:
    graphics = False


class Maze:
    def __init__(self, width, height):
        self.size = width * height
        self.width = width
        self.height = height
        self.maze = [[0 for i in range(height)] for i in range(width)]

    def generatemaze(self):
        pass