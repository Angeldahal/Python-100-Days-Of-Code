import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os



api_key = "50a2de7b5c11efbfc0070a0e43daa0b9"
parameters = {
    "lat" : 26.796946,
    "lon" : 87.291290,
    "exclude":"current,minutely,daily",
    "appid" : api_key,
}

account_sid = os.environ.get("ACCOUNT_SID")
auth_token =os.environ.get("AUTH_TOKEN")

response = requests.get(url = "https://api.openweathermap.org/data/2.5/onecall", params = parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:11]
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body= "It's going to rain today. Remember to bring an umbrella.",
            from_ = "+15164004128",
            to = "+9779806736272",
        )
    print(message.status)