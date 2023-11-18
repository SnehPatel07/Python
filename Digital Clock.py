from tkinter import *
from tkinter.ttk import *
from time import strftime

a = Tk()

a.title("Digital clock")
a.configure(background="black")
def clock():
    t = strftime("%I:%M:%S %p")
    label.config(text =t)
    label.after(1000, clock)

label = Label(a, font=('arial',60),foreground = "red", background = "black")

label.pack(anchor= "center")

clock()
a.mainloop()