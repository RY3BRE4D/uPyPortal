# apps/info/infoMenu.py

from core.menuScreen import MenuScreen
from apps.info.timeApp import TimeAppScreen
from apps.info.locationApp import LocationAppScreen
from apps.info.weatherApp import WeatherAppScreen
from apps.info.systemInfoApp import SystemInfoAppScreen


class InfoMenuScreen(MenuScreen):
    def __init__(self, appManager, hardware, parentScreen):
        self.appManagerRef = appManager
        self.hardwareRef = hardware

        options = [
            {"label": "Time", "action": self.openTimeApp},
            {"label": "Location", "action": self.openLocationApp},
            {"label": "Weather", "action": self.openWeatherApp},
            {"label": "System Info", "action": self.openSystemInfoApp}
        ]

        super().__init__(appManager, hardware, "Info", options, parentScreen)

    def openTimeApp(self):
        self.appManager.setScreen(TimeAppScreen(self.appManagerRef, self.hardwareRef, self))

    def openLocationApp(self):
        self.appManager.setScreen(LocationAppScreen(self.appManagerRef, self.hardwareRef, self))

    def openWeatherApp(self):
        self.appManager.setScreen(WeatherAppScreen(self.appManagerRef, self.hardwareRef, self))

    def openSystemInfoApp(self):
        self.appManager.setScreen(SystemInfoAppScreen(self.appManagerRef, self.hardwareRef, self))

