import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")

lable1 = tk.Lable(window, text = "Client database")
dogphoto = PhotoImage(file="dog.png")
label2 = tk.Label(window, image=dogphoto)
lable3 = tk.Lable(window, text = "Search by name", relief=SUNKEN)
lable4 = tk.Lable(window, text = "Name")
lable5 = tk.Lable(window, text = "Type")
lable6 = tk.Lable(window, text = "Breed")
lable7 = tk.Lable(window, text = "Owner")
lable8 = tk.Lable(window, text = "Birthdate")