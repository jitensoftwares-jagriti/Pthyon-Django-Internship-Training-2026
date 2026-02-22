class Student:
    def __init__(self, name):
        self.name = name

    # Method inside the class
    def greet(self):
        print("Hello, my name is", self.name)


# Creating an object
s = Student("Rahul")
Student.__name__

# Calling a method using the object
s.greet()
