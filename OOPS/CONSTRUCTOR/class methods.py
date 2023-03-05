class Student:
    name = "ram"
    age = 10

    def display():
        print("name :",Student.name)
        print("age:",Student.age)

Student.display()
getattr(Student,"display")()
Student.__dict__["display"]()

there are 3 ways to call methods
