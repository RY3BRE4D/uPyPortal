# Built-In Apps

This document provides an overview of the built-in applications included in **uPyPortal**.

---

## Overview

uPyPortal includes a collection of pre-built applications to demonstrate capabilities and provide useful functionality out of the box.

These apps serve two purposes:

- Provide immediate usability
- Act as reference implementations for development

---

## App Categories

Built-in apps are typically grouped into categories:

### Games
- Interactive apps designed for fun and input testing
- Examples:
  - Snake
  - Pong
  - Game of Life

### Info / System
- Display system or device information
- Examples:
  - Time and date
  - Network status
  - Device stats

### Stocks
- Data-driven apps related to market information
- Examples:
  - Stock price tools
  - Market data displays
  - Experimental finance-related apps

---

## Games

### Snake

A classic snake game adapted for button navigation.

Features:
- Grid-based movement
- Score tracking
- Simple collision detection

Purpose:
- Demonstrates continuous updates and input handling

---

### Pong

A paddle-and-ball game.

Features:
- Real-time movement
- Collision physics
- Player input control

Purpose:
- Demonstrates animation and timing

---

### Game of Life

A simulation of Conway’s Game of Life.

Features:
- Cellular automaton logic
- Pattern evolution
- Optional pattern editing

Purpose:
- Demonstrates grid rendering and algorithmic updates

---

## Info / System Apps

### System Info

Displays device-level information.

Examples:
- Uptime
- Memory usage
- Basic system stats

---

### Time / Clock

Displays current time and date.

Typically powered by:
- NTP service
- Local system clock fallback

---

### Network Info

Displays network-related data.

Examples:
- IP address
- SSID
- Signal strength

---

## Stocks

The **Stocks** section is currently under development, but is included as an early example of integrating external data into uPyPortal.

This category is intended to provide:

- Stock price lookups
- Basic market data
- Potential real-time or near real-time updates
- Future expansion into trading tools or analytics

---

### Current State

The Stocks apps are **under construction**, but partially implemented.

They are a good reference for:

- Rapid app prototyping
- Integrating external APIs
- Structuring data-driven apps

---

### Why It’s Included Now

Even in its current state, the Stocks section demonstrates how quickly you can:

- Create a new app file
- Register it in a menu
- Enable it in the system
- Start building functionality incrementally

This reflects the core philosophy of uPyPortal:

> Build fast → iterate → expand

---

### How to Enable

If the stock app exists in your project:

1. Ensure the app file is present (for example, `stocksApp.py`)
2. Add it to the appropriate menu
3. Deploy the project
4. Navigate to the app from the UI

Example menu entry:

`("Stocks", StocksApp),`

---

### Development Potential

The Stocks category is a strong foundation for more advanced features:

- API-driven data (Alpha Vantage, custom endpoints, etc.)
- Displaying price, volume, and trends
- Integrating with your existing stock tools
- Expanding into dashboards or alerts

---

### Notes

- Expect incomplete features
- APIs and structure may change
- Intended for experimentation and expansion

---

## WiFi Setup

Handles initial WiFi configuration.

Features:
- Scan available networks
- Navigate using buttons
- Enter credentials
- Save configuration

This app is typically triggered automatically on first boot.

---

## How Built-In Apps Are Organized

Apps are located in:

`apps/`

Subdirectories group related apps:

```text
apps/
├── games/
├── info/
├── stocks/
```

Each category usually contains:
- App files
- A corresponding menu file

---

## Menu Integration

Each category has a menu file.

Example:

`gamesMenu.py`

Menus define:

- App names
- App class references

Example:

`("Snake", SnakeApp),`  
`("Pong", PongApp),`

---

## Using Built-In Apps as Templates

You are encouraged to:

- Study existing apps
- Copy structure and patterns
- Modify behavior
- Extend functionality

This is the fastest way to learn the system.

---

## Design Patterns Used

Built-in apps demonstrate:

- BaseScreen inheritance
- Clean separation of logic and rendering
- Button-driven input handling
- Lightweight update loops

---

## Limitations

Keep in mind:

- OLED size is limited (128x64)
- Input is button-based (no touch)
- Performance is constrained on MicroPython

Apps are intentionally simple and efficient.

---

## Extending Built-In Apps

You can:

- Add features (scores, animations, menus)
- Improve UI layouts
- Add persistence (save data)
- Combine apps into larger systems

---

## Removing or Disabling Apps

If needed:

- Remove the app file
- Remove it from its menu

This keeps the system lightweight.

---

## Next Steps

- Explore `app-development.md` to build your own apps
- Modify existing apps to understand behavior
- Create new categories and expand the system
