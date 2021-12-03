import time
import os
from tkinter import Tk,Canvas,PhotoImage
from PIL import Image, ImageTk
# time between left and right
time_period = 10

def display_left():
    root = Tk()
    root.geometry("+200+200")
    canvas = Canvas(root, width = 300, height = 300)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open("left.png"))  
    canvas.create_image(20,20, anchor='nw', image=img)
    root.after(5000,lambda:root.destroy())
    root.mainloop()
    os.system("python C:/Users/KHALS/OneDrive/Desktop/professorX/record.py")

display_left()


time.sleep(time_period)

def display_right():
    root = Tk()
    root.geometry("+1000+200")
    canvas = Canvas(root, width = 300, height = 300)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open("right.png"))  
    canvas.create_image(20,20, anchor='nw', image=img) 
    root.after(5000,lambda:root.destroy())
    root.mainloop()
    os.system("python C:/Users/KHALS/OneDrive/Desktop/professorX/record.py")

display_right()

time.sleep(time_period)




