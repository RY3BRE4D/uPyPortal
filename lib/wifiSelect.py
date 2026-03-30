from buttons import buttons, led
from i2cOLED import oled
import network
import time
import usocket as socket


"""___ Initializing Wi-Fi ___"""
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
selectedWiFi = None

if wifi.isconnected():
    selectedWiFi = wifi.config('essid')               #This Variable Will Store The SSID Of The Selected Wi-Fi Network. If WiFi Connection Is Already Established, It Will Store The SSID Of The Connected Network
    print(f'Already Connected To: {selectedWiFi}')
    
"""___ Defining The Characters That Can Be Entered ___"""
asciiLowercase = 'abcdefghijklmnopqrstuvwxyz'
asciiUppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
asciiDigits = '0123456789'
asciiPunctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

""" Generate Seperate Lists For The Characters That Can Be Entered """
charLists = [list(' ' + asciiLowercase), list(' ' + asciiUppercase), list(' ' + asciiDigits), list(' ' + asciiPunctuation)]
charListsIndex = 0
charState = charLists[charListsIndex]   # The Current Character List
showPassword = False                     # Toggle To Show / Hide Password Characters
holdThreshold = 1000                 # Hold Threshold In Milliseconds
        

"""___ This Function Is For Quickly, And Safely, Clearing The Display (Mainly For Upon Exit) ___"""
def blankOLED():
    try:
        oled.fill(0)
        oled.show()
    except:
        pass  # If I2C/OLED Is Already Gone, Don't Crash Here
    
    
"""___ This Function Maps Signal Strength With A 4 Bar Meter (Just For Fun And Awesome Debugging) ___"""
def rssiToBars(rssi):
    if rssi >= -40:
        return "|█████|" 
    elif rssi >= -50:
        return "|████ |"
    elif rssi >= -60:
        return "|███  |"
    elif rssi >= -70:
        return "|██   |"
    elif rssi >= -80:
        return "|█    |"
    else:
        return "|     |"


"""___ This Function Prints A Nice Table With The Bar Style Signal Indicators (Just For Fun And Awesome Debugging) ___"""
def printWiFiBars(wifiNetworks):
    print("\n{:<25} RSSI   Signal".format("SSID"))
    print("-" * 45)

    for ssid in sorted(wifiNetworks, key=lambda s: wifiNetworks[s], reverse=True):
        rssi = wifiNetworks[ssid]
        bars = rssiToBars(rssi)
        print(f"{ssid:<25} {rssi:>4}  {bars}")
        

"""___ This Function Generates The Dictionary Of All The Wi-Fi Networks That Are Available With Signal Strength ___"""
wifiNetworks = {}   # SSID -> signalStrength
def scanForWiFi():
    for networkInfo in wifi.scan():
        ssid = networkInfo[0].decode('utf-8')
        signalStrength = networkInfo[3]

        if not ssid:
            continue
        
        if ssid not in wifiNetworks or signalStrength != wifiNetworks[ssid]:
            wifiNetworks[ssid] = signalStrength

    printWiFiBars(wifiNetworks)
    return wifiNetworks


