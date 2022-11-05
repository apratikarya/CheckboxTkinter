from tkinter import *
from tkinter import messagebox
root = Tk()

root.geometry("300x300")

messagebox.showinfo("Info", "Saved Successfully")
messagebox.showerror("OOPs something went wrong", "Error")
messagebox.showwarning("Warning", "Warning")

mainloop()
