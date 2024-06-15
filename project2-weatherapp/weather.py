import requests
import json
import pyttsx3

city=input("enter the name of the city\n")

url=f"https://api.weatherapi.com/v1/current.json?key=5afe9975b8c648cd87393144241006&q={city}"

r=requests.get(url)
# print(r.text)
wdic=json.loads(r.text)
w=wdic["current"]["temp_c"]

engine = pyttsx3.init()  # Initialize the TTS engine by creating an instance of pyttsx3.Engine
print(f"The current weather in {city} is {w} degrees")
engine.say(f"The current weather in {city} is {w} degrees")  # Storing the text for speech call
engine.runAndWait()