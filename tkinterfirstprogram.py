import tkinter as tk
root=tk.Tk()
root.geometry("600x400")
name_var=tk.StringVar()
passw_var=tk.StringVar()
def submit():
    name=name_var.get()
    password=passw_var.get()
    print("The name is:"=name)
    print("The password is:"=password)
    name_var.set("")
    passw_var.set("")
name_label = tk.Label(root, text='username', font=("arial",10,"bold"))
name_entry = tk.Entry(root,textvariable=name_var,font=("arial",10,"normal"))
passw_label = tk.Label(root,text='password',font=("arial",10,"bold"))
passw_entry = tk.Entry(root,textvariable=passw_var,font=("arial",10,"normal"))
sub_btn=tk.Button(root,text="submit",command=submit)
