from tkinter import *
from tkinter import messagebox


class FileIO:
    
    def __init__(self,addr):
        self.addr=addr
        
    def readIO(self):
        f1=open(self.addr,"tr")
        output=f1.read()
        f1.close()
        return output
    
    def writeIO(self,str1):
        f1=open(self.addr,"ta")
        f1.write(str1)
        f1.close()


    
class DesignMainForm:
    def __init__(self):
        self.mainform = Tk()
        self.mainform.title("Registration Form")
        self.FONT_SIZE = 30

        # 1
        label1 = Label(self.mainform, text="First name",
                       font=("", self.FONT_SIZE, ""))
        label1.grid(row=0, column=0)

        self.ent_fname = Entry(self.mainform, font=("", self.FONT_SIZE, ""))
        self.ent_fname.grid(row=0, column=1)
        self.ent_fname.config(bg="#6b5b95", fg="#a2b9bc")

        # 2
        label2 = Label(self.mainform, text="Last name",
                       font=("", self.FONT_SIZE, ""))
        label2.grid(row=1, column=0)

        self.ent_lname = Entry(self.mainform, font=("", self.FONT_SIZE, ""))
        self.ent_lname.grid(row=1, column=1)  # bg = "#6b5b95",fg ="#a2b9bc"
        self.ent_lname.config(bg="#6b5b95", fg="#a2b9bc")

        # 3
        label3 = Label(self.mainform, text="Phon number",
                       font=("", self.FONT_SIZE, ""))
        label3.grid(row=2, column=0)

        self.ent_phone = Entry(self.mainform, font=("", self.FONT_SIZE, ""))
        self.ent_phone.grid(row=2, column=1)
        self.ent_phone.config(bg="#6b5b95", fg="#a2b9bc")

        # 4
        label4 = Label(self.mainform, text="Age", font=("", self.FONT_SIZE, ""))
        label4.grid(row=3, column=0)

        self.ent_age = Entry(self.mainform, font=("", self.FONT_SIZE, ""))
        self.ent_age.config(bg="#6b5b95", fg="#a2b9bc")
        self.ent_age.grid(row=3, column=1)


        # 5
        label5 = Label(self.mainform, text="Adress", font=("", self.FONT_SIZE, ""))
        label5.grid(row=4, column=0, columnspan=2)

        self.ent_add = Entry(self.mainform, width=70, font=("", self.FONT_SIZE, ""))
        self.ent_add.config(bg="#6b5b95", fg="#a2b9bc")
        self.ent_add.grid(row=5, column=0, columnspan=2)


        # 6
        label6 = Label(self.mainform, text="Email", font=("", self.FONT_SIZE, ""))
        label6.grid(row=6, column=0, columnspan=2)

        self.ent_email = Entry(self.mainform, width=70, font=("", self.FONT_SIZE, ""))
        self.ent_email.config(bg="#6b5b95", fg="#a2b9bc")
        self.ent_email.grid(row=7, column=0, columnspan=2)

        # 7
        btn_submit = Button(self.mainform, text="Submit",
                            command=self.submit_action, font=("", self.FONT_SIZE, ""), bg="green")
        btn_submit.grid(row=8, column=0, sticky=W+E)

        btn_exit = Button(self.mainform, text="Exit",
                          command=self.mainform.destroy, font=("", self.FONT_SIZE, ""), bg="red")
        btn_exit.grid(row=8, column=1, sticky=W+E)

        btn_data = Button(self.mainform, text="Show Data",
                          command=self.new_form, font=("", self.FONT_SIZE, ""))
        btn_data.grid(row=9, column=0, columnspan=2, sticky=W+E)

        mainloop()

    def clear_form(self):
        self.ent_fname.delete(0, END)
        self.ent_lname.delete(0, END)
        self.ent_add.delete(0, END)
        self.ent_email.delete(0, END)
        self.ent_phone.delete(0, END)
        self.ent_age.delete(0, END)

    def submit_action(self):
       fobj.writeIO(
           f"{self.ent_fname.get()},{self.ent_lname.get()},{self.ent_phone.get()},{self.ent_age.get()},{self.ent_email.get()}\n")
       messagebox.showinfo("showinfo", "Data Saved")
       self.clear_form()

    def create_table(self,lines):
        for row,line in enumerate(lines):
            list1=line.split(",")
            for column,item in enumerate(list1):
                label1 = Label(self.form2, text=item, font=(
                    "", self.FONT_SIZE, ""), borderwidth=2)
                label1.grid(row=row, column=column,padx=5, pady=5)
            
            
    def new_form(self):
        self.form2 = Tk()
        self.form2.title("Data Table")
        lines = fobj.readIO().splitlines()
        print(lines)
        self.create_table(lines)

if __name__=="__main__":
    form1 = DesignMainForm()
    fobj = FileIO("/Users/alireza/Desktop/pyadv-02/session-6/data.txt")
