import time

from core.baseScreen import BaseScreen
from core.screenUtils import centerText, drawSmartText
from services.locationService import getLocation


class LocationAppScreen(BaseScreen):
    def __init__(self, appManager, hardware, parentScreen):
        super().__init__(appManager, hardware)
        self.parentScreen = parentScreen
        self.header = 'Geolocation'
        self.error = 'No Location WTF?'
        self.location = None
        self.cityScroll = 128
        self.regionScroll = 128
        self.countryScroll = 128

    def enter(self):
        self.location = getLocation()

    def update(self):
        self.input.update()

        if self.input.enterPressed() or self.input.backPressed():
            self.appManager.setScreen(self.parentScreen)
            return

        time.sleep(0.1)

    def draw(self):
        if self.location:
            city = self.location.get('city', 'Unknown')
            region = self.location.get('regionName', 'Unknown')
            country = self.location.get('country', 'Unknown')
            lat = round(self.location.get('lat', 0.0), 3)
            lon = round(self.location.get('lon', 0.0), 3)
            coordinates = f'{lat},{lon}'

            self.oled.fill(0)
            self.oled.text(self.header, centerText(self.header), 0)

            for lineX in range(128):
                self.oled.pixel(lineX, 10, 1)

            self.cityScroll = drawSmartText(self.oled, city, 18, self.cityScroll)
            self.regionScroll = drawSmartText(self.oled, region, 28, self.regionScroll)
            self.countryScroll = drawSmartText(self.oled, country, 38, self.countryScroll)
            self.oled.text(coordinates, centerText(coordinates), 52)
            self.oled.show()

        else:
            self.oled.fill(0)
            self.oled.text(self.error, 0, 28)
            self.oled.show()

    def exit(self):
        pass