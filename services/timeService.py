import ntptime
import time
from services.locationService import getLocation


cachedUtcOffset = None
cachedOffsetTime = 0


def syncTime(retries=3):
    for i in range(retries):
        try:
            ntptime.settime()
            return True
        except OSError:
            print(f"NTP Sync Failed, Retrying {i + 1}/{retries}...")
            time.sleep(2)

    print("Failed To Sync Time!")
    return False


def getUtcOffset():
    global cachedUtcOffset, cachedOffsetTime

    now = time.time()

    if cachedUtcOffset is not None and (now - cachedOffsetTime) < 1800:
        return cachedUtcOffset

    location = getLocation()

    if location and "offset" in location:
        cachedUtcOffset = int(location["offset"])
        cachedOffsetTime = now
        return cachedUtcOffset

    return None


def getTime():
    try:
        utcOffset = getUtcOffset()

        if utcOffset is None:
            print("No UTC Offset Available!")
            return None

        currentTime = time.localtime(time.time() + utcOffset)
        return currentTime

    except Exception as e:
        print(f"Error Getting Time: {e}")
        return None