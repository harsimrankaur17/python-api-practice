import requests

city = input("Please enter your city: ")

params1 = {
    "name": city,
    "count": 10,
    "language": "en",
    "format": "json"
}

r = requests.get(
    "https://geocoding-api.open-meteo.com/v1/search",
    params=params1
)

data = r.json()

latitude = data["results"][0]["latitude"]
longitude = data["results"][0]["longitude"]

params2 = {
    "latitude": latitude,
    "longitude": longitude,
    "current": "temperature_2m,wind_speed_10m"
}

r2 = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params=params2
)

data2 = r2.json()

print("Time:", data2["current"]["time"])
print("Temperature:", data2["current"]["temperature_2m"])
print("Wind speed:", data2["current"]["wind_speed_10m"])
