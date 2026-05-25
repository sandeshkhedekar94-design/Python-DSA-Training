'''

Class is a logical representation of things.
It is like a blueprint or template for the object.
Object is the physical representation of class and representation of things.


To initialize class variable we use Constructor.
    def __init__ (self):
        print("default constructor ")

    def show(self):
        print(" I am in show")
'''

class Student:
    def __init__(self):
        print("default constructor ")
    def __init__(self,a):
        print(a)

    def show(self):
        print("I am in showA")

s = Student()
s.show()