import os
from tkinter import Tk,Canvas,PhotoImage
from PIL import Image, ImageTk

root = Tk()
root.geometry("+200+200")

canvas = Canvas(root, width = 300, height = 300)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("left.png"))  
canvas.create_image(20,20, anchor='nw', image=img) 


os.system("python C:/Users/KHALS/OneDrive/Desktop/professorX/record.py")
root.mainloop()



