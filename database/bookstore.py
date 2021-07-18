from tkinter import *

window = Tk()
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Year")
l2.grid(row=1,column=0)

l3 = Label(window, text="Author")
l3.grid(row=0,column=2)

l4 = Label(window, text="ISBN")
l4.grid(row=1,column=2)


title = StringVar()
e1 = Entry(window, text=title)
e1.grid(row=0,column=1)

Year = StringVar()
e2 = Entry(window, text=Year)
e2.grid(row=1,column=1)

author = StringVar()
e3 = Entry(window, text=author)
e3.grid(row=0,column=3)

ISBN = StringVar()
e4 = Entry(window, text=ISBN)
e4.grid(row=1,column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

s1= Scrollbar(window)
s1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=s1.set)
s1.configure(command=list1.yview)

b1= Button(window,text="View All",width =12)
b1.grid(row=2,column=3)

b2= Button(window,text="Search Entry",width=12)
b2.grid(row=3,column=3)

b3= Button(window,text="Add Entry",width=12)
b3.grid(row=4,column=3)

b4= Button(window,text="Delete Entry",width=12)
b4.grid(row=5,column=3)

b5= Button(window,text="Update Entry",width=12)
b5.grid(row=6,column=3)

b6= Button(window,text="Close",width=12)
b6.grid(row=7,column=3)

window.mainloop()
