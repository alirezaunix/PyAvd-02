from tkinter import*
mainform = Tk()
FONT_SIZE=30

def submit_action():
    print("this Is submit button")
    print(ent_fname.get())


#1
label1 = Label(mainform, text="First name", font=("", FONT_SIZE, ""))
label1.grid(row=0, column=0)

ent_fname = Entry(mainform, font=("", FONT_SIZE, ""))
ent_fname.grid(row=0, column=1)
ent_fname.config(bg="#6b5b95", fg="#a2b9bc")

#2
label2 = Label(mainform, text="Last name",font=("", FONT_SIZE, ""))
label2.grid(row=1, column=0)

ent_lname = Entry(mainform, font=("", FONT_SIZE, ""))
ent_lname.grid(row=1, column=1)  # bg = "#6b5b95",fg ="#a2b9bc"
ent_lname.config(bg="#6b5b95", fg="#a2b9bc")

#3
label3 = Label(mainform, text="Phon number", font=("", FONT_SIZE, ""))
label3.grid(row=2, column=0)

ent_phone = Entry(mainform, font=("", FONT_SIZE, ""))
ent_phone.grid(row=2, column=1)
ent_phone.config(bg="#6b5b95", fg="#a2b9bc")

#4
label4 = Label(mainform, text="Age", font=("", FONT_SIZE, ""))
label4.grid(row=3, column=0)

ent_age = Entry(mainform, font=("", FONT_SIZE, ""))
ent_age.config(bg="#6b5b95", fg="#a2b9bc")
ent_age.grid(row=3, column=1)


#5
label5 = Label(mainform, text="Adress", font=("", FONT_SIZE, ""))
label5.grid(row=4, column=0,columnspan=2)

ent_add = Entry(mainform, width=70, font=("", FONT_SIZE, ""))
ent_add.config(bg="#6b5b95", fg="#a2b9bc")
ent_add.grid(row=5, column=0, columnspan=2)


#6
label6 = Label(mainform, text="Email", font=("", FONT_SIZE, ""))
label6.grid(row=6, column=0, columnspan=2)

ent_email = Entry(mainform, width=70, font=("", FONT_SIZE, ""))
ent_email.config(bg="#6b5b95", fg="#a2b9bc")
ent_email.grid(row=7, column=0, columnspan=2)

#7
btn_submit = Button(mainform, text="Submit",
                    command=submit_action, font=("", FONT_SIZE, ""), bg="green")
btn_submit.grid(row=8, column=0, sticky=W+E)

btn_exit = Button(mainform, text="Exit",
                  command=mainform.destroy, font=("", FONT_SIZE, ""), bg="red")
btn_exit.grid(row=8, column=1, sticky=W+E)


mainloop()

