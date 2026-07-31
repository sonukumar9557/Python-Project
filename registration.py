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

def UpdateFrom():
    top2 = Toplevel()
    top2.geometry("1350x700")
    top2.title("welcome")
    top2.resizable(0, 0)

    def Update():
        k = e1.get()  # 1 name
        k2 = e2.get()  # 2 lastname
        k3 = int(e3.get())  # 3 contact
        #k4 = e4.get()  # 4 city
        k5 = e5.get()  # 5 email
        k6 = e6.get()  # 6 password
        format = '%m/%d/%y'
        s = cal.get()
        date = datetime.datetime.strptime(s, format)
        n = date.strftime('%y-%m-%d')  # 7 date

        k7 = cb.get()  # 4 city
        k8 = var.get()  # 8 gender
        import pymysql as sql
        db = sql.connect(host='localhost', user='root', password='YOUR_PASSWORD', db='data')
        cur = db.cursor()
        s="update registration set Name=%s,Lastname=%s,Contact=%s,City=%s,Password=%s,Date=%s,Gender=%s where Email=%s"

        g=(k,k2,k3,k7,k6,n,k8,k5)
        result = cur.execute(s,g)
        if (result > 0):
            messagebox.showinfo("Result", "your record Update successfully")
        else:
            messagebox.showinfo("Result", "Your record not Updated")
    
        db.commit()
        e1.delete(0, 'end')
        e2.delete(0, 'end')
        e3.delete(0, 'end')
        e4.delete(0, 'end')
        e5.delete(0, 'end')
        e6.delete(0, 'end')
        cb.current(0)



    homeimg = ImageTk.PhotoImage(file=r"C:\Users\sonup\OneDrive\Desktop\form.jpg")

    var = StringVar()

    L44 = Label(top2, image=homeimg)
    L44.pack()


    k = ['Select', 'Meerut', 'Delhi', 'Noida', 'Dehradun', 'Chambal', 'Gurgaon', 'Jaipur', 'Haridwar', 'Bijnor']

    L = Label(top2, text="Registration", fg="white", bg="purple", font=("Arial 25 bold"))
    L.place(x=500, y=10)

    L1 = Label(top2, text="Name", fg="white", bg="purple", font=("Arial 20 bold"))
    L1.place(x=100, y=150)

    e1 = Entry(top2, font=("Arial 20 bold"))
    e1.place(x=290, y=150)

    L2 = Label(top2, text="Lastname", fg="white", bg="purple", font=("Arial 20 bold"))
    L2.place(x=100, y=200)

    e2 = Entry(top2, font=("Arial 20 bold"))
    e2.place(x=290, y=200)

    L3 = Label(top2, text="Contact", fg="white", bg="purple", font=("Arial 20 bold"))
    L3.place(x=100, y=250)

    e3 = Entry(top2, font=("Arial 20 bold"))
    e3.place(x=290, y=250)

    L4 = Label(top2, text="City", fg="white", bg="purple", font=("Arial 20 bold"))
    L4.place(x=100, y=300)

    # e4 = Entry(top2, font=("Arial 20 bold"))
    # e4.place(x=290, y=300)

    cb = ttk.Combobox(top2, values=k, font=("Arial 19 bold"))
    cb.place(x=290, y=300)

    cb.current(0)

    L5 = Label(top2, text="Email", fg="white", bg="purple", font=("Arial 20 bold"))
    L5.place(x=100, y=350)

    e5 = Entry(top2, font=("Arial 20 bold"))
    e5.place(x=290, y=350)

    L6 = Label(top2, text="Password", fg="white", bg="purple", font=("Arial 20 bold"))
    L6.place(x=100, y=400)

    e6 = Entry(top2, font=("Arial 20 bold"), show="*")
    e6.place(x=290, y=400)

    l7 = Label(top2, text='Date', fg="white", bg="purple", font=("Arial 20 bold"))
    l7.place(x=100, y=450)

    cal = DateEntry(top2, width=19, bg="Dark blue", fg='white', year=2010, font=("Arial 20 bold"))
    cal.place(x=290, y=450)

    c1 = Checkbutton(top2, font=("Arial 15 bold"), command=showpassword)
    c1.place(x=565, y=400)

    b3 = Button(top2, text='Update', font=("Arial 20 bold"),command=Update)
    b3.place(x=540, y=570)

    l8 = Label(top2, text='Gender', fg="white", bg="purple", font=("Arial 20 bold"))
    l8.place(x=100, y=500)

    r1 = Radiobutton(top2, text='Male', variable=var, value='Male', font=("Arial 17 bold"))
    r1.place(x=290, y=500)

    r2 = Radiobutton(top2, text='FeMale', value='Female', variable=var, font=("Arial 17 bold"))
    r2.place(x=390, y=500)

    r3 = Radiobutton(top2, text='Other', value='OTHER', variable=var, font=("Arial 17 bold"))
    r3.place(x=522, y=500)


