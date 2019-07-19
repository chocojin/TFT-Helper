from tkinter import *

class App:
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button1 = Button(frame, text="Quit", fg="red", command=frame.quit)
        self.button1.pack(side=LEFT)

root = Tk()

app = App(root)

root.mainloop()
