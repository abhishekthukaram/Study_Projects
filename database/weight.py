from tkinter import *

window = Tk()


def convertfromkg():
    grams = float(input_kg.get())*1000
    grams_output = str(grams) + " " + "grams"
    t1.insert(END,grams_output)
    pounds = float(input_kg.get())*2.20462
    pounds_output = str(pounds) + " " + "pounds"
    t2.insert(END,pounds_output)
    ounces = float(input_kg.get())*35.274
    ounces_output=str(ounces)+ " "+"ounces"
    t3.insert(END,ounces_output)


e1= Label(window,text="Kg")
e1.grid(row=0,column=0)

input_kg = StringVar()
entry = Entry(window, text=input_kg)
entry.grid(row=0, column=1)

b1 = Button(window, text="Convert", command=convertfromkg)
b1.grid(row=0, column=2)


t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)


window.mainloop()