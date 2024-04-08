# In this program we know about class and object class have some properties and functions and object is used to access the properties and functions of the clas
# Class is defined with "class" keyword


class Student:
    name="Haris"
    age=22
    def program(self):  # self keyword is used to access class properties in function
        print("It is the software engineering class and student name is: ",self.name,"and his age is: ",self.age)


std =Student()  # It is the object of class Student
std.program()