# Getting Started

This guide helps you get **uPyPortal** running for the first time.

uPyPortal is a MicroPython portal-style system with a menu-driven UI, WiFi setup, apps, and services for devices such as the **ESP32** and **Raspberry Pi Pico W**.

---

## What Is uPyPortal?

uPyPortal is a modular MicroPython application that provides:

- A menu-driven UI on an OLED display
- WiFi setup and connectivity tools
- Multiple apps (games, info, utilities, etc.)
- A structured project layout for expansion

It is designed to behave like a small embedded “portal” system.

---

## How the System Works

At a high level:

1. The device boots and runs `main.py`
2. Hardware and configuration are initialized
3. WiFi is checked or configured
4. Core services start (AppManager, UI, etc.)
5. The main menu is displayed
6. You navigate and launch apps

---

## Project Structure (Simplified)

- `main.py` → Entry point
- `apps/` → Applications (games, tools, etc.)
- `core/` → Core UI and system logic
- `services/` → Background services (WiFi, time, etc.)
- `config/` → Hardware + platform configuration
- `lib/` → Drivers (OLED, etc.)

---

## Hardware Overview

Typical setup includes:

- ESP32 or Raspberry Pi Pico W
- SSD1306 I2C OLED display (usually 0x3C)
- Navigation buttons

---

## Configuration

Before running, review:

`config/platformConfig.py`

Make sure:

- SDA / SCL pins are correct
- I2C bus matches your board
- Button pins match your wiring
- Correct profile is selected (for RP2)

---

## First Boot Experience

On first boot:

- If WiFi is not configured → WiFi selection UI appears
- After connecting → system continues to main menu
- Apps become accessible through navigation buttons

---

## Navigation

Typical buttons:

- up / down → move through menu
- enter → select
- back → go back
- shift → change character set (in WiFi connection mode) / left (in some applications)
- special → right (in some applications)
- forward → re-scan for networks (in WiFi connection mode)
- delete → backspace (in WiFi connection mode)  
The buttons can be configured and used however fit

---

## Development Workflow (Recommended)

1. Flash MicroPython (see installation guide)
2. Verify board works (OLED, buttons)
3. Deploy project files
4. Iterate on apps and UI
5. Use tools like mpremote or Thonny for debugging

---

## Troubleshooting (Quick)

**OLED not working**
- Check wiring (SDA/SCL)
- Confirm address (usually 0x3C)
- Verify I2C pins in config

**Buttons not working**
- Check pin mapping
- Confirm common ground

**Nothing runs**
- Ensure `main.py` exists
- Check for runtime errors via REPL

---

## Next Steps

Continue with:

- `installation.md` → Set up your computer and tools
- `configuration.md` → Fine-tune hardware setup
- `project-structure.md` → Understand file layout
