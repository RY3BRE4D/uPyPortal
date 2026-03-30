import urequests
from core.screenUtils import closeResponse


def getWeather(location):
    response = None

    try:
        if not location:
            return None

        lat = location.get("lat")
        lon = location.get("lon")

        if lat is None or lon is None:
            return None

        response = urequests.get(f"http://wttr.in/{lat},{lon}?format=%C|%t&u")
        weather = response.text.strip()

        if "|" not in weather:
            return None

        condition, temp = weather.split("|", 1)

        return {
            "condition": condition.strip(),
            "temp": temp.strip()
        }

    except Exception as e:
        print("Error Getting Weather:", e)
        return None

    finally:
        closeResponse(response)