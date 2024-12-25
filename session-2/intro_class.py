class Person:
    
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def print_info(self):
        print(f"Your name is {self.fname} and your lastname is {self.lname} and your age is {self.age}")


p1=Person("Alireza","Kiani",40)
p1.print_info()
