# https://tlgrm.ru/docs/bots/api
# Free https://openweathermap.org/current

import requests
import json
import config as Conf

def AnswerUserBot(MyData):
    data = {
        'chat_id':Conf.MyTelegramId,
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
        BotUrl = Conf.BotUrl.format(method=Conf.TelegramUpdate)
        BotContent = requests.get(BotUrl).text

        BotData = json.loads(BotContent)
        SortResult = BotData['result'][::-1]
        MyMessageResult = None

        for MyElem in SortResult:
            if MyElem['message']['chat']['id'] == Conf.MyTelegramId:
                MyMessageResult = MyElem
                break

        if  MyMessageResult != None:
            NewTelegramIdStr = str(MyMessageResult['update_id'])

            if not Conf.TelegramUpdateId:
                with open(Conf.TelegramIdFilePath,'w') as file:
                    file.write(NewTelegramIdStr)

            if Conf.TelegramUpdateId != NewTelegramIdStr:
                Conf.TelegramUpdateId = NewTelegramIdStr
                MyMessage = GetMessage(MyMessageResult)
                MyWeather = GetWeather(MyMessage)
                AnswerUserBot(MyWeather)
                SaveNewTelegramIdStr(NewTelegramIdStr)

BotWeather()