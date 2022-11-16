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

# to get values from collection
def HandleGet():
    database = client["student"]
    col = database["student_info"]
    data=col.find()
    for i in data:
        print(i)

# to delete values from
def HandleDelete():
    database = client["student"]
    col = database["student_info"]
    col.delete_one({'name':'Kiran'})
    print("Deleted Sucessfully...")

def HandleUpdate():
    database = client["student"]
    col = database["student_info"]
    col.update_one({'name':'Karan'},{'$set':{'name':'Zyz'}})

l = Label(root, text="Enter Name")
l.grid(row=0, column=1)
e1 = Entry(root)
e1.grid(row=0, column=2)
b1 = Button(root, text="Submit", command=HandleInsert)
b1.grid(row=1, column=2)
b2 = Button(root, text="Get", command=HandleGet)
b2.grid(row=2, column=2)
b3 = Button(root, text="Delete", command=HandleDelete)
b3.grid(row=3, column=2)
b4 = Button(root, text="Update", command=HandleUpdate)
b4.grid(row=4, column=2)

root.mainloop()