def login():
    top.destroy()
    import login

def Search():
    k = e1.get()
    for i in tv.get_children():
        tv.delete(i)
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='YOUR_PASSWORD', db='data')
    cur = db.cursor()
    p = "select * from registration where name=%s"
    cur.execute(p,k)
    result = cur.fetchall()
    for col in result:
        name=col[0]
        lastname=col[1]
        contact=col[2]
        city=col[3]
        email=col[4]
        password=col[5]
        date=col[6]
        gender=col[7]
        tv.insert("",'end',values=(name,lastname,contact,city,email,password,date,gender))

def showpassword():
    if e6.cget('show') == "*":
        e6.config(show='')
    else:
        e6.config(show="*")

def show():

    for i in tv.get_children():
        tv.delete(i)
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='YOUR_PASSWORD', db='data')
    cur = db.cursor()
    p = "select * from registration"
    cur.execute(p)
    result=cur.fetchall()
    for col in result:
        name=col[0]
        lastname=col[1]
        contact=col[2]
        city=col[3]
        email=col[4]
        password=col[5]
        date=col[6]
        gender=col[7]
        tv.insert("",'end',values=(name,lastname,contact,city,email,password,date,gender))
        #print(name,lastname,contact,city,email,password,date,gender)


def Delete():
    k = e1.get()
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='YOUR_PASSWORD', db='data')
    cur = db.cursor()
    s = "delete from registration where name=%s"
    result = cur.execute(s, k)
    if (result > 0):
        messagebox.showinfo("Result", "your record delete successfully")
    else:
        messagebox.showinfo("Result", "Your record not deleted")
    db.commit()


def Insert():
    k=e1.get() # 1 name
    k2=e2.get() # 2 lastname
    k3=int(e3.get()) # 3 contact
    k4=e4.get() # 4 city
    k5=e5.get() # 5 email
    k6=e6.get()  # 6 password
    format = '%m/%d/%y'
    s = cal.get()
    date = datetime.datetime.strptime(s, format)
    n = date.strftime('%y-%m-%d') # 7 date

    k7=cb.get() # 4 city
    k8=var.get() # 8 gendear

    import pymysql as sql
    db=sql.connect(host="localhost",user="root",passwd="YOUR_PASSWORD",db="data")
    cur=db.cursor()
    s="Insert into registration values('%s','%s','%s','%s','%s','%s','%s','%s')"%(k,k2,k3,k7,k5,k6,n,k8)
    result=cur.execute(s)
    if(result > 0):
        messagebox.showinfo("Result","Your record is successfully added")
    else:
        messagebox.showinfo("Result","Your record is already added")
    db.commit()
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')
    e5.delete(0, 'end')
    e6.delete(0, 'end')
    cb.current(0)


homeimg = ImageTk.PhotoImage(file=r"C:\Users\sonup\OneDrive\Desktop\form.jpg")

var=StringVar()

L44=Label(top,image=homeimg)
L44.pack()

tv = ttk.Treeview(top,height=16)
tv['columns']=('Name','Lastname','Contact','City','Email','Password','Date','Gender')

tv.column('#0', width=0, stretch=NO)
tv.column('Name', anchor=CENTER, width=90)
tv.column('Lastname', anchor=CENTER, width=90)
tv.column('Contact', anchor=CENTER, width=90)
tv.column('City', anchor=CENTER, width=90)
tv.column('Email', anchor=CENTER, width=90)
tv.column('Password', anchor=CENTER, width=90)
tv.column('Date', anchor=CENTER, width=90)
tv.column('Gender', anchor=CENTER, width=90)


