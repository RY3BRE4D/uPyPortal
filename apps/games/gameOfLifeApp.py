# apps/games/gameOfLifeApp.py

import time
import urandom

from core.baseScreen import BaseScreen


class GameOfLifeAppScreen(BaseScreen):
    def __init__(self, appManager, hardware, parentScreen, patternName="blinkingEyes", customGrid=None):
        super().__init__(appManager, hardware)
        self.parentScreen = parentScreen
        self.patternName = patternName
        self.customGrid = customGrid

        self.gridWidth = 20
        self.gridHeight = 10
        self.cellSpacing = 6
        self.cellSize = 4
        self.gridOffsetX = 4
        self.gridOffsetY = 2

        self.grid = []
        self.isPaused = False
        self.lastUpdateTime = 0
        self.updateIntervalMs = 100

    def enter(self):
        self.resetGrid()
        self.lastUpdateTime = time.ticks_ms()

    def createEmptyGrid(self):
        return [
            [0 for _ in range(self.gridWidth)]
            for _ in range(self.gridHeight)
        ]

    def copyGrid(self, sourceGrid):
        return [row[:] for row in sourceGrid]

    def resetGrid(self):
        self.grid = self.createEmptyGrid()

        if self.patternName == "custom":
            if self.customGrid is not None:
                self.grid = self.copyGrid(self.customGrid)
            return

        self.loadPattern(self.patternName)

    def loadPattern(self, patternName):
        if patternName == "blinkingEyes":
            self.loadBlinkingEyesPattern()

        elif patternName == "glider":
            self.loadGliderPattern()

        elif patternName == "exploder":
            self.loadExploderPattern()

        elif patternName == "random":
            self.loadRandomPattern()

    def setCell(self, x, y, value=1):
        if 0 <= x < self.gridWidth and 0 <= y < self.gridHeight:
            self.grid[y][x] = value

    def loadBlinkingEyesPattern(self):
        self.setCell(9, 5)
        self.setCell(10, 5)
        self.setCell(8, 6)
        self.setCell(9, 6)
        self.setCell(9, 7)
        self.setCell(8, 3)
        self.setCell(11, 8)

    def loadGliderPattern(self):
        startX = 8
        startY = 3

        self.setCell(startX + 1, startY + 0)
        self.setCell(startX + 2, startY + 1)
        self.setCell(startX + 0, startY + 2)
        self.setCell(startX + 1, startY + 2)
        self.setCell(startX + 2, startY + 2)

    def loadExploderPattern(self):
        startX = 7
        startY = 2

        self.setCell(startX + 0, startY + 0)
        self.setCell(startX + 2, startY + 0)
        self.setCell(startX + 4, startY + 0)

        self.setCell(startX + 0, startY + 1)
        self.setCell(startX + 4, startY + 1)

        self.setCell(startX + 0, startY + 2)
        self.setCell(startX + 4, startY + 2)

        self.setCell(startX + 0, startY + 3)
        self.setCell(startX + 4, startY + 3)

        self.setCell(startX + 0, startY + 4)
        self.setCell(startX + 2, startY + 4)
        self.setCell(startX + 4, startY + 4)

    def loadRandomPattern(self):
        for row in range(self.gridHeight):
            for col in range(self.gridWidth):
                self.grid[row][col] = urandom.getrandbits(1)

    def countNeighbors(self, x, y):
        neighborOffsets = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        neighborCount = 0

        for offsetX, offsetY in neighborOffsets:
            neighborX = x + offsetX
            neighborY = y + offsetY

            if 0 <= neighborX < self.gridWidth and 0 <= neighborY < self.gridHeight:
                neighborCount += self.grid[neighborY][neighborX]

        return neighborCount

    def updateGrid(self):
        newGrid = self.createEmptyGrid()

        for row in range(self.gridHeight):
            for col in range(self.gridWidth):
                liveNeighbors = self.countNeighbors(col, row)

                if self.grid[row][col] == 1:
                    if liveNeighbors == 2 or liveNeighbors == 3:
                        newGrid[row][col] = 1
                    else:
                        newGrid[row][col] = 0
                else:
                    if liveNeighbors == 3:
                        newGrid[row][col] = 1
                    else:
                        newGrid[row][col] = 0

        self.grid = newGrid

    def update(self):
        self.input.update()

        # Exit To Pattern Menu
        if self.input.backPressed():
            self.appManager.setScreen(self.parentScreen)
            return

        # Pause / Resume
        elif self.input.enterPressed():
            self.isPaused = not self.isPaused

        # Reset Current Pattern
        elif self.input.deletePressed():
            self.resetGrid()

        # Step Once Or Regenerate Random
        elif self.input.forwardPressed():
            if self.patternName == "random" and self.isPaused:
                self.resetGrid()
            elif self.isPaused:
                self.updateGrid()

        currentTime = time.ticks_ms()

        if not self.isPaused:
            if time.ticks_diff(currentTime, self.lastUpdateTime) >= self.updateIntervalMs:
                self.updateGrid()
                self.lastUpdateTime = currentTime

    def draw(self):
        self.oled.fill(0)

        for row in range(self.gridHeight):
            for col in range(self.gridWidth):
                if self.grid[row][col] == 1:
                    pixelX = self.gridOffsetX + (col * self.cellSpacing)
                    pixelY = self.gridOffsetY + (row * self.cellSpacing)
                    self.oled.fill_rect(pixelX, pixelY, self.cellSize, self.cellSize, 1)

        self.oled.show()

    def exit(self):
        pass