try:
    """___ This Loop Will Run Until A WiFi Connection Is Established ___"""
    wifiIndex = 0
    selectedState = 0
    if not selectedWiFi:
        wifiNetworks = scanForWiFi()
    else:
        pass
    while not wifi.isconnected():
        cIndex = 1
        cNum = 0
        c = [charState[cIndex]]
        cursorX = 0

        """___ Display The Available Networks On The OLED Display ___"""
        oled.fill(0)
        oled.text('Select Newtork',7,0)
        for lineX in range(128):
            oled.pixel(lineX,10,1)
        if wifiNetworks:
            ssidList = sorted(
                wifiNetworks,
                key=lambda ssid: wifiNetworks[ssid],
                reverse=True
            )

            ssid = ssidList[wifiIndex]
            rssi = wifiNetworks[ssid]

            oled.text(ssid, 0, 27)
            oled.text(str(rssi), 0, 37)
        else:
            oled.text('No Networks',20,27)
        oled.show()

        """___ Check For Button Presses To Navigate The WiFi Networks ___"""
        buttons.update()

        if buttons.pressed("up"):
            wifiIndex = (wifiIndex - 1) % len(wifiNetworks)
        if buttons.pressed("down"):
            wifiIndex = (wifiIndex + 1) % len(wifiNetworks) 
        if buttons.pressed("forward"):
            wifiNetworks = scanForWiFi()
        if buttons.pressed("enter"):
            ssidList = sorted(
                wifiNetworks,
                key=lambda s: wifiNetworks[s],
                reverse=True
            )
            selectedWiFi = ssidList[wifiIndex]
            print(f"\nNetwork Selected: {selectedWiFi}\n")
            selectedState = 1
        
        time.sleep(0.1)

        """___ This Loop Will Run Until The Password Is Entered ___"""
        while selectedState == 1:
            """ Printing The Current Password Entry Information To The OLED """
            oled.fill(0)
            oled.text('Enter Password:',0,0)       # Prompt To Enter Password

            """ If Password Length Exceeds Display Width, Shift The View """
            maxChars = 128 // 8  # Number Of Characters That Fit On Screen (16 For 128px Width)
            startIndex = max(0, len(c) - maxChars)  # Start Showing From The Last Visible Part

            """ Draw The Password From StartIndex Onward """
            cXVal = 0
            
            if showPassword:
                for i in range(startIndex, len(c)):
                    oled.text(c[i], cXVal, 18)
                    cXVal += 8
            else:
                """ All Characters Will Be *s Except The Current Entry Character """
                for i in range(startIndex, len(c) - 1):
                    oled.text('*', cXVal, 18)
                    cXVal += 8

                oled.text(c[-1], cXVal, 18)      

            """ Draw Cursor """
            cursorX = min(cNum * 8, 128 - 8)  # Keep Cursor Within Screen Bounds
            for cx in range(cursorX, cursorX + 8):
                oled.pixel(cx, 27, 1)
            oled.show()      

            """___ Checking For Button Presses To Enter The Password ___"""
            buttons.update()

            if buttons.pressed("up"):
                cIndex = (cIndex + 1) % len(charState)
                c[cNum] = charState[cIndex]

            if buttons.pressed("down"):
                cIndex = (cIndex - 1) % len(charState)
                c[cNum] = charState[cIndex]

            # HOLD → Toggle Show / Hide
            if buttons.held("forward", holdThreshold):
                showPassword = not showPassword           
            # QUICK PRESS → Normal Forward Behavior
            if buttons.tap("forward", holdThreshold):
                cursorX += 8
                c.append('')
                cIndex = 0
                cNum += 1

            if buttons.pressed("delete"):
                if len(c) > 1:
                    cursorX -= 8
                    c.pop()
                    cNum -= 1

            if buttons.pressed("back"):
                selectedState = 0

            if buttons.pressed("shift"):
                charListsIndex = (charListsIndex + 1) % len(charLists)
                charState = charLists[charListsIndex]
                cIndex = 0

            if buttons.pressed("enter"):
                password = ''.join(c).strip()
                """ Uncomment The Following Line To Print The Entered Password """
                #print(password)
                if password:
                    wifi.connect(selectedWiFi, password)
                else:
                    wifi.connect(selectedWiFi)
                timeoutCounter = 0
                while not wifi.isconnected():
                    oled.fill(0)
                    oled.text('Connecting...', 0, 0)
                    oled.show()
                    time.sleep(1)
                    timeoutCounter += 1
                    if timeoutCounter > 15:
                        oled.fill(0)
                        oled.text('Connect Failed', 0, 18)
                        oled.show()
                        time.sleep(2)
                        c = ['']
                        break
                selectedState = 0

            time.sleep(0.1)

    """___ Turn On Builtin LED To Indicate A Connection ___"""
    led.value(1)

    """___ Show The SSID And IP Address Until The Enter Button Is Pressed ___"""
    ipAddr = wifi.ifconfig()[0]       # Get The IP Address
    displayState = 1
    scrollOffset = 0
    maxScroll = len(selectedWiFi) * 8 - 128  # Amount Of Pixels To Scroll

    while displayState == 1:
        oled.fill(0)
        oled.text("Success!", 0, 0)
        oled.text("Connected To:", 0, 18)

        if len(selectedWiFi) * 8 > 128:
            oled.text(selectedWiFi, -scrollOffset, 27)
            scrollOffset = (scrollOffset + 2) % maxScroll
        else:
            oled.text(selectedWiFi, int((128 / 2) - ((len(selectedWiFi) * 8) / 2)), 27)

        oled.text("IP:", 0, 45)
        oled.text(ipAddr, (int((128/2)-((len(ipAddr)*8)/2))), 54)
        oled.show()

        """___ Checking For Enter Button Press To Exit ___"""
        buttons.update()

        if buttons.pressed("enter"):
            displayState = 0

        time.sleep(0.1)
finally:
    blankOLED();
    

        

