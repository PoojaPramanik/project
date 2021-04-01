import tkinter as tk
import mysql.connector
from tkinter import messagebox
from mysql.connector import Error
from mysql.connector import errorcode
global name
global email
global phone_no
global gender
global dob
global address
global qualification


def simple():
    try:
        conn=mysql.connector.connect(user='root',password='suzy',host='localhost',port=3307,database='project')
        c=conn.cursor()
        messagebox.showinfo("status","Done")
        name=stuname.get()
        print(name)
        email=stuemail.get()
        print(email)
        phone_no=stuphone_no.get()
        print(phone_no)
        gender=stugender.get()
        print(gender)
        dob=studob.get()
        print(dob)
        address=stuaddress.get()
        print(address)
        qualification=stuqualification.get()
        print(qualification)
        
        sql="insert into student(name,email,phone_no,gender,dob,address,qualification) values (%s,%s,%s,%s,%s,%s,%s)"
        val=(name,email,phone_no,gender,dob,address,qualification)
        c.execute(sql,val)
        conn.commit()
        print("inserted")
        messagebox.showinfo("status","You are Registered")
        win.destroy()
        import library.py
    except mysql.connector.Error as error:
        print("Failed to update record to database: ()".format(error))
def difficult():
    win.destroy()
    import login.py
win=tk.Tk()
win.title("Personal Information")
win.minsize(450,120)
win.configure(bg='#adc2bc')
tk.Label(win,text="Name : ", bg="#adc2bc",fg="blue",font="10").grid(row=0,column=1,padx=10,ipady=10,ipadx=15)
stuname=tk.Entry(win)
stuname.grid(row=0,column=2,padx=20,pady=20,ipady=10,ipadx=15)


tk.Label(win,text="Email-Id : ", bg="#adc2bc",fg="blue",font="10").grid(row=1,column=1,padx=10,ipady=10,ipadx=15)
stuemail=tk.Entry(win)
stuemail.grid(row=1,column=2,padx=20,pady=20,ipady=10,ipadx=15)


tk.Label(win,text="Phone No : ", bg="#adc2bc",fg="blue",font="10").grid(row=3,column=1,padx=10,ipady=10,ipadx=15)
stuphone_no=tk.Entry(win)
stuphone_no.grid(row=3,column=2,padx=20,pady=20,ipady=10,ipadx=15)

tk.Label(win,text="Gender : ", bg="#adc2bc",fg="blue",font="10").grid(row=4,column=1,padx=10,ipady=10,ipadx=15)
stugender=tk.Entry(win)
stugender.grid(row=4,column=2,padx=20,pady=20,ipady=10,ipadx=15)

tk.Label(win,text="DOB : ", bg="#adc2bc",fg="blue",font="10").grid(row=5,column=1,ipady=10,ipadx=15)
studob=tk.Entry(win)
studob.grid(row=5,column=2,pady=20,ipady=10,ipadx=15)

tk.Label(win,text="Address : ", bg="#adc2bc",fg="blue",font="10").grid(row=6,column=1,padx=10,ipady=10,ipadx=15)
stuaddress=tk.Entry(win)
stuaddress.grid(row=6,column=2,padx=20,pady=20,ipady=10,ipadx=15)

tk.Label(win,text="Qualification : ", bg="#adc2bc",fg="blue",font="10").grid(row=7,column=1,padx=10,ipady=10,ipadx=15)
stuqualification=tk.Entry(win)
stuqualification.grid(row=7,column=2,padx=20,pady=20,ipady=10,ipadx=15)

button=tk.Button(win,text="Submit",bg="#d3ece5",fg="blue",command=simple).grid(row=8,column=1,ipady=10,ipadx=15)
button=tk.Button(win,text="Back",bg="#d3ece5",fg="blue",command=difficult).grid(row=8,column=2,ipady=10,ipadx=15)
win.mainloop()
