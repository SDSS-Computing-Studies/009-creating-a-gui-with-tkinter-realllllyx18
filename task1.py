import tkinter as tk 
from tkinter import *

window = tk.Tk()
window.title("tk")

lable1 = tk.lable(window,text="x")
lable2 = tk.lable(window,text="=")

label1.grid(row = 1, column = 1)
label2.grid(row = 1, column = 1)

window.mainloop()