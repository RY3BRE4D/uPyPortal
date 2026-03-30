# core/appManager.py

class AppManager:
    def __init__(self, hardware):
        self.hardware = hardware
        self.currentScreen = None

    def setScreen(self, newScreen):
        if self.currentScreen is not None:
            self.currentScreen.exit()

        self.currentScreen = newScreen
        self.currentScreen.enter()

    def update(self):
        if self.currentScreen is not None:
            self.currentScreen.update()

    def draw(self):
        if self.currentScreen is not None:
            self.currentScreen.draw()

