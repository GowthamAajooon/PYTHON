class Std:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        #G.dis = G.name+" is "+str(G.age)+" years old "
    @property
    def d(self):
        return self.name+" is "+str(self.age)+" years old "
        
g= Std("Ram",20)
print(g.d)
g.age=40
print(g.d)
