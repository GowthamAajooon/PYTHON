class Student:
    
    def __init__(self,*args):
        if len(args)==0:
            self.name="Ram"
            self.age=23
        elif len(args)==1:
            self.name = args[0]
        elif len(args)==2:
            self.name = args[0]
            self.age = args[1]
        elif len(args)==3:
            self.name=args[0]
            self.age = args[1]
            self.marks = args[2]

s0 = Student()
print(s0.name,s0.age)

s1 = Student("velu")
print(s1.name)

s2 = Student("sham",23)
print(s2.name,s2.age)

s3 = Students("Deva",18,98)
print(s3.name,s3.age,s3.marks)
