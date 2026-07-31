from tkinter import *
from tkcalendar import Calendar,DateEntry
from tkinter import ttk
from PIL import ImageTk,Image
import datetime
from tkinter import messagebox

top=Tk()
top.geometry("1350x700")
top.title("welcome")
top.resizable(0,0)

def loginFetch():
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='sonu#7535', db='data')
    cur = db.cursor()
    cur.execute("select * from registration where name=%s and password=%s",(e1.get(),e2.get()))
    row=cur.fetchone()

    if row == None:
        messagebox.showinfo("Error","Invalid User Name And Password  ")
    else:
        top.destroy()
        import registration

def showpassword():
    if e2.cget('show') == "*":
        e2.config(show='')
    else:
        e2.config(show="*")

homeimg = ImageTk.PhotoImage(file=r"C:\Users\sonup\OneDrive\Desktop\form.jpg")

var=StringVar()

L44=Label(top,image=homeimg)
L44.pack()

L=Label(top,text="Login",fg="white",bg="purple",font=("Arial 25 bold"))
L.place(x=500,y=10)



L1=Label(top,text="Name",fg="white",bg="purple",font=("Arial 20 bold"))
L1.place(x=100,y=150)

e1=Entry(top,font=("Arial 20 bold"))
e1.place(x=290,y=150)

L2=Label(top,text="Password",fg="white",bg="purple",font=("Arial 20 bold"))
L2.place(x=100,y=200)

e2=Entry(top,font=("Arial 20 bold"),show="*")
e2.place(x=290,y=200)



b6=Button(top,text='Login',font=("Arial 20 bold"),command=loginFetch)
b6.place(x=336,y=300)

top.mainloop()
