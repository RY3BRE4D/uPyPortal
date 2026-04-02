# Project Structure

This project is organized into modular components to support scalability, maintainability, and cross-platform compatibility.

---

## Root Directory

├── apps/  
├── config/  
├── core/  
├── lib/  
├── services/  
├── main.py  

---

## apps/

Contains all user-facing applications.

Examples:
- Info screens
- Games
- Stock tools
- Utilities

Each app typically:
- Inherits from BaseScreen
- Handles its own rendering
- Handles its own input logic

---

## core/

The heart of the UI system.

### Key Components

#### AppManager
- Controls app lifecycle
- Handles switching between screens
- Manages navigation stack

#### BaseScreen
- Base class for all apps
- Defines required methods:
  - update()
  - draw(display)
  - handleInput(button)

#### MenuScreen
- Provides menu navigation UI
- Used for app selection

---

## config/

Contains hardware and platform configuration.

### platformConfig.py

Defines:
- Pin mappings
- I2C configuration
- Platform profiles

This is the only place hardware should be defined.

---

## lib/

Drivers and low-level modules.

Examples:
- ssd1306.py (OLED driver)
- Hardware interfaces

These should remain reusable and platform-agnostic.

---

## services/

Background utilities and integrations.

Examples:
- Time service (NTP)
- Weather service
- Location service

Services typically:
- Fetch external data
- Provide structured data to apps

---

## main.py

Entry point of the system.

Responsibilities:
- Initialize hardware
- Load configuration
- Initialize AppManager
- Start main loop

---

## Application Flow 

1. Device boots  
2. `main.py` initializes hardware and configuration  
3. System checks WiFi connection  
4. If not connected → WiFi selection UI is launched  
5. User selects network and enters credentials  
6. WiFi connects and system continues startup  
7. AppManager starts  
8. Main menu is displayed  
9. User selects an app  
10. App runs and handles input/rendering  

---

## Design Philosophy

- Modular architecture
- Separation of concerns
- Hardware abstraction via config
- Reusable UI framework
- Easy app expansion

---

## Adding a New App

1. Create a new file in apps/  
2. Inherit from BaseScreen  
3. Implement required methods  
4. Register it in a menu  

---

## Example App Skeleton

from core.baseScreen import BaseScreen

class MyApp(BaseScreen):
    def __init__(self):
        super().__init__()

    def update(self):
        pass

    def draw(self, display):
        display.text("Hello", 0, 0)

    def handleInput(self, button):
        if button == "enter":
            print("Pressed")

---

## Notes

- Keep apps lightweight
- Avoid direct hardware access in apps
- Use services for external data
- Use config for all pin references
