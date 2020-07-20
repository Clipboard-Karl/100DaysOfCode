#100DaysOfCode 032/100 - GUI with Tkinter
#
#  20200720 - 100DaysOfCode 032/100 - Tkinter and GUI
#     Tkinter is a built in pyton library
#
#
################################################################################
#
from tkinter import *

window=Tk()

def km_to_miles():
    print(e1_value.get())
    miles=float(e1_value.get())*1.6
    t1.insert(END,miles)

b1=Button(window,text="Execute",command=km_to_miles)
b1.grid(row=0,column=0)   #alternate would be jut b1.pack()

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=25)
t1.grid(row=0,column=2)


# this is the end of the loop for the window
window.mainloop()
