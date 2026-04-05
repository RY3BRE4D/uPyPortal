# Deployment Guide

This guide explains how to deploy uPyPortal using uPyDeploy.

---

## Overview

uPyDeploy is a deployment tool designed for multi-file MicroPython projects.

It simplifies uploading full project directories while keeping your device clean and efficient.

---

## Why Use uPyDeploy

Compared to manual tools like mpremote or Thonny:

* Handles full project deployments
* Avoids leftover or unwanted files
* Provides a repeatable workflow
* Supports project-specific exclusions

---

## .uPyDeployignore

uPyDeploy supports a `.uPyDeployignore` file placed in the root of your project.

This file allows you to exclude files and directories from deployment.

---

### Example

```
docs/
README.md
.git/
.gitignore
__pycache__/
*.pyc
```

---

## What This Does

When deploying:

* Ignored files are skipped
* Only runtime-critical files are transferred
* Device storage stays clean and efficient

---

## Typical Use in uPyPortal

For uPyPortal, this ensures that:

* Only application code is deployed
* Documentation and development files stay on your computer
* The device runs a minimal, optimized file set

---

## Recommended Workflow

1. Create or update `.uPyDeployignore`
2. Run:

```bash
./deploy.sh /path/to/uPyPortal
```

3. Reboot device

---

## Summary

uPyDeploy + `.uPyDeployignore` provides a clean, scalable deployment workflow for MicroPython projects.

It is the recommended method for working with uPyPortal.
