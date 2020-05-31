from tkinter import *
from tkinter.ttk import *


def convert(uin):
    from forex_python.converter import CurrencyRates
    c=CurrencyRates()#force_decimal=True
    sum=c.convert('USD','INR',uin)
    return sum

window=Tk()
window.title("Currency Converter verion 1.0_by :vishwa")
l0=Label(window,text="WELCOME TO CURRENCY CONVERTER",font=("Arial",20))
l0.grid(column=0,row=0)

l1=Label(window,text="Enter amount in Dollars $")
l1.grid(column=0,row=1)

txt=Entry(window,width=16)
txt.grid(column=0,row=3)


def clicked():
    from forex_python.converter import CurrencyRates
    c = CurrencyRates()  # force_decimal=True
    uin = int(txt.get())
    sum = c.convert('USD', 'INR', uin)

    l2.configure(text="The Amount in INR:"+str(sum))

bt1=Button(window,text="Convert to INR",command=clicked)
bt1.grid(column=0,row=4)
l2=Label(window,text="click on Convert button")
l2.grid(column=0,row=5)



window.geometry("400x350")
window.mainloop()
