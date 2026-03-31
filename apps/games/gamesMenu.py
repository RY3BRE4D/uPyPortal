# apps/games/gamesMenu.py

from core.menuScreen import MenuScreen
from apps.games.pongApp import PongAppScreen
from apps.games.snakeApp import SnakeAppScreen
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
                "action": self.openSnake
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

    def openSnake(self):
        self.appManager.setScreen(
            SnakeAppScreen(self.appManager, self.hardware, self)
        )

    def openLifeMenu(self):
        self.appManager.setScreen(
            LifePatternMenuScreen(self.appManager, self.hardware, self)
        )
