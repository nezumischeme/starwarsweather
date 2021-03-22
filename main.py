import requests
import random
from sanic import Sanic
from sanic.response import json

app = Sanic("Star Wars Weather app")

def starWars(temp):
  temp = int(temp)
  if temp < 5:
    return "Hoth"
  elif temp > 26:
    return "Tatooine"
  else:
    return random.choice(['Alderaan', 'Naboo'])

def getPlanet(city):
    cityName = city
    r = requests.get(f'http://wttr.in/{cityName}?format=j1')
    tempC = r.json()['current_condition'][0]['temp_C']
    planetName = starWars(tempC)
    return [planetName, tempC]

def celsiusToF(temp):
    fahrenheit = (temp * 9/5) + 32
    return fahrenheit

@app.route('/api')
async def default(request):
    return text("Enter a city.")

@app.route('/api/<city>')
async def test(request, city):
    userPlanet = getPlanet(city)
    return json({'planet': userPlanet[0], 'tempC': userPlanet[1], 'tempF': celsiusToF(float(userPlanet[1]))})

app.static("/static", "./static")
app.static("/", "./views/index.html")

if __name__ == '__main__':
    app.run()