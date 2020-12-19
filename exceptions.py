# MyString = input("Введіть число: ")
# try:
#     MyNumber = int(MyString)
#     print(MyNumber)
# except:
#     print("Помилка перетворення числа!")
# except Exception:
#     print("Загальне виключення")
MyString = input("Введіть число 1: ")
MyString2 = input("Введіть число 2: ")
try:
    MyNumber = int(MyString)
    MyNumber2 = int(MyString2)
    if MyNumber2 == 0:
        raise Exception("Друге число не повинно бути дорівнює 0")
    print("Результат: "+str(MyNumber / MyNumber2))
except ValueError as e:
    print("Опис помилки: ", e)
except ZeroDivisionError:
    print("Спроба ділення на нуль!")
finally:
    print("Завершили виконання")