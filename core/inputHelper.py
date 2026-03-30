# core/inputHelper.py

class InputHelper:
    def __init__(self, buttons):
        self.buttons = buttons

    def update(self):
        self.buttons.update()

    def upPressed(self):
        return self.buttons.pressed("up")

    def downPressed(self):
        return self.buttons.pressed("down")

    def enterPressed(self):
        return self.buttons.pressed("enter")

    def backPressed(self):
        return self.buttons.pressed("back")

    def forwardPressed(self):
        return self.buttons.pressed("forward")

    def deletePressed(self):
        return self.buttons.pressed("delete")

    def shiftPressed(self):
        return self.buttons.pressed("shift")

    def specialPressed(self):
        return self.buttons.pressed("special")
    
    def upDown(self):
        return self.buttons.state["up"] == 0

    def downDown(self):
        return self.buttons.state["down"] == 0
