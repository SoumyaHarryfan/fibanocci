# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 17:26:55 2021

@author: hp
"""

from tkinter import *

root=Tk()

root.title("Fibonacci series")
root.geometry("400x400")
label_series = Label(root,text="fibonacci series:")
label_flower = Label(root)
label_spiral = Label(root)
def Fibonacci():
    num = 10
    first_no = 0 
    second_no = 1
    sum =0
    counter = 1
    while(counter<=num):
        label_series["text"]+=str(sum)+""
        counter = counter+1
        first_no = second_no
        second_no = sum
        sum = first_no+second_no
        label_flower['text']="flower is fully bloomed"
        label_spiral["text"]="spiral in the right direction are"+str(first_no)+"spiral in the left direction are"+str(second_no)
        +"total spirals are"+str(sum)
    
btn=Button(root,text="Show fibonacci series",command=Fibonacci)
    
btn.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()
root.mainloop()