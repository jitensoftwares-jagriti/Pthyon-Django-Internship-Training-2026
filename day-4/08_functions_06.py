def print_info(**info):
    print(info)
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Ravi", age=[1, 2, 3], message="Hello world")

# $ py 08_functions_06.py 
# name: Ravi
# age: 30