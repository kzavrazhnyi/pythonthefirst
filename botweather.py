# ----------------- botweather.py

# Free https://openweathermap.org/current

import requests
import json
import config as Conf

def AnswerUserBot(MyData, CurrentTelegramId):
    data = {
        'chat_id': CurrentTelegramId,
        'text':MyData
    }
    BotUrl = Conf.BotUrl.format(method = Conf.TelegramSend)
    requests.post(BotUrl, data=data)

def ParseWeatherData(MyData):
    WeatherState = ''
    for MyElem in MyData['weather']:
        WeatherState = MyElem['main']
    WeatherTemp = MyData['main']['temp']
    WeatherCity = MyData['name']
    return f'The weather in {WeatherCity}: Temp is {WeatherTemp}, state is {WeatherState}'

def GetWeather(MyLocation):
    OpenWeatherUrl = Conf.OpenWeatherUrl.format(city=MyLocation)
    response = requests.get(OpenWeatherUrl)
    if response.status_code != 200:
        return 'City not found!'
    WeatherData = json.loads(response.content)
    return ParseWeatherData(WeatherData)

def GetMessage(MyData):
    return MyData['message']['text']

def SaveNewTelegramIdStr(NewTelegramIdStr):
    with open(Conf.TelegramIdFilePath, 'w') as file:
        file.write(NewTelegramIdStr)

def BotWeather():
    while True:
        BotUrl = Conf.BotUrl.format(method=Conf.TelegramUpdate.format(update_id=Conf.TelegramUpdateId+1))
        BotContent = requests.get(BotUrl).text

        BotData = json.loads(BotContent)
        SortResult = BotData['result']

        for MyElem in SortResult:
            NewTelegramId = MyElem['update_id']
            try:
                MyElemMes = MyElem['message']
            except:
                continue
            if MyElemMes['text'] == "/start":
                Conf.TelegramUpdateId = NewTelegramId
                SaveNewTelegramIdStr(str(NewTelegramId))
            else:
                NewTelegramId = MyElem['update_id']
                if Conf.TelegramUpdateId != NewTelegramId:
                    Conf.TelegramUpdateId = NewTelegramId
                    MyMessage = GetMessage(MyElem)
                    MyWeather = GetWeather(MyMessage)
                    print("From: " + MyElemMes['from']['first_name']
                          + " Message: " + MyMessage + " Answer: " + MyWeather)
                    AnswerUserBot(MyWeather, MyElemMes['chat']['id'])
                    SaveNewTelegramIdStr(str(NewTelegramId))


BotWeather()

# ----------------- config.py

# WeatherNew2023_bot
# https://home.openweathermap.org/api_keys

Token = ''
BotUrl = 'https://api.telegram.org/bot'+Token+'/{method}'

TelegramIdFilePath = 'telegram_id'

with open(TelegramIdFilePath) as file:
    TelegramUpdateId = file.readline()
    TelegramUpdateId = int(TelegramUpdateId)

TelegramUpdate = 'getUpdates?offset={update_id}'
TelegramSend = 'sendMessage'

with open('weather_token') as file:
    OpenWeatherToken = file.readline()

OpenWeatherUrl = 'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid='+OpenWeatherToken

# ----------------- telegram_id
0

# ----------------- weather_token

