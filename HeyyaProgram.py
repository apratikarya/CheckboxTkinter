from tkinter import *

# create a tkinter window
root = Tk()

# Open a window having dimesion 100x100
root.geometry('1000x100')

# Create a button
btn = Button(root, text='Click me !', bd='5',
             command=root.destroy)

# Set th position of button on the top of window.
btn.pack(side='top')

root.mainloop()