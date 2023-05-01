import smtplib
import time

import requests
from datetime import datetime

MY_LAT=13.309510 # my Lat
MY_LONG=52.473200 # my Long
MY_EMAIL ="mmytest779@gmail.com"
MY_PASSWORD ="1234567@abc%$"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # If the ISS is close to my current position
    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5<=iss_latitude<=MY_LAT+5 and MY_LONG-5<=iss_longitude<=MY_LONG+5:
        return True

def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    # and it is currently dark
    if time_now >= sunset or time_now <= sunrise:
        return True
while True:
    time.sleep(60)
    # Then send me an email to tell me to look up.
    if is_iss_overhead() and is_night():
        connection= smtplib.SMTP("stmp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg="Subject: ISS Location \n\n ISS is above you in the sky")
    # BONUS: run the code every 60 seconds.




