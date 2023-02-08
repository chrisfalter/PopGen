from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random
import creatures as c

class World(QFrame):

    msg2statusbar = pyqtSignal(str)

    def __init__(self, maxWorldAge, maxX, maxY, worldSpeed):
        super(World, self).__init__()

        self.timer = QBasicTimer()
        self.setStyleSheet("background-image: url('PopGen/pyqt-simulation/background.png')")
        self.setFocusPolicy(Qt.StrongFocus)

        self.maxX = maxX
        self.maxY = maxY
        self.grid = []

        self.terrainGrid = [] # Unused right now.
        self.terrainList = []

        self.thingList = []
        self.worldSpeed = worldSpeed # Milliseconds per frame.
        self.maxWorldAge = maxWorldAge
        self.worldAge = 0

        for aRow in range(self.maxY):
            row = []
            for aCol in range(self.maxX):
                row.append(None)
            self.grid.append(row)

        for aRow in range(self.maxY):
            row = []
            for aCol in range(self.maxX):
                row.append("L")
            self.terrainGrid.append(row)

        print("Size of grid:", len(self.grid))
        #print(self.terrainGrid)

    def start(self):
        # Starting message and the clock
        self.msg2statusbar.emit("Simulating.")
        self.timer.start(self.worldSpeed, self)

    def addThing(self, thing, x, y):
        if self.emptyLocation(x, y):
            thing.xPos = x
            thing.yPos = y
            thing.world = self
            thing.birthYear = self.worldAge
            self.grid[y][x] = thing
            self.thingList.append(thing)
            return thing
        else:
            print("Looks like there was something already there.")
    
    def delThing(self, thing):
        self.grid[thing.yPos][thing.xPos] = None
        self.thingList.remove(thing)

    def advanceTime(self):
        if self.worldAge > self.maxWorldAge:
            self.msg2statusbar.emit("Max world age reached.")
            print("Max world age reached.")
            self.timer.stop()
            self.update()
        elif self.thingList != []:
            random.shuffle(self.thingList)
            for thing in self.thingList:
                if thing.dead == True:
                    self.delThing(thing)
                else:
                    thing.liveALittle()
        else:
            self.msg2statusbar.emit("There is nothing left in the world...")
            print("There is nothing left in the world...")
            self.timer.stop()
            self.update()

    def drawThing(self, painter, thing):
        #image = QPixmap(thing.imagePath)
        #painter.drawPixmap(int(thing.xPos), int(thing.yPos), 15, 15, image)

        painter.setPen(QPen(thing.color, 5, Qt.SolidLine))
        painter.drawEllipse(int(thing.xPos), int(thing.yPos), 5, 5)

    def drawTerrain(self, painter, terrain):
        painter.setPen(QPen(QColor(0, 0, 255), 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.blue, Qt.DiagCrossPattern))
        painter.drawRect(terrain[0], terrain[1], terrain[0], terrain[1])

    # Draw everything for each frame.
    def paintEvent(self, event):
        painter = QPainter(self)
        for thing in self.thingList:
            self.drawThing(painter, thing)
        for terrain in self.terrainList:
            self.drawTerrain(painter, terrain)

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.advanceTime()
            self.update()
            self.worldAge += 1
            #print("World age:", self.worldAge)

    def emptyLocation(self, x, y):
        try:
            if self.grid[y][x] == None:
                return True
            else:
                return False
        except IndexError:
            #print("IndexError occured.")
            return False

    def checkLocation(self, x, y):
        try:
            if not self.emptyLocation(x, y):
                return self.grid[y][x]
            else:
                return None
        except IndexError:
            #print("IndexError occured.")
            return False