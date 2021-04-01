import tkinter as tk
import mysql.connector
from tkinter import messagebox
from mysql.connector import Error
from mysql.connector import errorcode
global name
global phone_no
global book
global issue
global return_date


def simple():
    try:
        conn=mysql.connector.connect(user='root',password='suzy',host='localhost',port=3307,database='project')
        c=conn.cursor()
        messagebox.showinfo("status","Done")
        name=stuname.get()
        print(name)
        phone_no=stuphone_no.get()
        print(phone_no)
        book=stubook.get()
        print(book)
        issue=stuissue.get()
        print(issue)
        return_date=stureturn_date.get()
        print(return_date)
       
        
        sql="insert into library(name,phone_no,book,issue,return_date) values (%s,%s,%s,%s,%s)"
        val=(name,phone_no,book,issue,return_date)
        c.execute(sql,val)
        conn.commit()
        print("inserted")
        messagebox.showinfo("status","You are Registered")
    except mysql.connector.Error as error:
        print("Failed to update record to database: ()".format(error))
def difficult():
     win.destroy()
     import student.py
win=tk.Tk()
win.title("Library Form")
win.configure(bg='#c2adb3')
tk.Label(win,text="Name : ", bg="#c2adb3",fg="purple",font="10").grid(row=0,column=0,padx=10,ipady=10,ipadx=15)
stuname=tk.Entry(win)
stuname.grid(row=0,column=1,padx=20,pady=20,ipady=10,ipadx=15)

tk.Label(win,text="Phone No : ", bg="#c2adb3",fg="purple",font="10").grid(row=3,column=0,padx=10,ipady=10,ipadx=15)
stuphone_no=tk.Entry(win)
stuphone_no.grid(row=3,column=1,padx=20,pady=20,ipady=10,ipadx=15)

tk.Label(win,text="Name of The Book : ", bg="#c2adb3",fg="purple",font="10").grid(row=4,column=0,padx=10,ipady=10,ipadx=15)
stubook=tk.Entry(win)
stubook.grid(row=4,column=1,padx=20,pady=20,ipady=10,ipadx=15)

tk.Label(win,text="Book Issue Date : ", bg="#c2adb3",fg="purple",font="10").grid(row=5,column=0,ipady=10,ipadx=15)
stuissue=tk.Entry(win)
stuissue.grid(row=5,column=1,pady=20,ipady=10,ipadx=15)

tk.Label(win,text="Book Return Date : ", bg="#c2adb3",fg="purple",font="10").grid(row=6,column=0,padx=10,ipady=10,ipadx=15)
stureturn_date=tk.Entry(win)
stureturn_date.grid(row=6,column=1,padx=20,pady=20,ipady=10,ipadx=15)



button=tk.Button(win,text="Submit",bg="#ecd3da",fg="purple",command=simple).grid(row=7,column=0,ipady=10,ipadx=15)
button=tk.Button(win,text="Back",bg="#ecd3da",fg="purple",command=difficult).grid(row=7,column=1,ipady=10,ipadx=15)
win.mainloop()
