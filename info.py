
import tkinter as tk
win=tk.Tk()
label1=tk.Label(win,text="Welcome To Library",font="30",)
label1.pack()
photo=tk.PhotoImage(file="img.gif")
label=tk.Label(image=photo)
label.pack()
def a():
    win.destroy()
    import login.py

button=tk.Button(win,text="Register",fg="purple",bg="yellow",activebackground="pink",font="bold",command=a)
button.pack()
win.mainloop()
