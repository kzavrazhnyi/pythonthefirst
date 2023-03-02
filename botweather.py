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
    # виконувати цикл нескінченно до перерви програми
    while True:
        # Сформувати строку запиту на отримання оновлень даних бота
        # беремо останній ID запиту бота і додаємо 1
        BotUrl = Conf.BotUrl.format(method=Conf.TelegramUpdate.format(update_id=Conf.TelegramUpdateId+1))
        # Виконуємо запит і отримаємо дані в форматі json
        BotContent = requests.get(BotUrl).text

        # Читаємо отримані дані в структуру
        BotData = json.loads(BotContent)
        # З даних беремо елемент result
        SortResult = BotData['result']

        # Перебираємо елементи пакету даних бота
        for MyElem in SortResult:
            # Отримаємо Id елемента
            NewTelegramId = MyElem['update_id']
            # Блок отримання елемента message з перевіркою на помилку
            try:
                # Отримаємо елемент message
                MyElemMes = MyElem['message']
            # Виключення якщо помилка
            except:
                # Продовжити цикл
                continue
            # Якщо text елемента це /start пропускаємо аналіз і записуємо перевірений Id в файл
            if MyElemMes['text'] == "/start":
                Conf.TelegramUpdateId = NewTelegramId
                SaveNewTelegramIdStr(str(NewTelegramId))
            # інакше якщо збережений перевірений Id не дорівнює новому тоді
            elif Conf.TelegramUpdateId != NewTelegramId:
                    # зберігаємо новий Id
                    Conf.TelegramUpdateId = NewTelegramId
                    # отримаємо повідомлення бота
                    MyMessage = GetMessage(MyElem)
                    # передаємо повідомлення бота для запиту прогнозу погоди
                    MyWeather = GetWeather(MyMessage)
                    # виводимо на печать інформацію від кого повідомелення та відповідь на нього
                    print("From: " + MyElemMes['from']['first_name']
                          + " Message: " + MyMessage + " Answer: " + MyWeather)
                    # передаємо відповідь в бот
                    AnswerUserBot(MyWeather, MyElemMes['chat']['id'])
                    # записуємо в файл Id обробленого повідомлення
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

