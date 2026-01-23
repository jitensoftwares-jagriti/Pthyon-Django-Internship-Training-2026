def divide(a, b, /):
	return a / b

print(divide(10, 2))
# valid function call

print(divide(a=10, b=2))
# Error
# in-valid function call