class Student:
	def __init__(self, name, age):
		# Instance variables
		self.name = name
		self.age = age

	def profile(self, name, age):
		pass


# Creating objects with different data
s1 = Student("Amit", 21)
s2 = Student("Riya", 22)

# Accessing object attributes
print(s1.name, s1.age)
print(s2.name, s2.age)
