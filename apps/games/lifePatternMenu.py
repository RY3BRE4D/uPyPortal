# apps/games/lifePatternMenu.py

from core.menuScreen import MenuScreen
from apps.games.gameOfLifeApp import GameOfLifeAppScreen
from apps.games.lifePatternEditor import LifePatternEditorScreen


class LifePatternMenuScreen(MenuScreen):
    def __init__(self, appManager, hardware, parentScreen):
        self.appManagerRef = appManager
        self.hardwareRef = hardware

        options = [
            {
                "label": "Blinking Eyes",
                "action": self.openBlinkingEyes
            },
            {
                "label": "Glider",
                "action": self.openGlider
            },
            {
                "label": "Exploder",
                "action": self.openExploder
            },
            {
                "label": "Random",
                "action": self.openRandom
            },
            {
                "label": "Custom",
                "action": self.openCustom
            }
        ]

        super().__init__(appManager, hardware, "Life Patterns", options, parentScreen)

    def openBlinkingEyes(self):
        self.appManager.setScreen(
            GameOfLifeAppScreen(
                self.appManagerRef,
                self.hardwareRef,
                self,
                patternName="blinkingEyes"
            )
        )

    def openGlider(self):
        self.appManager.setScreen(
            GameOfLifeAppScreen(
                self.appManagerRef,
                self.hardwareRef,
                self,
                patternName="glider"
            )
        )

    def openExploder(self):
        self.appManager.setScreen(
            GameOfLifeAppScreen(
                self.appManagerRef,
                self.hardwareRef,
                self,
                patternName="exploder"
            )
        )

    def openRandom(self):
        self.appManager.setScreen(
            GameOfLifeAppScreen(
                self.appManagerRef,
                self.hardwareRef,
                self,
                patternName="random"
            )
        )

    def openCustom(self):
        self.appManager.setScreen(
            LifePatternEditorScreen(
                self.appManagerRef,
                self.hardwareRef,
                self
            )
        )
