# apps/stocks/stocksMenu.py

from core.menuScreen import MenuScreen


class StocksMenuScreen(MenuScreen):
    def __init__(self, appManager, hardware, parentScreen):
        options = [
            {
                "label": "Quote",
                "action": self.placeholderQuote
            },
            {
                "label": "Search",
                "action": self.placeholderSearch
            },
            {
                "label": "Watchlist",
                "action": self.placeholderWatchlist
            }
        ]

        super().__init__(appManager, hardware, "Stocks", options, parentScreen)

    def placeholderQuote(self):
        pass

    def placeholderSearch(self):
        pass

    def placeholderWatchlist(self):
        pass
