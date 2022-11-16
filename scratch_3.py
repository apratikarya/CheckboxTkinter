from pymongo import MongoClient
from tkinter import *

root = Tk()
root.geometry("300x300")
client = MongoClient("localhost", 27017)


# insert
def HandleInsert():
    # db
    database = client["student"]
    # collection
    col = database["student_info"]
    name = e1.get()
    col.insert_one({'name': name})
    e1.delete(0, END)
    print("Date successfully inserted...")


l = Label(root, text="Enter Name")
l.grid(row=0, column=1)
e1 = Entry(root)
e1.grid(row=0, column=2)
b1 = Button(root, text="Submit", command=HandleInsert)
b1.grid(row=1, column=2)

root.mainloop()
