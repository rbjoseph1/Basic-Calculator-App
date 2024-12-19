from customtkinter import *
import tkinter as tk

# setup
app = CTk()
app.geometry("300x350")
set_default_color_theme("green")

entry = CTkEntry(master = app, font = CTkFont(size = 30, weight = "bold"))
entry.place(relx = 0.5, rely = 0.05, anchor = "nw")

# creating the buttons
def button_7():
    entry.insert(tk.END, "7")

btn7 = CTkButton(master = app, text = "7", height = 50, width = 50, corner_radius = 25, command = button_7)
btn7.place(relx = 0.05, rely = 0.2, anchor = "nw")

def button_8():
    current = entry.get()
    entry.insert(tk.END, "8")

btn8 = CTkButton(master = app, text = "8", height = 50, width = 50, corner_radius = 25, command = button_8)
btn8.place(relx = 0.38, rely = 0.2, anchor = "n")

def button_9():
    entry.insert(tk.END, "9")

btn9 = CTkButton(master = app, text = "9", height = 50, width = 50, corner_radius = 25, command = button_9)
btn9.place(relx = 0.62, rely = 0.2, anchor = "n")

def multiply():
    entry.insert(tk.END, "*")

btnmult = CTkButton(master = app, text = "x", height = 50, width = 50, corner_radius = 25, command = multiply)
btnmult.place(relx = 0.95, rely = 0.2, anchor = "ne")

def button_4():
    entry.insert(tk.END, "4")

btn4 = CTkButton(master = app, text = "4", height = 50, width = 50, corner_radius = 25, command = button_4)
btn4.place(relx = 0.05, rely = 0.4, anchor = "nw")

def button_5():
    entry.insert(tk.END, "5")

btn5 = CTkButton(master = app, text = "5", height = 50, width = 50, corner_radius = 25, command = button_5)
btn5.place(relx = 0.38, rely = 0.4, anchor = "n")

def button_6():
    entry.insert(tk.END, "6")
btn6 = CTkButton(master = app, text = "6", height = 50, width = 50, corner_radius = 25, command = button_6)
btn6.place(relx = 0.62, rely = 0.4, anchor = "n")

def divide():
    entry.insert(tk.END, "/")
btndiv = CTkButton(master = app, text = "/", height = 50, width = 50, corner_radius = 25, command = divide)
btndiv.place(relx = 0.85, rely = 0.4, anchor = "n")

def button_1():
    entry.insert(tk.END, "1")
btn1 = CTkButton(master = app, text = "1", height = 50, width = 50, corner_radius = 25, command = button_1)
btn1.place(relx = 0.05, rely = 0.6, anchor = "nw")

def button_2():
    entry.insert(tk.END, "2")
btn2 = CTkButton(master = app, text = "2", height = 50, width = 50, corner_radius = 25, command = button_2)
btn2.place(relx = 0.38, rely = 0.6, anchor = "n")

def button_3():
    entry.insert(tk.END, "3")
btn3 = CTkButton(master = app, text = "3", height = 50, width = 50, corner_radius = 25, command = button_3)
btn3.place(relx = 0.62, rely = 0.6, anchor = "n")

def add():
    entry.insert(tk.END, "+")
btnplus = CTkButton(master = app, text = "+", height = 50, width = 50, corner_radius = 25, command = add)
btnplus.place(relx = 0.95, rely = 0.6, anchor = "ne")

def button_0():
    entry.insert(tk.END, "0")
btn0 = CTkButton(master = app, text = "0", height = 50, width = 50, corner_radius = 25, command = button_0)
btn0.place(relx = 0.05, rely = 0.8, anchor = "nw")

def clear():
    entry.delete(0, tk.END)
btnC = CTkButton(master = app, text = "C", height = 50, width = 50, corner_radius = 25, command = clear)
btnC.place(relx = 0.38, rely = 0.8, anchor = "n")

# calculate function
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END)
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error.")
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error.")

btneq = CTkButton(master = app, text = "=", height = 50, width = 50, corner_radius = 25, command = calculate)
btneq.place(relx = 0.62, rely = 0.8, anchor = "n")

def subtract():
    entry.insert(tk.END, "-")
btnminus = CTkButton(master = app, text = "-", height = 50, width = 50, corner_radius = 25, command = subtract)
btnminus.place(relx = 0.95, rely = 0.8, anchor = "ne")

app.mainloop()