tv.heading('Name', text='Name', anchor=CENTER)
tv.heading('Lastname', text='Lastname', anchor=CENTER)
tv.heading('Contact', text='Contact', anchor=CENTER)
tv.heading('City', text='City', anchor=CENTER)
tv.heading('Email', text='Email', anchor=CENTER)
tv.heading('Password', text='Password', anchor=CENTER)
tv.heading('Date', text='Date', anchor=CENTER)
tv.heading('Gender', text='Gender', anchor=CENTER)

tv.place(x=625,y=150)



k=['Select','Meerut','Delhi','Noida','Dehradun','Chambal','Gurgaon','Jaipur','Haridwar','Bijnor']

L=Label(top,text="Registration",fg="white",bg="purple",font=("Arial 25 bold"))
L.place(x=500,y=10)



L1=Label(top,text="Name",fg="white",bg="purple",font=("Arial 20 bold"))
L1.place(x=100,y=150)

e1=Entry(top,font=("Arial 20 bold"))
e1.place(x=290,y=150)

L2=Label(top,text="Lastname",fg="white",bg="purple",font=("Arial 20 bold"))
L2.place(x=100,y=200)

e2=Entry(top,font=("Arial 20 bold"))
e2.place(x=290,y=200)


L3=Label(top,text="Contact",fg="white",bg="purple",font=("Arial 20 bold"))
L3.place(x=100,y=250)

e3=Entry(top,font=("Arial 20 bold"))
e3.place(x=290,y=250)


L4=Label(top,text="City",fg="white",bg="purple",font=("Arial 20 bold"))
L4.place(x=100,y=300)

e4=Entry(top,font=("Arial 20 bold"))
e4.place(x=290,y=300)

cb=ttk.Combobox(top,values=k,font=("Arial 19 bold"))
cb.place(x=290,y=300)

cb.current(0)

L5=Label(top,text="Email",fg="white",bg="purple",font=("Arial 20 bold"))
L5.place(x=100,y=350)

e5=Entry(top,font=("Arial 20 bold"))
e5.place(x=290,y=350)


L6=Label(top,text="Password",fg="white",bg="purple",font=("Arial 20 bold"))
L6.place(x=100,y=400)

e6=Entry(top,font=("Arial 20 bold"),show="*")
e6.place(x=290,y=400)

l7=Label(top,text='Date',fg="white",bg="purple",font=("Arial 20 bold"))
l7.place(x=100,y=450)


cal = DateEntry(top,width=19,bg="Dark blue",fg='white',year=2010,font=("Arial 20 bold"))
cal.place(x=290,y=450)

c1=Checkbutton(top,font=("Arial 15 bold"),command=showpassword)
c1.place(x=565,y=400)


b=Button(top,text='Submit',font=("Arial 20 bold"),command=Insert)
b.place(x=290,y=570)

b2=Button(top,text='Delete',font=("Arial 20 bold"),command=Delete)
b2.place(x=420,y=570)

b3=Button(top,text='Update',font=("Arial 20 bold"),command=UpdateFrom)
b3.place(x=540,y=570)

b4=Button(top,text='Search',font=("Arial 20 bold"),command=Search)
b4.place(x=670,y=570)

b5=Button(top,text='Display',font=("Arial 20 bold"))
b5.place(x=800,y=570)

b6=Button(top,text='Login',font=("Arial 20 bold"),command=login)
b6.place(x=936,y=570)

b7=Button(top,text='Show',font=("Arial 20 bold"),command=show)
b7.place(x=1050,y=570)

l8=Label(top,text='Gender',fg="white",bg="purple",font=("Arial 20 bold"))
l8.place(x=100,y=500)

r1=Radiobutton(top,text='Male',variable=var,value='Male',font=("Arial 17 bold"))
r1.place(x=290,y=500)

r2=Radiobutton(top,text='FeMale',value='Female',variable=var,font=("Arial 17 bold"))
r2.place(x=390,y=500)

r3=Radiobutton(top,text='Other',value='OTHER',variable=var,font=("Arial 17 bold"))
r3.place(x=522,y=500)

top.configure(bg="purple")
top.mainloop()
