my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
index_of_m = my_tuple.index('m')
print(index_of_m) # Output: 3

# The index() method raises an error if the value is not found
try:
    my_tuple.index('z')
except ValueError as e:
    print(e) # Output: 'z' is not in tuple
