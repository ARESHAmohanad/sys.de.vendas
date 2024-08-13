from tkinter import *
from tkinter import messagebox
import tkinter as tk
import webbrowser
import os
import sys
pro = Tk()
pro.geometry('850x520+280+50')
pro.resizable(False,False)
pro.title('Aplicativo De Vendas')
#pro.iconbitmap("home/muh443/Desktop/app/car.ico")
title = Label(pro , text='kibelicia',fg='gold',bg='black',font=('tajawal',16,'bold'))
title.pack(fill=X)

u1='https://www.ifood.com.br/delivery/florianopolis-sc/kibelicia--culinaria-arabe-centro/014f621e-c8aa-46c8-b238-ee9cbd62c882?UTM_Medium=share'
u2='https://api.whatsapp.com/send?phone=5548998215277&text=Gostataria%20de%20mais%20informa%C3%A7%C3%B5es%20sobre%20o%20Kibel%C3%ADcia'
u3='www.instagram.com/_kibelicia'
u4='https://kibelicia.wordpress.com'
u5='https://biolink.info/kibelicia?fbclid=PAZXh0bgNhZW0CMTEAAabnPG_hj17Ybys4lc5R0vX6XxMuy8eHRk1pCuqB_ZZRlGoJfoExNuA2uTM_aem_baH1adBqSQYGNtPyMRD7dw'

def open1():
    webbrowser.open_new_tab(u1)

def open2():
    webbrowser.open_new_tab(u2)

def open3():
    webbrowser.open_new_tab(u3)

def open4():
    webbrowser.open_new_tab(u4)

def open5():
    webbrowser.open_new_tab(u5)
#--------------------------------------------------------------------------------
#def about1():
#    messagebox.showinfo('mohanad aresha','muh')
#--------------------------------------------------------------------------------

def log():
    user = en1.get()
    passw = en2.get()
    if user == 'kibelicia' and passw == '12345' :
        messagebox.showinfo('oi','certo')
    else:
        messagebox.showerror('muhh','senha errada')







#--------------------------------------------------------------------------------
F1 = Frame(pro , width=280 , height=560 , bg='#0B2F3A')
F1.place(x=570,y=30)
title1 = Label(F1 , text='sistema de vendas' , bg='#0B2F3A' , fg='white' , font=('tajawal',12,'bold'))
title1.place(x=55,y=10)
title2 = Label(F1,text='criado por mohanad' , bg='#0B2F3A' , fg='white' , font=('tajawal',12,'bold'))
title2.place(x=50,y=50)
title3 = Label(F1 , text='nossos contatos 👇' , bg='#0B2F3A' , fg='white' , font=('tajawal',12,'bold'))
title3.place(x=62 ,y=90)

b1 = Button(F1, text='IFOOD' , width=26,fg='white',bg='green',font=('tajawal',11,'bold'), command=open1)
b1.place(x=6,y=130)

b2 = Button(F1, text='WHATSAPP' , width=26,fg='white',bg='green',font=('tajawal',11,'bold'), command=open2)
b2.place(x=6,y=190)

b3 = Button(F1, text='INSTAGRAM' , width=26,fg='white',bg='green',font=('tajawal',11,'bold'), command=open3)
b3.place(x=6,y=250)

b4 = Button(F1, text='CARDABIO' , width=26,fg='white',bg='green',font=('tajawal',11,'bold'), command=open4)
b4.place(x=6,y=310)

b5 = Button(F1, text='SITE' , width=26,fg='white',bg='green',font=('tajawal',11,'bold'), command=open5 )
b5.place(x=6,y=370)


f2 = Frame(pro , width=30, height=30 , bg='green')
f2.place(x=0, y=30)

f2 = Frame(pro , width=595, height=280 , bg='#0B2F3A')
f2.place(x=0, y=340)


photo2 = PhotoImage(file='/home/muh443/Desktop/app/kibe.png')
imo2 = Label(pro , image=photo2)
imo2.place(x=0 , y=30  )

l1 =Label(f2,text='usario:' ,fg='white', bg='#0B2F3A', font=('tajawal',14))
l1.place(x=130,y=54)
l1 =Label(f2,text='senha:' ,fg='white' ,  bg='#0B2F3A', font=('tajawal',14))
l1.place(x=130,y=100)

l1 =Label(f2,text='👤' , font=('tajawal',60))
l1.place(x=20,y=43)

en1 = Entry(f2 , font=('tajawal',13), justify='center')
en1.place(x=200,y=100)
en2 = Entry(f2 , font=('tajawal',13), justify='center')
en2.place(x=200,y=54)

b = Button(f2 , text='entrar' , bg='green',font=('tajawal',16), width=7 , height=2 ,command=log )
b.place(x=440,y=56)










pro.mainloop()


