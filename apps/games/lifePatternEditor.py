# apps/games/lifePatternEditor.py

import time

from core.baseScreen import BaseScreen
from apps.games.gameOfLifeApp import GameOfLifeAppScreen


class LifePatternEditorScreen(BaseScreen):
    def __init__(self, appManager, hardware, parentScreen):
        super().__init__(appManager, hardware)
        self.parentScreen = parentScreen

        self.gridWidth = 20
        self.gridHeight = 10
        self.cellSpacing = 6
        self.cellSize = 4
        self.gridOffsetX = 4
        self.gridOffsetY = 2

        self.cursorX = 0
        self.cursorY = 0
        self.grid = []

        self.lastBlinkTime = 0
        self.cursorVisible = True

    def enter(self):
        self.clearGrid()
        self.cursorX = 0
        self.cursorY = 0
        self.lastBlinkTime = time.ticks_ms()
        self.cursorVisible = True

    def clearGrid(self):
        self.grid = [
            [0 for _ in range(self.gridWidth)]
            for _ in range(self.gridHeight)
        ]

    def copyGrid(self):
        return [row[:] for row in self.grid]

    def toggleCurrentCell(self):
        if self.grid[self.cursorY][self.cursorX] == 1:
            self.grid[self.cursorY][self.cursorX] = 0
        else:
            self.grid[self.cursorY][self.cursorX] = 1

    def launchSimulation(self):
        self.appManager.setScreen(
            GameOfLifeAppScreen(
                self.appManager,
                self.hardware,
                self.parentScreen,
                patternName="custom",
                customGrid=self.copyGrid()
            )
        )

    def update(self):
        self.input.update()

        # Move Cursor Up
        if self.input.upPressed():
            if self.cursorY > 0:
                self.cursorY -= 1

        # Move Cursor Down
        elif self.input.downPressed():
            if self.cursorY < self.gridHeight - 1:
                self.cursorY += 1
                
        # Move Cursor Left
        elif self.input.shiftPressed():
            if self.cursorX > 0:
                self.cursorX -= 1
                
        # Move Cursor Right
        elif self.input.specialPressed():
            if self.cursorX < self.gridWidth - 1:
                self.cursorX += 1

        # Clear Grid
        elif self.input.deletePressed():
            self.clearGrid()

        # Start Simulation
        elif self.input.forwardPressed():
            self.launchSimulation()
            return

        # Toggle Cell
        elif self.input.enterPressed():
            self.toggleCurrentCell()

        # Cancel And Return
        elif self.input.backPressed():
            self.appManager.setScreen(self.parentScreen)
            return

        currentTime = time.ticks_ms()
        if time.ticks_diff(currentTime, self.lastBlinkTime) >= 250:
            self.cursorVisible = not self.cursorVisible
            self.lastBlinkTime = currentTime

    def drawCursor(self, pixelX, pixelY):
        # Draw Cursor Border
        self.oled.fill_rect(pixelX - 1, pixelY - 1, self.cellSize + 2, 1, 1)
        self.oled.fill_rect(pixelX - 1, pixelY + self.cellSize, self.cellSize + 2, 1, 1)
        self.oled.fill_rect(pixelX - 1, pixelY - 1, 1, self.cellSize + 2, 1)
        self.oled.fill_rect(pixelX + self.cellSize, pixelY - 1, 1, self.cellSize + 2, 1)

    def draw(self):
        self.oled.fill(0)

        # Draw Pattern Grid
        for row in range(self.gridHeight):
            for col in range(self.gridWidth):
                pixelX = self.gridOffsetX + (col * self.cellSpacing)
                pixelY = self.gridOffsetY + (row * self.cellSpacing)

                if self.grid[row][col] == 1:
                    self.oled.fill_rect(pixelX, pixelY, self.cellSize, self.cellSize, 1)

        # Draw Cursor
        if self.cursorVisible:
            cursorPixelX = self.gridOffsetX + (self.cursorX * self.cellSpacing)
            cursorPixelY = self.gridOffsetY + (self.cursorY * self.cellSpacing)
            self.drawCursor(cursorPixelX, cursorPixelY)

        self.oled.show()

    def exit(self):
        pass
