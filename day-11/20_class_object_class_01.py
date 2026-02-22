''' Let's check a normal 'Object' '''
x = 10
print(type(x))

''' Let's check a 'Class Object' '''
class Beverages:
	def __init__(self, name, temperature, caffeine):
		self.name = name
		self.temperature = temperature
		self.caffeine = caffeine

	def describe(self):
		return f"{self.name} is served {self.temperature} and has {self.caffeine} caffeine. ☕"

	def sip(self):
		return f"You take a refreshing sip of {self.name}!"

# Example
tea = Beverages("Tea", "hot", "low")
juice = Beverages("Orange Juice", "cold", "none")

print(tea.describe())
print(juice.sip())

# Main Focus
print(type(Beverages))

'''
Summary
instance → created by class
class → created by type
'''