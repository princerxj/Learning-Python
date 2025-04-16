# Constructors - All classes have a function called _init_(), which is always executed when the class is being initiated

# creating class
class Student:
    college = "ABC college"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


# creating object
s1 = Student("Prince", 98)
print(s1.name, s1.marks)

s2 = Student("Arjun", 92)
print(s2.name, s2.marks)

print(Student.college)
print(s1.college)
print(s2.college)
# The self param is a refernce to the current instance of the class and is used to access variables that belongs to the class
# Class and Instance Attribites
# class.attr, obj.attr
