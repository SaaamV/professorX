from tkinter import Tk,Canvas,PhotoImage
import random
import time
import numpy as np
import pandas as pd




class Toolbox():

    def __init__(self):
        self.colors_list = ["red", "yellow", "green"]

    def random_gen(self, n):
        # n is the total number of elements
        k = int(n/2)
        # k is the number of zeros
        arr = np.array([0]*k + [1]*(n-k))
        np.random.shuffle(arr)
        df = pd.DataFrame(arr, columns=['Sequence'])
        df.to_csv('sequence.csv')

    def stimuli(self,period,buffer):
        # before running for the first time make sure you call random_gen() once.
        df = pd.read_csv(r"sequence.csv")
        markers = df["Sequence"].to_numpy()
        # imports the binary values from sequence.csv into a list named markers

        for i in markers:
            if i==0:
                self.display_left(period)
                time.sleep(buffer)
            else:
                self.display_right(period)
                time.sleep(buffer)
        
    
    #def plot(self):

        



    def display_left(self, time):
        color_of_frame = random.choice(self.colors_list)
        root = Tk()
        root.geometry("+100+200")
        canvas = Canvas(root, width=300, height=300)
        canvas.pack()
        canvas.create_rectangle(0, 0, 300, 300, fill=color_of_frame)
        canvas.create_line(75, 150, 225, 150, fill="black", width=10)
        canvas.create_line(75, 150, 150, 100, fill="black", width=10)
        canvas.create_line(75, 150, 150, 200, fill="black", width=10)
        root.after(time, lambda: root.destroy())
        root.mainloop()

    def display_right(self, time):
        color_of_frame = random.choice(self.colors_list)
        root = Tk()
        root.geometry("+1100+200")
        canvas = Canvas(root, width = 300, height = 300)
        canvas.pack()
        canvas.create_rectangle(0,0,300,300,fill=color_of_frame)
        canvas.create_line(75,150,225,150,fill="black",width=10)
        canvas.create_line(225,150,150,100,fill="black",width=10)
        canvas.create_line(225,150,150,200,fill="black",width=10)
        root.after(time,lambda:root.destroy())
        root.mainloop()


