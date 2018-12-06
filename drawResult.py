"""  
-------------------------------------------------------  
gui.py
[program description]
-------------------------------------------------------  
Author:  Brian Hane 
ID:      150571750  
Email:   hane1750@mylaurier.ca 
_updated_ ="2018-12-05"
-------------------------------------------------------  
"""
from tkinter import *
import tkinter


class frame_grid(Frame):
    def __init__(self, arr, y, x):
        root = tkinter.Tk()
        resultArr = arr
        self.c = Canvas(root, height=(y * 20),
                        width=(x * 20), bg='white')
        self.draw_grid(resultArr, x, y)
        self.c.pack(fill=BOTH, expand=True)

        root.mainloop()

    def draw_grid(self, resultArr, x, y):

        for y in range(0, y - 1):
            for x in range(0, x - 1):
                temp = resultArr[y][x]
                # switch (resultArr[x][y]){
                if temp == 0:
                    self.c.create_rectangle(
                        x * 10, y * 10, x * 10 + 10, y * 10 + 10, fill="white")

                elif temp == 1:
                    self.c.create_rectangle(
                        x * 10, y * 10, x * 10 + 10, y * 10 + 10, fill="black")  # wall

                elif temp == 2:
                    self.c.create_rectangle(
                        x * 10, y * 10, x * 10 + 10, y * 10 + 10, fill="orange")  # frontier

                elif temp == 3:
                    self.c.create_rectangle(
                        x * 10, y * 10, x * 10 + 10, y * 10 + 10, fill="red")  # explored

                elif temp == 4:
                    self.c.create_rectangle(
                        x * 10, y * 10, x * 10 + 10, y * 10 + 10, fill="blue")  # start position

                elif temp == 5:
                    self.c.create_rectangle(
                        x * 10, y * 10, x * 10 + 10, y * 10 + 10, fill="green")  # end position

                elif temp == 6:
                    self.c.create_rectangle(
                        x * 10, y * 10, x * 10 + 10, y * 10 + 10, fill="purple")  # path taken
