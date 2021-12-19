import pandas as pd

colors_list = ["red", "yellow", "green"]

df = pd.read_csv(r"C:/Users/KHALS/OneDrive/Desktop/professorX/toolbox/sequence.csv")
# change the location of the csv file as per system
markers = df["Sequence"].to_numpy()
# imports the binary values from sequence.csv into a list named markers

