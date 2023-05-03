# WAP to create login page

from tkinter import *

root = Tk()

root.geometry("500x500")

username = Label(root, text="Username")
username.grid(column=0, row=0)

password = Label(root, text="Password")
password.grid(column=0, row=1)

username_input = Entry(root)
username_input.grid(column=1, row=0)

password_input = Entry(root, show="*")
password_input.grid(column=1, row=1)


button = Button(root, text="Log In")
button.grid(column=0, row=2)

root.mainloop()