import time

from core.baseScreen import BaseScreen
from core.screenUtils import centerText, drawSmartText
from services.locationService import getLocation
from services.weatherService import getWeather


class WeatherAppScreen(BaseScreen):
    def __init__(self, appManager, hardware, parentScreen):
        super().__init__(appManager, hardware)
        self.parentScreen = parentScreen
        self.location = None
        self.header = 'Weather'
        self.weatherTimerOld = 0
        self.condition = 'Checking...'
        self.temp = ''
        self.conditionScroll = 128

    def enter(self):
        self.location = getLocation()

    def update(self):
        self.input.update()

        if self.input.enterPressed() or self.input.backPressed():
            self.appManager.setScreen(self.parentScreen)
            return

        weatherTimerNew = time.time()

        if weatherTimerNew - self.weatherTimerOld >= 60:
            try:
                weather = getWeather(self.location)

                if weather:
                    self.condition = weather['condition']
                    self.temp = weather['temp']
                    self.temp = self.temp.replace('+', '').replace('°', '').strip()
                else:
                    self.condition = 'No Weather!'
                    self.temp = 'WTF?!'

                self.weatherTimerOld = weatherTimerNew

            except Exception as e:
                print(f"Error Getting Weather: {e}")
                self.condition = 'No Weather!'
                self.temp = 'WTF?!'

        time.sleep(0.1)

    def draw(self):
        self.oled.fill(0)
        self.oled.text(self.header, centerText(self.header), 0)

        for lineX in range(128):
            self.oled.pixel(lineX, 10, 1)

        self.conditionScroll = drawSmartText(self.oled, self.condition, 26, self.conditionScroll)
        self.oled.text(self.temp, centerText(self.temp), 40)
        self.oled.show()

    def exit(self):
        pass