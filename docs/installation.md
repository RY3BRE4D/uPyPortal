# Installation

This guide walks you through setting up your computer and tools to run **uPyPortal**.

---

## Overview

There are **three supported ways** to use uPyPortal:

### 1. Thonny (Simplest)
- GUI-based
- No command line required
- Best for beginners and quick testing

### 2. mpremote (Command Line)
- Direct CLI control of the device
- Good for copying files and scripting

### 3. uPyDeploy (Structured Deployment)
- Best for larger projects
- Automates wiping and redeploying full project folders

> You only need **one of these workflows** — choose what fits your setup.

---

## Install Based on Your Workflow

### Thonny Only (No CLI Required)

Download and install:

https://thonny.org

That’s it — no other tools required.

---

### mpremote Workflow

#### Install pipx (Recommended)

```bash
sudo apt update
sudo apt install pipx
pipx ensurepath
```

Restart your terminal after this.

#### Install mpremote

```bash
pipx install mpremote
```

If not found:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

---

### uPyDeploy Workflow

uPyDeploy depends on both **mpremote** and **rsync**.

#### Install pipx

```bash
sudo apt update
sudo apt install pipx
pipx ensurepath
```

Restart your terminal after this.

#### Install dependencies

```bash
pipx install mpremote
sudo apt install rsync
```

#### Get uPyDeploy

```bash
git clone https://github.com/RY3BRE4D/uPyDeploy.git
cd uPyDeploy
```

---

### ESP32 Only: Install esptool

If you are using an ESP32, install:

```bash
pipx install esptool
```

---

## Summary

| Workflow   | Required Tools            |
|-----------|--------------------------|
| Thonny    | Thonny only              |
| mpremote  | pipx, mpremote           |
| uPyDeploy | pipx, mpremote, rsync    |

---

## Flash MicroPython

### ESP32

Find port:

```bash
ls /dev/ttyUSB*
ls /dev/ttyACM*
```

Check device:

```bash
esptool --port /dev/ttyUSB0 chip_id
esptool --port /dev/ttyUSB0 read-mac
```

Erase:

```bash
esptool --chip esp32 --port /dev/ttyUSB0 erase_flash
```

Flash firmware:

```bash
esptool --chip esp32 --port /dev/ttyUSB0 --baud 460800 write-flash -z 0x1000 firmware.bin
```

---

### Raspberry Pi Pico W

1. Hold BOOTSEL
2. Plug into USB
3. Copy `.uf2` firmware file
4. Wait for reboot

---

## Deploy the Project

### Option 1: mpremote

From your project directory:

```bash
mpremote connect /dev/ttyUSB0 cp -r . :
mpremote connect /dev/ttyUSB0 run main.py
```

---

### Option 2: uPyDeploy

Clone:

```bash
git clone https://github.com/RY3BRE4D/uPyDeploy.git
cd uPyDeploy
```

Run:

```bash
./deploy.sh /path/to/yourProject
```

---

### Option 3: Thonny

- Connect to board
- Open files
- Save directly to device

---

## Linux Permissions Fix

```bash
sudo usermod -aG dialout $USER
```

Log out and back in.

---

## Common Issues

**mpremote not found**
```bash
export PATH="$HOME/.local/bin:$PATH"
```

**Port not detected**
- Replug device
- Check `/dev/ttyUSB*` again

**Board not responding**
- Try different cable
- Reflash firmware

---

## Next

After installation:

- Configure your hardware
- Deploy and run the system
