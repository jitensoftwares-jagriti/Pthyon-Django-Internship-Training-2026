friend1 = ["Rahul", "Pizza"]
friend2 = ["Rahul", "Pizza"]
friend3 = friend1

print(friend1 is friend2)   # Same data, different people ❌
print(friend1 is friend3)   # Same soul 😄
print(friend1 is not friend3)   # Opposite of same soul ❌

x = 10
y = 10
z = x
print(x is y)   # Small integers are cached by Python 😄
print(x is z)   # Same soul 😄