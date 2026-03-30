# platformConfig.py
from sys import platform

# 🔧 Change Between COnfigurations. (Right Now, We Have 2 Options For rp2)
rp2Config = "full"   # Change To "alt" Or Whatever You Add ("full" For New 8 Button On Certain Platforms) 


platformConfig = {
    "esp32": {
        "i2cId": 0,
        "sda": 21,
        "scl": 22,
        "led": 2,
        "buttons": {
            "up": 26,
            "down": 27,
            "enter": 4,
            "back": 33,
            "forward": 14,
            "delete": 25,
            "shift": 32,
            "special": 13,
        },
    },

    "rp2": {
        "profiles": {
            "default": {
                "i2cId": 0,
                "sda": 0,
                "scl": 1,
                "led": "LED",
                "buttons": {
                    "up": 15,
                    "down": 16,
                    "enter": 13,
                    "back": 14,
                    "forward": 18,
                    "delete": 17,
                    "shift": 19,
                },
            },
            
            "full": {
                "i2cId": 0,
                "sda": 0,
                "scl": 1,
                "led": "LED",
                "buttons": {
                    "up": 15,
                    "down": 16,
                    "enter": 13,
                    "back": 14,
                    "forward": 18,
                    "delete": 17,
                    "shift": 19,
                    "special": 21,
                },
            },

            "alt": {
                "i2cId": 0,
                "sda": 0,
                "scl": 1,
                "led": "LED",
                "buttons": {
                    "up": 12,
                    "down": 13,
                    "enter": 10,
                    "back": 15,
                    "forward": 11,
                    "delete": 14,
                    "shift": 9,
                },
            },
        }
    },
}


def getPinConfig():
    if platform not in platformConfig:
        raise RuntimeError("Unsupported platform: " + platform)

    if platform == "rp2":
        return platformConfig["rp2"]["profiles"][rp2Config]

    return platformConfig[platform]