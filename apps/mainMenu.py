# apps/mainMenu.py

from core.menuScreen import MenuScreen

from apps.info.infoMenu import InfoMenuScreen
from apps.games.gamesMenu import GamesMenuScreen
from apps.stocks.stocksMenu import StocksMenuScreen


class MainMenuScreen(MenuScreen):
    def __init__(self, appManager, hardware):
        self.appManagerRef = appManager
        self.hardwareRef = hardware

        options = [
            {
                "label": "Info",
                "action": self.openInfoMenu
            },
            {
                "label": "Games",
                "action": self.openGamesMenu
            },
            {
                "label": "Stocks",
                "action": self.openStocksMenu
            }
        ]

        super().__init__(appManager, hardware, "Main Menu", options)

    def openInfoMenu(self):
        self.appManager.setScreen(
            InfoMenuScreen(self.appManagerRef, self.hardwareRef, self)
        )

    def openGamesMenu(self):
        self.appManager.setScreen(
            GamesMenuScreen(self.appManagerRef, self.hardwareRef, self)
        )

    def openStocksMenu(self):
        self.appManager.setScreen(
            StocksMenuScreen(self.appManagerRef, self.hardwareRef, self)
        )
