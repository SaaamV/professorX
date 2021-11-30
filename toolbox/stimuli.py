import time
import os
from tkinter import Tk,Canvas,PhotoImage
import random
from PIL import Image, ImageTk
# time in seconds, make sure time in record.py matches this
time_period = 3
# time period of change from left to right
direction_time_period = 5
# total time of display of one direction
color_time_period = random.choice(range(1000,4000,1000))
# total time of display of one color

def display_left():
    colors_list = ["red", "yellow", "green", "blue"]
    timeout = time.time() + direction_time_period
    for i in colors_list:
        if time.time() > timeout:
            break
        else:
            root = Tk()
            root.geometry("+100+200")
            canvas = Canvas(root, width=300, height=300)
            canvas.pack()
            canvas.create_rectangle(0, 0, 300, 300, fill=i)
            canvas.create_line(75, 150, 225, 150, fill="black", width=10)
            canvas.create_line(75, 150, 150, 100, fill="black", width=10)
            canvas.create_line(75, 150, 150, 200, fill="black", width=10)
            #os.system("python C:/Users/KHALS/OneDrive/Desktop/professorX/record.py")
            root.after(color_time_period, lambda: root.destroy())
            root.mainloop()

display_left()

time.sleep(time_period)

def display_right():
    colors_list = ["red", "yellow", "green", "blue"]
    timeout = time.time() + direction_time_period
    for i in colors_list:
        if time.time() > timeout:
            break
        else:
            root = Tk()
            root.geometry("+1100+200")
            canvas = Canvas(root, width = 300, height = 300)
            canvas.pack()
            canvas.create_rectangle(0,0,300,300,fill=i)
            canvas.create_line(75,150,225,150,fill="black",width=10)
            canvas.create_line(225,150,150,100,fill="black",width=10)
            canvas.create_line(225,150,150,200,fill="black",width=10)
            #os.system("python C:/Users/KHALS/OneDrive/Desktop/professorX/record.py")
            root.after(color_time_period,lambda:root.destroy())
            root.mainloop()

display_right()

time.sleep(time_period)
