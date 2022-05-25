#!/usr/bin/python3.10.4

from requests import request
import json

url =  "https://api.openweathermap.org/data/2.5/weather?lat=37.560092&lon=126.919925&appid=f207fd8d68aa40b9800315db70748f36"
req = request("GET", url)
result = dict(json.loads(req.text))

temp = str(int(result["main"]["temp"] - 273.15)) + "°C"

print(temp)
