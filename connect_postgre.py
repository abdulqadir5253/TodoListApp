import psycopg2
import tkinter as tk
from tkinter import *

conn = psycopg2.connect("dbname=todo user =postgres password=5152 host=localhost")

cur = conn.cursor()

def insert():
    roo_new.deiconify()
    roo_new.bind('<Return>', getValues)

def getValues(event):
    task = roo_new.taskEntry.get()
    time = roo_new.taskTime.get()
    print(task)
    print(type(task))
    print(type(time))
    cur.execute("insert into list values (%s, %s)", (roo_new.taskEntry.get()
        , roo_new.taskTime.get()))
    conn.commit()
    roo_new.withdraw()

def deleted():

    print()

def shows():
    showAllRecord()


def showAllRecord():
    cur.execute("Select * from list")
    rows = cur.fetchall()
    wind = tk.Tk()

    for index, dat in enumerate(rows):
        Label(wind, text=dat[0]).grid(row=index + 4, column=0)
        Label(wind, text=dat[1]).grid(row=index + 5, column=1)
        Label(wind, text=dat[2]).grid(row=index + 6, column=2)


def updated():
    cur.close()
    conn.close()
    print()

def createWidget():
    add = tk.Button(root, text="Add Task"
                    , command=insert)
    add.grid(row=1, column=1, padx=5, pady=15)

    delete = tk.Button(root, text="Delete Task"
                       , command=deleted)
    delete.grid(row=1, column=5, padx=55, pady=15)

    update = tk.Button(root, text="Update Task"
                       , command=updated)
    update.grid(row=1, column=6, padx=75, pady=15)

    show = tk.Button(root, text="show all tasks",command=shows)
    show.grid(row=3, column=1)

    task = tk.Label(roo_new, text="Task: ")
    task.grid(row=0, column=1)

    time = tk.Label(roo_new, text="Time of Task")
    time.grid(row=2, column=1)

    roo_new.taskEntry = Entry(roo_new, width=50,
                             font=60)
    roo_new.taskEntry.grid(row=0, column=5)
    roo_new.taskEntry.focus()

    roo_new.taskTime = Entry(roo_new, width=10
                             , font=40)
    roo_new.taskTime.grid(row=2, column=5, padx=30, pady=30)
    roo_new.taskTime.focus()




root = tk.Tk()
roo_new = tk.Tk()
roo_new.withdraw()
root.geometry('400x400')
createWidget()
root.mainloop()