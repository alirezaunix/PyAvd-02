class Person:
    def __init__(self,igender,ifname,ilname,iage):
        self.gender=igender
        self.fname=ifname
        self.lname=ilname
        self.age=iage
    
    def show_info(self):
        print(f"{'Male' if self.gender  else 'Female'} {self.fname} {self.lname}")
    
    def abalities(self,):
        pass
    
p1=Person(True,"Alireza","Kiani",40)
p1.show_info()

p2=Person(False,"Zahra","Gholi",20)
p2.show_info()