import time

from core.baseScreen import BaseScreen
from core.screenUtils import clearScreen, showScreen, centerText, getDateSuffix
from services.timeService import syncTime, getTime


daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


class TimeAppScreen(BaseScreen):
    def __init__(self, appManager, hardware, parentScreen):
        super().__init__(appManager, hardware)
        self.parentScreen = parentScreen
        self.header = "Current Time"
        self.currentTime = None
        self.lastUpdate = 0

    def enter(self):
        syncTime()

    def update(self):
        self.input.update()

        if self.input.backPressed() or self.input.enterPressed():
            self.appManager.setScreen(self.parentScreen)
            return

        now = time.time()
        if now - self.lastUpdate >= 1:
            self.currentTime = getTime()
            self.lastUpdate = now

    def draw(self):
        self.oled.fill(0)
        self.oled.text(self.header, centerText(self.header), 0)

        for lineX in range(128):
            self.oled.pixel(lineX, 10, 1)

        if self.currentTime:
            day = daysOfWeek[self.currentTime[6]]
            dateDay = f"{self.currentTime[2]}{getDateSuffix(self.currentTime[2])}"
            date = f"{months[self.currentTime[1] - 1]} {dateDay}"
            year = f"{self.currentTime[0]}"
            currentClock = f"{self.currentTime[3]:02}:{self.currentTime[4]:02}:{self.currentTime[5]:02}"

            self.oled.text(day, centerText(day), 18)
            self.oled.text(date, centerText(date), 28)
            self.oled.text(year, centerText(year), 38)
            self.oled.text(currentClock, centerText(currentClock), 52)

        self.oled.show()

    def exit(self):
        pass