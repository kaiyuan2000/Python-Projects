import requests
import datetime as dt
import smtplib

MY_LAT = 3.139003
MY_LONG = 101.686852
MY_EMAIL = "EMAIL"
MY_PASSWORD = "PASSWORD"

def is_above():
    # get ISS coordinates
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])

    if abs(longitude - MY_LONG) <=5 and abs(latitude - MY_LAT) <=5:
        return True

def is_dark():
    # Get sunset & sunrise time
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    #change into Malaysia UTC+8 timezone
    sunrise_hour = (int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 8) % 24
    sunset_hour = (int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 8) % 24
    time_now_hour = dt.datetime.now().hour
    if sunrise_hour <= time_now_hour <= sunset_hour:
        return False
    else :
        return True

#if ISS is above given coordinates and the sky is dark, send email
if is_dark() and is_above() :
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up !! \n\n ISS is above you, look up now"
        )
