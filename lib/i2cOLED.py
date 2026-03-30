from config.platformConfig import getPinConfig
from machine import I2C, Pin
from ssd1306 import SSD1306_I2C                  


pinConfig = getPinConfig()
i2c = I2C(pinConfig["i2cId"], sda=Pin(pinConfig["sda"]), scl=Pin(pinConfig["scl"]))

oled = SSD1306_I2C(128, 64, i2c)    
# Start With A Clear Screen
oled.fill(0)
oled.show() 

""" You Can Uncomment The Following Lines To Determine The I2C Adress Of The OLED Display """
#devices = i2c.scan()
#print("I2C devices:", devices)
""" If The OLED Isn't Automatically Detected, Specify The Correct Address As addr """
#oled = SSD1306_I2C(128, 64, i2c, addr=0x3D) 
# Common Addresses Are 0x3C And 0x3D