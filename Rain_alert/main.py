import load_dotenv
import requests
from twilio.rest import Client
import os

load_dotenv()

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
api_key = os.getenv("api_key")
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")

weather_params = {
    "lat": 46.947975,
    "lon": 7.447447,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"])

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today ☔",
        from_='+19342465468',
        to='+916361736795',
    )
    print(message.sid)