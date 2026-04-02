# App Development

This guide explains how to create and integrate new applications in **uPyPortal**.

---

## Overview

Apps in uPyPortal are modular, self-contained screens that:

- Render their own UI
- Handle their own input
- Update their own state

All apps live inside:

apps/

---

## Core Concept

Every app is a **screen**.

Apps inherit from:

core/baseScreen.py

This provides a consistent interface across the system.

---

## Required Methods

Every app must implement:

### update()

Handles logic updates.

Called every loop iteration.

### draw(display)

Handles rendering to the OLED.

display is the SSD1306 instance.

### handleInput(button)

Handles button input.

button is a string such as:

- "up"
- "down"
- "enter"
- "back"
- "shift"
- "special"

---

## Basic App Template

from core.baseScreen import BaseScreen

class MyApp(BaseScreen):
    def __init__(self):
        super().__init__()
        self.counter = 0

    def update(self):
        pass

    def draw(self, display):
        display.fill(0)
        display.text("My App", 0, 0)
        display.text(str(self.counter), 0, 10)

    def handleInput(self, button):
        if button == "up":
            self.counter += 1
        elif button == "down":
            self.counter -= 1

---

## Rendering Rules

- Always clear screen first:

display.fill(0)

- Keep text within 128x64 bounds
- Avoid excessive redraw complexity
- Keep UI simple and readable

---

## Input Handling

Buttons are abstracted via config.

Do NOT use GPIO directly.

Use button names:

if button == "enter":
    # Do something

This ensures cross-platform compatibility.

---

## Navigation

To exit an app:

Use the AppManager stack system.

Typically handled automatically when using "back".

Example:

if button == "back":
    return "BACK"

---

## State Management

Keep state inside the class:

self.value = 0

Avoid global variables.

---

## Using Services

Apps should NOT fetch external data directly.

Instead, use services from:

services/

Example:

- time service
- weather service
- network data

This keeps apps clean and modular.

---

## Menu Integration

To make your app accessible:

1. Import your app in a menu file (e.g. gamesMenu.py)
2. Add it to the menu list

Example:

("My App", MyApp)

---

## File Organization

Example:

apps/
└── games/
    ├── gamesMenu.py
    └── myApp.py

Group apps logically.

---

## Performance Tips

- Avoid blocking code
- Avoid long delays (sleep)
- Keep update() lightweight
- Minimize allocations inside loops

---

## Debugging

Use print statements via REPL:

print("Debug")

Or run:

mpremote connect /dev/ttyUSB0 repl

---

## Common Mistakes

### Screen Not Updating

- Forgot display.fill(0)
- draw() not implemented

### Input Not Working

- Wrong button name
- Not handled in handleInput()

### App Crashes

- Missing method
- Typo in class name
- Import error

---

## Design Guidelines

- Keep apps small and focused
- Reuse UI patterns
- Separate logic from rendering
- Use services for external data
- Avoid hardware coupling

---

## Example Ideas

- RF tranceiver interface
- WiFi scanner
- Stock ticker
- Games
- Sensor displays

---

## Next Steps

- Create your first custom app
- Integrate it into a menu
- Iterate and improve UI/UX
