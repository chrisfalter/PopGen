from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
import random
from abc import ABC,abstractmethod

# Class for anything that moves around.
class MovingObject(ABC):
    def __init__(self, maxAge, speed):
        self.world = None
        self.dead = False
        self.birthYear = None
        self.age = 0
        self.maxAge = maxAge
        self.speed = speed
        self.xPos = None
        self.yPos = None
        self.offsetList = [(-speed, speed), (0, speed), (speed, speed),
                           (-speed, 0),                     (speed, 0),
                           (-speed, -speed), (0, -speed), (speed, -speed)]

    def tryToMove(self):
        randomOffsetIndex = random.randrange(len(self.offsetList))
        randomOffset = self.offsetList[randomOffsetIndex]
        nextX = self.xPos + randomOffset[0]
        nextY = self.yPos + randomOffset[1]
        while not (0 <= nextX < self.world.maxX and \
                   0 <= nextY < self.world.maxY):
            randomOffsetIndex = random.randrange(len(self.offsetList))
            randomOffset = self.offsetList[randomOffsetIndex]
            nextX = self.xPos + randomOffset[0]
            nextY = self.yPos + randomOffset[1]

        if self.world.emptyLocation(nextX, nextY):
            self.xPos = nextX
            self.yPos = nextY

    def tryToBreed(self, thing):
        randomOffsetIndex = random.randrange(len(self.offsetList))
        randomOffset = self.offsetList[randomOffsetIndex]
        nextX = self.xPos + randomOffset[0]
        nextY = self.yPos + randomOffset[1]
        while not (0 <= nextX < self.world.maxX and \
                   0 <= nextY < self.world.maxY):
            randomOffsetIndex = random.randrange(len(self.offsetList))
            randomOffset = self.offsetList[randomOffsetIndex]
            nextX = self.xPos + randomOffset[0]
            nextY = self.yPos + randomOffset[1]

        if self.world.emptyLocation(nextX, nextY):
            baby = self.world.addThing(thing, nextX, nextY)

    @abstractmethod
    def liveALittle(self):
        return

# Red
class RedDot(MovingObject):
    def __init__(self, maxAge, speed):
        super().__init__(maxAge, speed)
        self.geneLvl = 255
        self.color = QColor(self.geneLvl, 0, 0)
        self.babies = 0

    def tryToBreed(self, baby):
        randomOffsetIndex = random.randrange(len(self.offsetList))
        randomOffset = self.offsetList[randomOffsetIndex]
        nextX = self.xPos + randomOffset[0]
        nextY = self.yPos + randomOffset[1]
        while not (0 <= nextX < self.world.maxX and \
                   0 <= nextY < self.world.maxY):
            randomOffsetIndex = random.randrange(len(self.offsetList))
            randomOffset = self.offsetList[randomOffsetIndex]
            nextX = self.xPos + randomOffset[0]
            nextY = self.yPos + randomOffset[1]

        if self.world.emptyLocation(nextX, nextY):
            if self.geneLvl > 15:
                baby.geneLvl = self.geneLvl - 10
                baby.color = QColor(baby.geneLvl, 0, 0)
            else:
                baby.geneLvl = self.geneLvl
                baby.color = QColor(baby.geneLvl, 0, 0)
            self.world.addThing(baby, nextX, nextY)

    def liveALittle(self):
        if self.age <= self.maxAge:
            if self.age >= (self.maxAge/2) and self.babies < 2:
                baby = RedDot(self.maxAge, self.speed)
                self.tryToBreed(baby)
                self.babies += 1
            self.tryToMove()
            self.age += 1
        else:
            self.dead = True

# Blue
class BlueDot(MovingObject):
    def __init__(self, maxAge, speed):
        super().__init__(maxAge, speed)
        self.color = QColor(0, 0, 205)
        self.babies = 0

    def liveALittle(self):
        if self.age <= self.maxAge:
            if self.age >= (self.maxAge/2) and self.babies < 1:
                baby = BlueDot(self.maxAge, self.speed)
                self.tryToBreed(baby)
                self.babies += 1
            self.tryToMove()
            self.age += 1
        else:
            self.dead = True