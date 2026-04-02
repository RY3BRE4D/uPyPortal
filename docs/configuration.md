# Configuration Guide

This project is designed to run on multiple MicroPython platforms (ESP32, Raspberry Pi Pico W, etc.) using a flexible configuration system.

All hardware-specific configuration is handled in:

config/platformConfig.py

---

## Overview

The configuration system defines:

- I2C bus and pins
- OLED display connection
- LED pin
- Button mappings
- Platform-specific profiles

This allows the same codebase to run on different hardware setups with minimal changes.

---

## Selecting a Platform

The platform is automatically detected using:

from sys import platform

Supported platforms include:

- "esp32"
- "rp2" (Raspberry Pi Pico / Pico W)

---

## RP2 (Pico / Pico W) Profiles

RP2 supports multiple configurations using profiles.

Set the active profile at the top of platformConfig.py:

rp2Config = "default"   # or "alt", "full", etc.

Use "full" for the 8 button version on the Pico W.

Each profile defines its own pin layout.

You can define your own profiles, or use mine.

---

## Example Configuration

### ESP32

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
}

---

### RP2 (Pico W)

"rp2": {
    "profiles": {
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
        }
    }
}

---

## I2C Configuration

The OLED display uses I2C.

Key fields:
- i2cId → I2C bus number
- sda → SDA pin
- scl → SCL pin

### Common OLED Address

Most SSD1306 displays use:

0x3C

Or 0x3D, although I have never seen that.

---

## Button Mapping

Buttons are mapped by name:

"buttons": {
    "up": 26,
    "down": 27,
    "enter": 4,
}

These names are used throughout the UI system.

### Standard Button Names

- up
- down
- enter
- back
- forward
- delete
- shift
- special (optional)

---

## LED Configuration

The LED field defines a status LED:

"led": 2        # ESP32 GPIO + onboard LED  
"led": "LED"    # Pico onboard LED  

---

## Common Issues

### OLED Not Detected

- Check wiring (are SDA/SCL swapped?)
- Verify address with:

i2cdetect -y 1

- Ensure correct i2cId

---

### Buttons Not Working

- Verify pin numbers match your wiring
- Ensure buttons share common ground

---

### Wrong Platform Detected

- Print platform:

import sys  
print(sys.platform)

- If not "esp32" or "rp2", a new platform configuration must be added for your board

---
