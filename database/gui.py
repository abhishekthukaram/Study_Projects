from tkinter import *

window = Tk()


def miles_to_km():
    miles = float(entry_value.get())*1.6
    t1.insert(END, miles)


b1 = Button(window, text="Convert", command=miles_to_km)
b1.grid(row=0, column=0)

entry_value=StringVar()
e1 = Entry(window, text=entry_value)
e1.grid(row=0, column=1)

t1 = Text(window,height =1, width =15)
t1.grid(row=0,column=2)

window.mainloop()

