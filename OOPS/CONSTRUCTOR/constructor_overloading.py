class Std:
    def __init__(self,name="",age="",depart=""):
        self.name = name
        self.age = age
        self.depart = depart
    def display(self):
        print(self.name,self.age,self.depart)

s1 = Std("ram")
s2 = Std("ram",20)
s3 = Std("ram",20,"cse")
s1.display()
Std.display(s2)
s3.display()







