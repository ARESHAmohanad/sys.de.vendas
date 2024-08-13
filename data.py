from tkinter import *
import math
import os 
import random
from tkinter import messagebox

class super:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1300x700+30+10')
        self.root.title('kibelicia')
        self.root.resizable(False,False)
#        self.root.iconbitmap('')
        title = Label(self.root, text='produtos' , fg='white',bg='gray',font=('fajawal',16))
        title.pack(fill=X)


root=Tk()
ob = super(root)
root.mainloop()