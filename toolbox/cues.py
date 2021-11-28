import time
import os
from tkinter import Tk,Canvas,PhotoImage
from PIL import Image, ImageTk
# time in seconds, make sure time in record.py matches this
time_period = 3

def display_left():
    root = Tk()
    root.geometry("+200+200")
    canvas = Canvas(root, width = 300, height = 300)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open("left.png"))  
    canvas.create_image(20,20, anchor='nw', image=img)
    root.after(3000,lambda:root.destroy())
    #os.system("python C:/Users/KHALS/OneDrive/Desktop/professorX/record.py")
    root.mainloop()

display_left()


time.sleep(time_period)

def display_right():
    root = Tk()
    root.geometry("+1000+200")
    canvas = Canvas(root, width = 300, height = 300)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open("right.png"))  
    canvas.create_image(20,20, anchor='nw', image=img) 
    #os.system("python C:/Users/KHALS/OneDrive/Desktop/professorX/record.py")
    root.after(3000,lambda:root.destroy())
    root.mainloop()

display_right()

time.sleep(time_period)




