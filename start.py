import account

MyRate = int(input("Введіть процентну ставку: "))
MyMoney = int(input("Введіть суму: "))
MyPeriod = int(input("Введіть період ведення рахунку в місцях: "))

MyResult = account.MyCalculate(MyRate, MyMoney, MyPeriod)
print("Параметри рахунку:\n", "Сума: ", MyMoney, "\n", "Ставка: ", MyRate, "\n",
      "Період: ", MyPeriod, "\n", "Сума на рахунку в кінці періоду: ", MyResult)