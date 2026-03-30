# core/menuScreen.py

from core.baseScreen import BaseScreen
from core.screenUtils import clearScreen, showScreen, drawHeader, drawMenuCursor


class MenuScreen(BaseScreen):
    def __init__(self, appManager, hardware, title, options, parentScreen=None):
        super().__init__(appManager, hardware)
        self.title = title
        self.options = options
        self.parentScreen = parentScreen
        self.selectedIndex = 0
        self.topIndex = 0
        self.visibleRows = 5

    def enter(self):
        pass

    def update(self):
        # Update Button States
        self.input.update()

        # Move Selection Up
        if self.input.upPressed():
            if self.selectedIndex > 0:
                self.selectedIndex -= 1
                if self.selectedIndex < self.topIndex:
                    self.topIndex = self.selectedIndex

        # Move Selection Down 
        elif self.input.downPressed():
            if self.selectedIndex < len(self.options) - 1:
                self.selectedIndex += 1
                if self.selectedIndex >= self.topIndex + self.visibleRows:
                    self.topIndex += 1

        # Open Selected Option
        elif self.input.enterPressed():
            if len(self.options) > 0:
                selectedOption = self.options[self.selectedIndex]
                selectedAction = selectedOption["action"]
                selectedAction()

        # Return To Parent Screen
        elif self.input.backPressed():
            if self.parentScreen is not None:
                self.appManager.setScreen(self.parentScreen)

    def draw(self):
        clearScreen(self.oled)
        drawHeader(self.oled, self.title)

        startY = 14
        rowHeight = 10

        for visibleIndex in range(self.visibleRows):
            optionIndex = self.topIndex + visibleIndex

            if optionIndex >= len(self.options):
                break

            option = self.options[optionIndex]
            y = startY + (visibleIndex * rowHeight)

            if optionIndex == self.selectedIndex:
                drawMenuCursor(self.oled, y)

            self.oled.text(option["label"], 10, y)

        showScreen(self.oled)

    def exit(self):
        pass
