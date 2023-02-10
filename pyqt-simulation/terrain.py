from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from abc import ABC, abstractmethod

class Terrain(ABC):
    def __init__(self, x, y, size):
        self.type = None
        self.x = x
        self.y = y
        self.color = None
        self.h = size
        self.w = size
        self.speedMultiplier = 1

class Water(Terrain):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.type = "W"
        self.color = QColor(0, 0, 255)
        self.speedMultiplier = 0.1

class Mountains(Terrain):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.type = "M"
        self.color = QColor(165,42,42)
        self.speedMultiplier = 0.5