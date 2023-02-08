from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random
import sys
import window as win
import creatures as c

# Run
if __name__ == '__main__':
    app = QApplication([])
    maxWorldAge = 128319877
    maxX = 800
    maxY = 600
    width = 800
    height = 600
    numReds = 1
    numBlues = 100
    maxCreatureAge = 2000
    worldSpeed = 10
    window = win.Window(maxWorldAge, maxX, maxY, width, height, worldSpeed)
    theWorld = window.world

    theWorld.terrainList.append([200, 200])

    for i in range(numReds):
        newDot = c.RedDot(maxCreatureAge, 10)
        x = random.randrange(theWorld.maxX)
        y = random.randrange(theWorld.maxY)
        while not theWorld.emptyLocation(x, y):
            x = random.randrange(theWorld.maxX)
            y = random.randrange(theWorld.maxY)
        theWorld.addThing(newDot, x, y)

    for i in range(numBlues):
        newDot = c.BlueDot(maxCreatureAge, 10)
        x = random.randrange(theWorld.maxX)
        y = random.randrange(theWorld.maxY)
        while not theWorld.emptyLocation(x, y):
            x = random.randrange(theWorld.maxX)
            y = random.randrange(theWorld.maxY)
        theWorld.addThing(newDot, x, y)

    sys.exit(app.exec_())
