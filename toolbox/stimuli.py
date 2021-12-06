import time
import os
from tkinter import Tk,Canvas,PhotoImage
import random
import pandas as pd
# time in seconds, make sure time in record.py matches this
colors_list = ["red", "yellow", "green"]

df = pd.read_csv(r'C:\Users\Tushar\Desktop\ProfessorX\sequence.csv')
# change the location of the csv file as per system
markers = df["Sequence"].to_numpy()
# imports the binary values from sequence.csv into a list named markers

def display_left():
    color_of_frame = random.choice(colors_list)
    root = Tk()
    root.geometry("+100+200")
    canvas = Canvas(root, width=300, height=300)
    canvas.pack()
    canvas.create_rectangle(0, 0, 300, 300, fill=color_of_frame)
    canvas.create_line(75, 150, 225, 150, fill="black", width=10)
    canvas.create_line(75, 150, 150, 100, fill="black", width=10)
    canvas.create_line(75, 150, 150, 200, fill="black", width=10)
    root.after(1000, lambda: root.destroy())
    root.mainloop()

def display_right():
    color_of_frame = random.choice(colors_list)
    root = Tk()
    root.geometry("+1100+200")
    canvas = Canvas(root, width = 300, height = 300)
    canvas.pack()
    canvas.create_rectangle(0,0,300,300,fill=color_of_frame)
    canvas.create_line(75,150,225,150,fill="black",width=10)
    canvas.create_line(225,150,150,100,fill="black",width=10)
    canvas.create_line(225,150,150,200,fill="black",width=10)
    root.after(1000,lambda:root.destroy())
    root.mainloop()

for i in markers:
    if i==0:
        display_left()
    else:
        display_right()
