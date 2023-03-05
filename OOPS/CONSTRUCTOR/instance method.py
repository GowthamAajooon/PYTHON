class std:
    def __init__(f,name,age):
        f.name = name
        f.age = age
    def display(self,gender):
        return self.name+" "+str(self.age)+" "+gender

d = std("ram",20)
print(d.display("male"))
print(std.display(d,"male"))
