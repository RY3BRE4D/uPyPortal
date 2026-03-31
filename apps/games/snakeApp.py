# apps/games/snakeApp.py
import time
import urandom
from core.baseScreen import BaseScreen


class SnakeAppScreen(BaseScreen):
    def __init__(self, appManager, hardware, parentScreen):
        super().__init__(appManager, hardware)
        self.parentScreen = parentScreen

        # Screen / Grid Settings
        self.screenWidth = 128
        self.screenHeight = 64
        self.cellSize = 4

        self.gridWidth = self.screenWidth // self.cellSize
        self.gridHeight = self.screenHeight // self.cellSize

        # Timing
        self.lastMoveTime = 0
        self.moveIntervalMs = 140

        # Game State
        self.snake = []
        self.direction = (1, 0)
        self.nextDirection = (1, 0)
        self.food = (0, 0)
        self.score = 0
        self.gameOver = False

    def enter(self):
        self.resetGame()

    def resetGame(self):
        centerX = self.gridWidth // 2
        centerY = self.gridHeight // 2

        self.snake = [
            (centerX, centerY),
            (centerX - 1, centerY),
            (centerX - 2, centerY),
        ]

        self.direction = (1, 0)
        self.nextDirection = (1, 0)
        self.score = 0
        self.gameOver = False
        self.spawnFood()
        self.lastMoveTime = time.ticks_ms()

    def spawnFood(self):
        while True:
            foodX = urandom.getrandbits(8) % self.gridWidth
            foodY = urandom.getrandbits(8) % self.gridHeight
            if (foodX, foodY) not in self.snake:
                self.food = (foodX, foodY)
                return

    def setDirection(self, newDirection):
        currentX, currentY = self.direction
        newX, newY = newDirection

        # Prevent instant reverse into self
        if (newX == -currentX) and (newY == -currentY):
            return

        self.nextDirection = newDirection

    def moveSnake(self):
        self.direction = self.nextDirection

        headX, headY = self.snake[0]
        dirX, dirY = self.direction
        newHead = (headX + dirX, headY + dirY)

        # Wall Collision
        if (
            newHead[0] < 0
            or newHead[0] >= self.gridWidth
            or newHead[1] < 0
            or newHead[1] >= self.gridHeight
        ):
            self.gameOver = True
            return

        # Self Collision
        if newHead in self.snake:
            self.gameOver = True
            return

        self.snake.insert(0, newHead)

        # Food Collision
        if newHead == self.food:
            self.score += 1
            self.spawnFood()
        else:
            self.snake.pop()

    def update(self):
        self.input.update()

        # Exit To Games Menu
        if self.input.backPressed():
            self.appManager.setScreen(self.parentScreen)
            return

        # Restart After Game Over
        if self.gameOver:
            if self.input.enterPressed():
                self.resetGame()
            return

        # Controls
        if self.input.upPressed():
            self.setDirection((0, -1))
        elif self.input.downPressed():
            self.setDirection((0, 1))
        elif self.input.specialPressed():
            self.setDirection((1, 0))
        elif self.input.shiftPressed():
            self.setDirection((-1, 0))

        currentTime = time.ticks_ms()
        if time.ticks_diff(currentTime, self.lastMoveTime) >= self.moveIntervalMs:
            self.moveSnake()
            self.lastMoveTime = currentTime

    def drawCell(self, gridX, gridY, fillValue=1):
        pixelX = gridX * self.cellSize
        pixelY = gridY * self.cellSize
        self.oled.fill_rect(pixelX, pixelY, self.cellSize, self.cellSize, fillValue)

    def drawCenterText(self, text, y):
        x = int((self.screenWidth - (len(text) * 8)) / 2)
        if x < 0:
            x = 0
        self.oled.text(text, x, y)

    def draw(self):
        self.oled.fill(0)

        if self.gameOver:
            self.drawCenterText("Game Over", 12)
            self.drawCenterText("Score: " + str(self.score), 26)
            self.drawCenterText("Enter=Again", 40)
            self.oled.show()
            return

        # Draw Food
        self.drawCell(self.food[0], self.food[1], 1)

        # Draw Snake
        for segmentX, segmentY in self.snake:
            self.drawCell(segmentX, segmentY, 1)

        self.oled.show()

    def exit(self):
        pass
