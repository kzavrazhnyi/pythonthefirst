import tkinter

class Paint(tkinter.Frame):

    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)

        self.Parent = parent
        self.ColorBrush = "blue"
        self.SizeBrush = 1
        self.SetMyGUI()

    def draw(self, event):
        self.canv.create_oval(event.x - self.SizeBrush,
                              event.y - self.SizeBrush,
                              event.x + self.SizeBrush,
                              event.y + self.SizeBrush,
                              fill=self.ColorBrush, outline=self.ColorBrush)

    def SetMyGUI(self):
        # Встановлюємо назву вікна
        self.Parent.title("Мій Paint")
        # Розміщуємо активні елементи на батьківському вікні
        self.pack(fill=tkinter.BOTH, expand=1)
        # Даємо можливість розтягуватися
        self.columnconfigure(6, weight=1)
        self.rowconfigure(2, weight=1)
        # Створюємо поле для малювання на білому фоні
        self.canv = tkinter.Canvas(self, bg="white")
        # Прикріплюємо canvas методом grid
        self.canv.grid(row=2, column=0, columnspan=7,
                       padx=5, pady=5, sticky=tkinter.E+tkinter.W+tkinter.S+tkinter.N)
        # Прив'язуємо обробник <B1-Motion> "при русі затиснутою лівої кнопки миші" викликати функцію draw
        self.canv.bind("<B1-Motion>", self.draw)

def main():
    MyTk = tkinter.Tk()
    MyTk.geometry("1000x600+500+500") # widthxheight+x+y
    MyApp = Paint(MyTk)
    MyTk.mainloop()

main()