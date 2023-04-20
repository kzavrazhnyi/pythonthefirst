import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Завантажуємо дані з файлу
df = pd.read_csv('saveecobot_19708.csv')

# Конвертуємо колонку logged_at в об'єкти дати-часу
df['logged_at'] = pd.to_datetime(df['logged_at'])

# Визначаємо кінцеву дату
end_date = df['logged_at'].max()

# Визначаємо початкову дату (два дні до кінцевої дати)
start_date = end_date - timedelta(days=2)

# Фільтруємо дані за потрібним періодом та для показників pm10, pm25, temperature, humidity, heca_temperature, heca_humidity
filtered_df = df[(df['logged_at'] >= start_date) & (df['logged_at'] <= end_date) & (df['phenomenon'].isin(['pm10', 'pm25', 'temperature', 'humidity', 'heca_temperature', 'heca_humidity']))]

# Розбиваємо дані на групи за показником
groups = filtered_df.groupby('phenomenon')

# Створюємо нове вікно для графіків
fig, ax = plt.subplots(figsize=(10, 6))

# Проходимо по кожній групі та створюємо відповідний графік
for name, group in groups:
    ax.plot(group['logged_at'], group['value'], label=name)

# Налаштовуємо візуалізацію графіків
plt.title('Динаміка показників')
plt.xlabel('Дата')
plt.ylabel('Значення')
plt.legend(loc='best')

# Показуємо графіки
plt.show()
