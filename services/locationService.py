import urequests
from core.screenUtils import closeResponse


def getLocation():
    response = None

    try:
        response = urequests.get(
            "http://ip-api.com/json/?fields=status,message,city,regionName,country,lat,lon,timezone,offset,isp,as,query"
        )
        data = response.json()

        if data.get("status") == "success":
            return data

        print("Location API Returned Error:", data)
        return None

    except Exception as e:
        print("Error Getting Location:", e)
        return None

    finally:
        closeResponse(response)