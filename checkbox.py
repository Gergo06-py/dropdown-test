from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Sliders")
root.iconbitmap("C:/Users/borbe/Pictures/code.ico")
root.geometry("400x400")

var = StringVar()
var.set("On")

def show():
    label = Label(root, text=var.get()).pack()


checkbox = Checkbutton(root, text="check this box ;D", variable=var, onvalue="On", offvalue="Off")
checkbox.pack()


button = Button(root, text="checked?", command=show).pack()

mainloop()
