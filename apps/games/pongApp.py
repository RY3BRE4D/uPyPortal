# apps/games/pongApp.py

import time
import random

from core.baseScreen import BaseScreen


class PongAppScreen(BaseScreen):
    def __init__(self, appManager, hardware, parentScreen):
        super().__init__(appManager, hardware)
        self.parentScreen = parentScreen

        # Display Constants
        self.screenWidth = 128
        self.screenHeight = 64

        # Ball Variables
        self.xInit = 64
        self.yInit = 32
        self.xNow = 64
        self.yNow = 32
        self.ballR = 3
        self.xSpeed = 1
        self.ySpeed = 1
        self.velocityX = 1
        self.velocityY = 1

        # Paddle Variables
        self.paddleWidth = 4
        self.lPadL = 20
        self.rPadL = 20

        self.lPadY = 0
        self.rPadY = 0
        self.lPadYOld = 0
        self.rPadYOld = 0

        self.lPadSpeed = 6
        self.rPadSpeed = 2

        # Game State
        self.lastFrameTime = 0
        self.frameIntervalMs = 15
        self.gameOver = False
        self.winnerText = ""

    def enter(self):
        self.resetGame()

    def resetGame(self):
        # Reset Ball
        self.xNow = self.xInit
        self.yNow = self.yInit

        self.xSpeed = random.choice([1, 2, 3])
        self.ySpeed = random.choice([1, 2, 3])

        self.velocityX = random.choice([-1, 1]) * self.xSpeed
        self.velocityY = random.choice([-1, 1]) * self.ySpeed

        # Reset Paddles
        self.lPadY = int((self.screenHeight - self.lPadL) / 2)
        self.rPadY = int((self.screenHeight - self.rPadL) / 2)

        self.lPadYOld = self.lPadY
        self.rPadYOld = self.rPadY

        self.gameOver = False
        self.winnerText = ""
        self.lastFrameTime = time.ticks_ms()

    def makeBall(self, x, y, r):
        for i in range(-r, r + 1):
            for j in range(-r, r + 1):
                if i * i + j * j <= r * r:
                    pixelX = x + i
                    pixelY = y + j

                    if 0 <= pixelX < self.screenWidth and 0 <= pixelY < self.screenHeight:
                        self.oled.pixel(pixelX, pixelY, 1)

    def makeLeftPaddle(self, y, length):
        for i in range(self.paddleWidth):
            for j in range(length):
                pixelX = i
                pixelY = y + j

                if 0 <= pixelY < self.screenHeight:
                    self.oled.pixel(pixelX, pixelY, 1)

    def makeRightPaddle(self, y, length):
        for i in range(self.screenWidth - self.paddleWidth, self.screenWidth):
            for j in range(length):
                pixelX = i
                pixelY = y + j

                if 0 <= pixelY < self.screenHeight:
                    self.oled.pixel(pixelX, pixelY, 1)

    def clampPaddles(self):
        if self.lPadY < 0:
            self.lPadY = 0
        elif self.lPadY > self.screenHeight - self.lPadL:
            self.lPadY = self.screenHeight - self.lPadL

        if self.rPadY < 0:
            self.rPadY = 0
        elif self.rPadY > self.screenHeight - self.rPadL:
            self.rPadY = self.screenHeight - self.rPadL

    def movePlayerPaddle(self):
        if self.input.upDown():
            self.lPadY -= self.lPadSpeed

        if self.input.downDown():
            self.lPadY += self.lPadSpeed

    def moveAiPaddle(self):
        aiCenter = self.rPadY + (self.rPadL // 2)
        deadZone = 7

        if self.yNow < aiCenter - deadZone:
            self.rPadY -= self.rPadSpeed

        elif self.yNow > aiCenter + deadZone:
            self.rPadY += self.rPadSpeed

    def handleCollisions(self):
        # Left Paddle Collision
        if (
            self.xNow <= self.ballR + self.paddleWidth and
            self.yNow >= self.lPadY + self.ballR and
            self.yNow <= self.lPadY + self.lPadL - self.ballR
        ):
            self.velocityX = abs(self.velocityX)
            self.xNow = self.ballR + self.paddleWidth + 1

            if self.lPadYOld < self.lPadY:
                self.velocityY = -abs(self.ySpeed)
            elif self.lPadYOld > self.lPadY:
                self.velocityY = abs(self.ySpeed)

        # Right Paddle Collision
        elif (
            self.xNow >= (self.screenWidth - 1) - self.ballR - self.paddleWidth and
            self.yNow >= self.rPadY + self.ballR and
            self.yNow <= self.rPadY + self.rPadL - self.ballR
        ):
            self.velocityX = -abs(self.velocityX)
            self.xNow = (self.screenWidth - 1) - self.ballR - self.paddleWidth - 1

            if self.rPadYOld < self.rPadY:
                self.velocityY = -abs(self.ySpeed)
            elif self.rPadYOld > self.rPadY:
                self.velocityY = abs(self.ySpeed)

        # Top / Bottom Wall Collision
        if self.yNow <= self.ballR:
            self.yNow = self.ballR + 1
            self.velocityY = abs(self.velocityY)

        elif self.yNow >= (self.screenHeight - 1) - self.ballR:
            self.yNow = (self.screenHeight - 1) - self.ballR - 1
            self.velocityY = -abs(self.velocityY)

        # Game Over
        if self.xNow < self.paddleWidth:
            self.gameOver = True
            self.winnerText = "Right Wins"

        elif self.xNow > self.screenWidth - self.paddleWidth:
            self.gameOver = True
            self.winnerText = "Left Wins"

    def updateGame(self):
        self.lPadYOld = self.lPadY
        self.rPadYOld = self.rPadY

        self.movePlayerPaddle()
        self.moveAiPaddle()
        self.clampPaddles()

        self.xNow += self.velocityX
        self.yNow += self.velocityY

        self.handleCollisions()

    def update(self):
        self.input.update()

        # Exit To Games Menu
        if self.input.backPressed():
            self.appManager.setScreen(self.parentScreen)
            return

        # Reset On Enter During Game Over
        if self.gameOver:
            if self.input.enterPressed():
                self.resetGame()
            return

        currentTime = time.ticks_ms()

        if time.ticks_diff(currentTime, self.lastFrameTime) >= self.frameIntervalMs:
            self.updateGame()
            self.lastFrameTime = currentTime

    def drawCenterText(self, text, y):
        x = int((self.screenWidth / 2) - ((len(text) * 8) / 2))
        if x < 0:
            x = 0
        self.oled.text(text, x, y)

    def draw(self):
        self.oled.fill(0)

        if self.gameOver:
            self.drawCenterText("Game Over", 16)
            self.drawCenterText(self.winnerText, 30)
            self.drawCenterText("Enter=Again", 44)
            self.oled.show()
            return

        self.makeBall(self.xNow, self.yNow, self.ballR)
        self.makeLeftPaddle(self.lPadY, self.lPadL)
        self.makeRightPaddle(self.rPadY, self.rPadL)

        self.oled.show()

    def exit(self):
        pass
