def MyCalculate(MyRate, MyMoney, MyMonth):
    if MyMoney <= 0:
        return 0
    for i in range(1, MyMonth + 1):
        MyMoney = round(MyMoney + MyMoney * MyRate / 100 / 12, 2)
    return MyMoney