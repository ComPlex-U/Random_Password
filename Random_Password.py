import string
from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.geometry('300x100')
root.config(bg='black')

def getp():
    randoom = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(9)])
    print(randoom)
    messagebox._show(title='Pass', message={randoom})

Label(text='-----------PASS GENERATOR-----------', font=12).pack(fill='x', pady=6)
button1=Button(text='GERAR', command=getp, padx=10).pack(pady=2)
root.mainloop()