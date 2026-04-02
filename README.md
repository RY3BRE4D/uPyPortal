# uPyPortal

### Modular MicroPython UI Framework for Embedded Devices

---

## Overview

**uPyPortal** is a modular UI framework for MicroPython devices like the ESP32 and Raspberry Pi Pico W.

It allows you to build interactive, menu-driven applications on embedded systems using an OLED display and physical buttons — without hardcoding WiFi credentials or writing everything from scratch.

Instead of one-off scripts, uPyPortal provides a structured system for building real embedded interfaces.

---

## Documentation

View full documentation here:

[Docs](docs/)

## Key Features

* **On-Device WiFi Setup**
  Scan, select, and connect to networks directly from the device — no hardcoding required

* **Modular Screen System**
  Build reusable screens, menus, and applications using a clean architecture

* **Button-Driven Input System**
  Supports tap, hold, and multi-button interactions

* **OLED UI Framework (SSD1306)**
  Includes rendering utilities for menus, headers, and scrolling text

* **Cross-Platform Support**
  Works with ESP32 and RP2040 (Pico W) using configurable pin layouts

* **Built-In Services**
  Location, time (NTP + timezone), and weather integration

---

## Architecture

uPyPortal is built around a simple but powerful concept:

```text
AppManager
   └── Screen (BaseScreen)
         ├── MenuScreen
         └── Custom Apps
```

Each screen:

* Handles its own input (`update()`)
* Handles its own rendering (`draw()`)
* Can transition to other screens via the AppManager

This keeps the system modular, scalable, and easy to extend.

---

## Project Structure

```text
apps/        # User-facing applications (info, games, stocks, etc.)
core/        # UI framework (screens, menus, app manager)
services/    # External data (weather, time, location)
config/      # Hardware configuration (pins, platform support)
lib/         # Drivers (e.g. SSD1306)
main.py      # Entry point
```

---

## Getting Started

### 1. Flash MicroPython

Install MicroPython on your ESP32 or Pico W.

---

### 2. Upload the Project

You have several options:

**Option A: Thonny (simple, manual)**
Upload files directly using the file browser.

**Option B: mpremote (recommended CLI method)**

```bash
mpremote connect /dev/ttyUSB0 cp -r ./uPyPortal/ :
```

**Option C: uPyDeploy (recommended for larger projects)**
Use the deployment script designed for multi-file MicroPython projects:
https://github.com/RY3BRE4D/uPyDeploy

---

### 3. Run

Ensure your entry file is:

```text
main.py
```

Then reboot the device.

---

### 4. First Boot Experience

* Device scans for WiFi networks
* You select a network using buttons
* Enter password via on-device UI
* System connects and launches the main menu

---

## Hardware Requirements

* ESP32 or Raspberry Pi Pico W
* SSD1306 OLED display (I2C, typically 128x64)
* 8+ buttons (configurable)

---

## Creating Your Own Apps

Create a new screen by extending `BaseScreen`:

```python
from core.baseScreen import BaseScreen

class MyApp(BaseScreen):
    def enter(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.oled.text("Hello World", 0, 0)
```

Then register it in a menu:

```python
{
    "label": "My App",
    "action": self.openMyApp
}
```

---

## Current Status

Core UI framework complete
Wi-Fi selection system working
OLED rendering system stable
Modular menu system implemented

In progress:

* Generic UI template for rapid app creation
* Expanded applications (stocks, tools, utilities, games)

---

## Roadmap

* Plugin-style app system
* Prebuilt UI templates
* API integrations (stocks, AI, etc.)
* Optional audio/voice support
* Additional hardware modules (RF, NFC, sensors)

---

## License

This project is licensed under the MIT License.

Includes third-party components such as the SSD1306 driver (MIT).

---

## Contributing

Contributions are welcome.
Feel free to:

* Add applications
* Improve UI components
* Optimize performance
* Expand hardware support

---

## Philosophy

Embedded devices can be more than just scripts. They can be sophisticated systems. 
Also, I grew tired of hardcoding my WiFi credentials. A solution for that grew into
a modular system that can serve as the basis for infinite device possibilties.

---

## Final Thoughts

uPyPortal is designed to be a foundation, not just a project.

Use it to build dashboards, handheld tools, network utilities, and custom embedded interfaces.

Build something useful.
