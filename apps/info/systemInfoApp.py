import time

from core.baseScreen import BaseScreen
from core.screenUtils import centerText, drawSmartText
from services.locationService import getLocation


class SystemInfoAppScreen(BaseScreen):
    def __init__(self, appManager, hardware, parentScreen):
        super().__init__(appManager, hardware)
        self.parentScreen = parentScreen
        self.header = 'System Info'
        self.error = 'No System Info!'
        self.location = None
        self.ipScroll = 128
        self.ispScroll = 128
        self.tzScroll = 128

    def enter(self):
        self.location = getLocation()

    def update(self):
        self.input.update()

        if self.input.enterPressed() or self.input.backPressed():
            self.appManager.setScreen(self.parentScreen)
            return

        time.sleep(0.1)

    def draw(self):
        self.oled.fill(0)
        self.oled.text(self.header, centerText(self.header), 0)

        for lineX in range(128):
            self.oled.pixel(lineX, 10, 1)

        if self.location and self.location.get('status') == 'success':
            ip = str(self.location.get('query', 'No IP'))
            isp = str(self.location.get('isp', 'No ISP'))
            timezone = str(self.location.get('timezone', 'No TZ'))

            self.ipScroll = drawSmartText(self.oled, ip, 18, self.ipScroll)
            self.ispScroll = drawSmartText(self.oled, isp, 28, self.ispScroll)
            self.tzScroll = drawSmartText(self.oled, timezone, 38, self.tzScroll)

        else:
            self.oled.text(self.error, 0, 28)

        self.oled.show()

    def exit(self):
        pass