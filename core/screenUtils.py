# core/screenUtils.py

def clearScreen(oled):
    oled.fill(0)


def showScreen(oled):
    oled.show()


def centerTextX(text, charWidth=8, screenWidth=128):
    textWidth = len(text) * charWidth
    return max(0, (screenWidth - textWidth) // 2)


def drawCenteredText(oled, text, y, charWidth=8):
    x = centerTextX(text, charWidth)
    oled.text(text, x, y)


def drawHeader(oled, title):
    oled.fill_rect(0, 0, 128, 10, 1)
    oled.text(title, 2, 1, 0)


def drawMenuCursor(oled, y):
    oled.text(">", 0, y)


def clamp(value, minValue, maxValue):
    return max(minValue, min(value, maxValue))


def centerText(text):
    textWidth = len(text) * 8
    return max(0, (128 - textWidth) // 2)


def getDateSuffix(day):
    if 11 <= day <= 13:
        return "th"

    lastDigit = day % 10

    if lastDigit == 1:
        return "st"
    elif lastDigit == 2:
        return "nd"
    elif lastDigit == 3:
        return "rd"
    else:
        return "th"


def closeResponse(response):
    try:
        if response:
            response.close()
    except:
        pass
    

def drawSmartText(oled, text, y, scrollX, screenWidth=128, charWidth=8):
    text = str(text)
    textWidth = len(text) * charWidth

    if textWidth <= screenWidth:
        x = max(0, (screenWidth - textWidth) // 2)
        oled.text(text, x, y)
        return scrollX

    oled.text(text, scrollX, y)
    scrollX -= 2

    if scrollX < -textWidth:
        scrollX = screenWidth

    return scrollX
