import tkinter as tk
import mysql.connector
from tkinter import messagebox
from mysql.connector import Error
from mysql.connector import errorcode
global login
global password

def simple():
    try:
        conn=mysql.connector.connect(user='root',password='suzy',host='localhost',port=3307,database='project')
        c=conn.cursor()
        messagebox.showinfo("status","Done")
        login=stulogin.get()
        print(login)
        password=stupassword.get()
        print(password)
        
        sql="insert into login(login,password) values (%s,%s)"
        val=(login,password)
        c.execute(sql,val)
        conn.commit()
        print("inserted")
        messagebox.showinfo("status","You are Registered")
        win.destroy()
        import student.py
    except mysql.connector.Error as error:
        print("Failed to update record to database: ()".format(error))

win=tk.Tk()
win.title("Login Page")
win.configure(bg='#bdc2ad')
win.minsize(200,200)
tk.Label(win,text="Username : ", bg="red",fg="yellow").grid(row=0,column=0,padx=10)
stulogin=tk.Entry(win)
stulogin.grid(row=0,column=1,padx=20,pady=20)

tk.Label(win,text="Password : ", bg="red",fg="yellow").grid(row=1,column=0,padx=10)
stupassword=tk.Entry(win)
stupassword.grid(row=1,column=1,padx=20,pady=20)

button=tk.Button(win,text="Login",bg="#e6ecd3",fg="purple",command=simple).grid(row=8,column=1)
win.mainloop()
