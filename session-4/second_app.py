from tkinter import *
mainform = Tk()
mainform.title("پنجره")
# mainform.resizable(0, 0)
mainform.configure(bg="red")
COLOR_1 = "#0000ff"
text1 = Text(mainform, height=10, width=10)
text1.pack()

btn1 = Button(mainform, text="FirstName")
btn1.pack()

btn2 = Button(mainform, text="OK", fg="orange", bg="green")
btn2.pack()

entry1 = Entry(mainform, width=10, font=("", 20, ""))
entry1.config(bg=COLOR_1, fg="#000010")
entry1.pack()

btn3 = Button(mainform, text="Cancel", command=mainform.destroy)
btn3.pack()

mainloop()
