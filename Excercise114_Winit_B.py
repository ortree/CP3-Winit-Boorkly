from forex_python.converter import *
from forex_python.bitcoin import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
import requests
currencyRate = CurrencyRates()
currencyCode = CurrencyCodes()
#bitcoin = BtcConverter()



#UI

# add widgets here
form =Tk()
form.title('Converter')
form.geometry('600x400')

#Function

dropclick1 = StringVar()
dropclick1.set(currencyCode.get_some_code_list()[0])
dropclick2 = StringVar()
dropclick2.set(currencyCode.get_some_code_list()[1])

def entryChange1(entryevent1):
    try:
        int(entryevent1.get())
        print('entryChange1:', type(entryevent1.get()))
        result = currencyRate.convert(dropclick1.get(),dropclick2.get(),float(entryevent1.get()))
        entryevent2.set(result)
    except ValueError:
        entryevent1.set('')


entryevent1 = StringVar()
entryevent1.trace("w", lambda name, index, mode, sv=entryevent1: entryChange1(entryevent1))

def entryChange2(entryevent2):
    try:
        int(entryevent2.get())
        print('entryChange2:', entryevent2.get())
        result = currencyRate.convert(dropclick2.get(), dropclick1.get(), float(entryevent2.get()))
        entryevent1.set(result)
    except ValueError:
        entryevent2.set('')


entryevent2 = StringVar()
entryevent2.trace("w", lambda name, index, mode, sv=entryevent2: entryChange2(entryevent2))



def changeDrop1(*drop):
    try:
        int(entryevent1.get())
        #print('changedrop 1 :', dropclick1.get())
        result = currencyRate.convert(dropclick1.get(), dropclick2.get(), float(entryevent1.get()))
        entryevent2.set(result)
    except ValueError:
        entryevent1.set('')

dropclick1.trace("w", changeDrop1)

def changeDrop2(*drop):
    try:
        int(entryevent2.get())
        #print('changedrop 2 :',dropclick2.get())
        result = currencyRate.convert(dropclick2.get(),dropclick1.get() ,float(entryevent2.get()))
        entryevent1.set(result)
    except ValueError:
        entryevent2.set('')

dropclick2.trace("w", changeDrop2)





#tab control
tabControl = ttk.Notebook(form)
tabControl.pack()
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Fiat Converter ')
tabControl.add(tab2, text='BTC Converter')
tabControl.pack(expand=1, fill="both")

#tab1 container
fiatConvertFrame1 = Frame(tab1,bg='#80c1ff',bd=5)
fiatConvertFrame1.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

fiatConvertFrame2 = Frame(tab1, bg= '#80c1ff', bd=5)
fiatConvertFrame2.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.1, anchor='n')

fiatEntry1 = Entry(fiatConvertFrame1,font=28,  textvariable=entryevent1)
fiatEntry1.place(relwidth=0.65, relheight=1)

fiatDrop1 = OptionMenu(fiatConvertFrame1,dropclick1,*currencyCode.get_some_code_list())
fiatDrop1.place(relx=0.7, relwidth=0.3, relheight=1)


fiatEntry2 = Entry(fiatConvertFrame2 ,font=28,  textvariable=entryevent2)
fiatEntry2.place(relwidth=0.65, relheight=1)

fiatDrop2 = OptionMenu(fiatConvertFrame2,dropclick2 ,*currencyCode.get_some_code_list())
fiatDrop2.place(relx=0.7, relwidth=0.3, relheight=1)


form.mainloop()




