"""
Multi-line comment
used for documentation.
This program checks
whether a number is
even or odd
"""
'''
Another way to write
multi-line comments
'''

# Single-line comment: This program checks if a number is even or odd

try:
	num = int(input("Enter an integer: "))
except ValueError:
	print("That's not an integer.")
else:
	if num % 2 == 0:
		print(f"{num} is even.")
	else:
		print(f"{num} is odd.")