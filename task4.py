import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Example")
window.geometry("315x135")

dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)
p = tk.Label(window, text = "Pochacco!")

label2 = tk.Label(window, text = "           A cuddly little puppy! This is from the same creators \n   who brought you Keropi and Kero Kero", bg = "#87ceeb")

label1.place(x=80,y=0)
p.place(x=160, y=30)
label2.place(x=0, y=100)

window.mainloop()
