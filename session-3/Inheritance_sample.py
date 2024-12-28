class Person:
    def __init__(self,name,id):
        self.Name=name
        self.ID=id
        
    def exportPersonInfo(self):
        print(f"Name: {self.Name}, ID: {self.ID}")
        
class Student(Person):
    def __init__(self,name,id,field):
        super().__init__(name,id)
        self.Filed=field
    
    def exportStudentInfo(self):
        print(f"Name: {self.Name}, ID: {self.ID}, Unit: {self.Filed}")

        


s1=Student("Ali",123,"Computer")
s1.exportPersonInfo()
s1.exportStudentInfo()

    