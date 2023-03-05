class Std:
    def __init__(self):
        self.age = 20
    def dis(s):
        print("The age is ",s.age)
class Teach(Std):
    def __init__(self):
        self.age = 40
    def dis(s):
        print("The age is",s.age)

s1 = Std()
s2 = Teach()

s2 = s1
s2.dis()
