# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import os
import smtplib
import requests
from twilio.rest import Client

api_key = secrets.OWM_API_KEY
account_sid = secrets.ACCT_SID
auth_token = secrets.AUTH_TOKEN

MY_EMAIL = secrets.MY_EMAIL
MY_PASSWORD = secrets.MY_PASSWORD

params = {
    "lat": -4.273897,
    "lon": 15.281513,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=params)
response.raise_for_status()
data = response.json()
http_status = data["cod"]
weather_list = data["list"]

will_rain = False

for w in weather_list:
    if w["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_="+17372212163",
        to="+2347035553312",
    )
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="okekevictor98@gmail.com",
                                msg="Subject: Hey, Pretty\n\nHow're you doing today, just so you know it's "
                                    "going to rain somewhere in Lagos today don't forget to leave home with your "
                                    "umbrella. Do have a nice day :) ")
        print("mail sent")
    print(message.status)
