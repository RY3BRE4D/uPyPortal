# main.py

""" ___ Get Connected ___ """
import wifiSelect
""" Free Memory By Deleting The Module """
del wifiSelect
import gc                                        # Garbage Collection Module
gc.collect()                                     # Force Memory Cleanup
import time

"""___ Now Start The Main Program  ___"""
from buttons import buttons, led
from i2cOLED import oled

from core.appManager import AppManager
from core.inputHelper import InputHelper
from apps.mainMenu import MainMenuScreen

''' Initialize Shared Hardware '''
hardware = {
    "oled": oled,
    "buttons": buttons,
    "led": led,
    "input": InputHelper(buttons)
}

''' Create App Manager '''
appManager = AppManager(hardware)

''' Load Main Menu '''
appManager.setScreen(MainMenuScreen(appManager, hardware))

''' Main Loop '''
while True:
    appManager.update()
    appManager.draw()
    time.sleep_ms(50)
