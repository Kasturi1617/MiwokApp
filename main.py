import requests
from twilio.rest import Client

account_sid = "ACa2e3b27862385c1e73bc7cff27f42e2a"
auth_token = "b13ec3b228165b53a14ab85529d11165"
# MY_LAT = 22.572645
# MY_LONG = 88.363892
MY_LAT = -8.075820
MY_LONG = 111.101230
MY_API = "c6c8d6ae3d76961c51805cdf5cf059f7"
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": MY_API,
    "exclude": {"current,minutely,daily"},
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = response.json()["hourly"][:12]
will_rain = False

for hour_data in weather_slice:
    weather_code = hour_data["weather"][0]["id"]
    if int(weather_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Bring an ☂️☔",
        from_="+19105861848",
        to="+917980429709"
    )
    print(message.status)
    message = client.messages \
        .create(
        body="It's going to rain today. Bring an ☂️☔",
        from_="+19105861848",
        to="+919674297042"
    )

