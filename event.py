import tkinter

def Button1(event):
    root.title("Ліва кнопка миші")
def Button3(event):
    root.title("Права кнопка миші")
def MyMove(event):
    x = event.x
    y = event.y
    root.title("Рух мишею {}x{}".format(x, y))

root = tkinter.Tk()
root.minsize(width=1000, height=500)
root.bind('<Button-1>', Button1)
root.bind('<Button-3>', Button3)
root.bind('<Motion>', MyMove)
root.mainloop()