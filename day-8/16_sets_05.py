a = set('abracadabra')
b = set('alacazam')

# unique letters in a
print(a, b)

print(a - b) # difference
# letters in a but not in b
print(a | b) # union
# letters in a or b or both
print(a & b) # intersection
# letters in both a and b
print(a ^ b) # symmetric difference
# letters in a or b but not both