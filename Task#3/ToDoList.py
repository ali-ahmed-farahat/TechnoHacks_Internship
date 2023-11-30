from tkinter import *
import tkinter as tk
from tkinter import messagebox

def AddTask(TaskList, EntryBox, listBox):
    task = EntryBox.get()
    if task:
        TaskList.append(task)
        EntryBox.delete(0, END)
        listAllTasks(root, TaskList, listBox)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def DeleteSelectedTask(TaskList, listBox):
    selected_task_index = listBox.curselection()
    if selected_task_index:
        TaskList.pop(selected_task_index[0])
        listAllTasks(root, TaskList, listBox)

def HeaderInterface(root):
    HFrame = tk.Label(root, text="To-Do List Program", bg='#76a5af', fg='white', width=250, padx=10, pady=10,
                      font='arial 20 bold')
    HFrame.place(x=100, y=0)
    HFrame.pack()

def listAllTasks(root, TaskList, listBox):
    listBox.delete(0, END)
    for task in TaskList:
        listBox.insert(END, f"{task} ")
    delete_button = Button(root, text="Delete Selected Task", font='arial 10 bold', borderwidth=2, bg='#ff7b7b',
                   padx=20, pady=10, command=lambda: DeleteSelectedTask(TaskList, listBox))
    delete_button.pack(side = BOTTOM)

def CreateInputInterface(root, TaskList, listBox):
    EntryFrame = tk.Frame(root, padx=20, pady=10, bg='#3d85c6', border=10)
    EntryBox = Entry(EntryFrame, width=250, font='arial 15 bold', borderwidth=5)
    EntryBox.pack()
    EntryFrame.pack()

    AddButton = Button(EntryFrame, text="Add Task", font='arial 10 bold', borderwidth=2, width=170, bg='#9fc5e8',
                       padx=20, pady=10, command=lambda: AddTask(TaskList, EntryBox, listBox))
    AddButton.pack()

def MyListInterface(root):
    MyList = tk.Label(root, text="All Tasks", bg='#8e7cc3', fg='white', width=200, padx=10, pady=10,
                      font='arial 20 bold')
    MyList.pack()



root = tk.Tk()
root.geometry('500x500')
root.resizable(False, False)
root.title('My ToDoList')
root.config(bg='#a2c8c8', borderwidth=2)
TaskList = []
listBox = Listbox(root, bd=3, width=200, height=200, bg="#0b5394")
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = BOTH)
listBox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = listBox.yview)
HeaderInterface(root)
CreateInputInterface(root, TaskList, listBox)
MyListInterface(root)
listAllTasks(root, TaskList, listBox)
listBox.pack(side=LEFT, fill=BOTH, padx=2)
DeleteSelectedTask(TaskList, listBox)

root.mainloop()
