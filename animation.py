import time
from tkinter import *
MyTk = Tk()
canvas = Canvas(MyTk, width=500, height=500)
canvas.pack()
# Створюємо трикутник за допомогою виклику create_polygon
canvas.create_polygon(10, 10, 10, 60, 50, 35)
def MyMove(MyX, MyY):
    for counter in range(0, 90):
        canvas.move(1, MyX, MyY)
        # Оновлення (перерисовка) зображення на екрані
        MyTk.update()
        time.sleep(0.01)
MyMove(5, 5); MyMove(-5, -5)
MyMove(5, 0); MyMove(-5, 0)
MyTk.mainloop()