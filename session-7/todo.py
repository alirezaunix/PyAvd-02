from tkinter import *
from tkinter import messagebox

windowform=Tk()
windowform.title("TO-Do List")


tasks=[]

def add_task():
    task=entry_task.get()
    if task:
        tasks.append(task)
        update_task_list()
        entry_task.delete(0,END)
        messagebox.showinfo("Information",f"\'{task}\' added")
        
def remove_task():
    selected_task=listbox_task.curselection()
    if selected_task:
        tasks.pop(selected_task[0])
        update_task_list()

def clear_task():
    tasks.clear()
    update_task_list()


def update_task_list():
    listbox_task.delete(0,END)
    for task in tasks:
        listbox_task.insert(END,task)


IMAGE_SIZE=15
FONT_SIZE=24
entry_task=Entry(windowform,width=25)
entry_task.grid(row=0,column=0,columnspan=3)

photo_add = PhotoImage(
    file="/Users/alireza/Desktop/pyadv-02/session-7/images/add.png").subsample(IMAGE_SIZE, IMAGE_SIZE)

btn_add = Button(windowform, image=photo_add, font=(
    "", FONT_SIZE, ""), command=add_task)
btn_add.grid(row=1,column=0)

photo_remove = PhotoImage(
    file="/Users/alireza/Desktop/pyadv-02/session-7/images/remove.png").subsample(IMAGE_SIZE, IMAGE_SIZE)
btn_remove = Button(windowform, image=photo_remove, font=(
    "", FONT_SIZE, ""),command=remove_task)
btn_remove.grid(row=1, column=1)

photo_clear = PhotoImage(
    file="/Users/alireza/Desktop/pyadv-02/session-7/images/clear.png").subsample(IMAGE_SIZE, IMAGE_SIZE)
btn_clear = Button(windowform, image=photo_clear, font=(
    "", FONT_SIZE, ""), command=clear_task)
btn_clear.grid(row=1, column=2)

listbox_task = Listbox(windowform, font=(
    "", FONT_SIZE, ""),width=30, height=15)
listbox_task.grid(row=2, column=0,columnspan=3)

mainloop()