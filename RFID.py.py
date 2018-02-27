from tkinter import *
import MySQLdb



root = Tk()

root.title("RFID scanning panel")

e1 = Entry(root,width=50)

e1.grid(row=0)


def close(self):
   # db = MySQLdb.connect(host="localhost", user="root", passwd="", db="test")
    db = MySQLdb.connect("Your Server Name", "Username", "", "Password")
    #cursor = db.cursor()
    cur = db.cursor()
    arg = e1.get()
    e1.delete(0,END)
    cur.execute("INSERT INTO tbl_user(name) VALUES('%s')" % arg)
    db.commit()


b1 = Button(root, text="Enter", fg="white", bg="blue", command=close)
root.bind('<Return>', close)
b1.grid(row=1)

root.mainloop()