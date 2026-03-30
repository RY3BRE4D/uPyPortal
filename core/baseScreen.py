# core/baseScreen.py

class BaseScreen:
    def __init__(self, appManager, hardware):
        self.appManager = appManager
        self.hardware = hardware
        self.oled = hardware["oled"]
        self.buttons = hardware["buttons"]
        self.input = hardware["input"]

    def enter(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def exit(self):
        pass
