# buttons.py
from config.platformConfig import getPinConfig
from machine import Pin
import time

pinConfig = getPinConfig()

class Buttons:
    def __init__(self, buttonPinMap):
        # buttonPinMap: {"up": 15, "down": 16, ...}
        self.buttonNames = list(buttonPinMap.keys())
        self.buttons = {name: Pin(pin, Pin.IN, Pin.PULL_UP) for name, pin in buttonPinMap.items()}

        # Store Current + Previous States (1 = Not Pressed, 0 = Pressed). Initial States Are Used At Boot
        initial = {name: self.buttons[name].value() for name in self.buttonNames}
        self.state = dict(initial)
        self.stateOld = dict(initial)

         # Hold tracking
        self.pressStartMs = {name: None for name in self.buttonNames}
        self.holdFired = {name: False for name in self.buttonNames} 
        self.lastPressDurationMs = {name: 0 for name in self.buttonNames}    

    def update(self):
        now = time.ticks_ms()

        for name in self.buttonNames:
            self.stateOld[name] = self.state[name]
            self.state[name] = self.buttons[name].value()

            # Button Just Pressed
            if self.state[name] == 0 and self.stateOld[name] == 1:
                self.pressStartMs[name] = now
                self.holdFired[name] = False

            # Button Just Released
            if self.state[name] == 1 and self.stateOld[name] == 0:
                if self.pressStartMs[name] is not None:
                    self.lastPressDurationMs[name] = time.ticks_diff(now, self.pressStartMs[name])
                self.pressStartMs[name] = None
                self.holdFired[name] = False

    def tap(self, name, holdMs):
        # Tap = Released And Duration Shorter than Hold Threshold And No Hold Fired
        return self.released(name) and (self.lastPressDurationMs[name] < holdMs) and (not self.holdFired[name])

    def pressed(self, name):
        return self.state[name] == 0 and self.stateOld[name] == 1

    def released(self, name):
        return self.state[name] == 1 and self.stateOld[name] == 0
    
    def held(self, name, holdMs):
        if self.state[name] == 0:
            start = self.pressStartMs[name]

            if start is not None and not self.holdFired[name]:
                if time.ticks_diff(time.ticks_ms(), start) >= holdMs:
                    self.holdFired[name] = True
                    return True

        return False

    def getEvents(self):
        pressed = []
        released = []

        for name in self.buttonNames:
            if self.pressed(name):
                pressed.append(name)
            if self.released(name):
                released.append(name)

        return pressed, released

# Builtin LED IF Needed
led = Pin(pinConfig["led"], Pin.OUT)
led.value(0)  # Turn Off LED Initially

buttons = Buttons(pinConfig["buttons"])


