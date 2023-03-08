STATIC METHODS

class A:
    @staticmethod
    def a_method(a):
        print(a)
A.a_method(9) # Output: "a"


CLASS METHODS

class A:
    @classmethod
    def a_method(cls,a):
        return a
print(A.a_method(9))  # Output: "a"


INSTANCE METHOD

class A:
    def s(a):
        print(a)
A.s(2)
