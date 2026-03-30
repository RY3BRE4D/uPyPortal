# apps/games/gamesMenu.py

from core.menuScreen import MenuScreen
from apps.games.pongApp import PongAppScreen
from apps.games.lifePatternMenu import LifePatternMenuScreen


class GamesMenuScreen(MenuScreen):
    def __init__(self, appManager, hardware, parentScreen):
        options = [
            {
                "label": "Pong",
                "action": self.openPong
            },
            {
                "label": "Snake",
                "action": self.placeholderSnake
            },
            {
                "label": "Life",
                "action": self.openLifeMenu
            }
        ]

        super().__init__(appManager, hardware, "Games", options, parentScreen)

    def openPong(self):
        self.appManager.setScreen(
            PongAppScreen(self.appManager, self.hardware, self)
        )

    def placeholderSnake(self):
        pass

    def openLifeMenu(self):
        self.appManager.setScreen(
            LifePatternMenuScreen(self.appManager, self.hardware, self)
        )
