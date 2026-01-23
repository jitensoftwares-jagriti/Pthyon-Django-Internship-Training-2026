'''
input() always returns string
Conversion avoids logical errors
'''

# num1 = int(input("Enter number: "))
# num2 = int(input("Enter number: "))
# print(num1 + num2)

x = 10 # integer -> 10.0
y = 45 #. float
z = x + y

print("The sum of", x, "and", y, "is", z)
print("The type of z is", type(z))