# WAP to Display Message on label

from tkinter import *

root = Tk()

root.geometry("500x500")

text_label = Label(root, text="This is just a text showing\nUsing the label...")
text_label.pack()


root.mainloop()