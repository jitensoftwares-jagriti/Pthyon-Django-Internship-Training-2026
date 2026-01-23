def greet(name, *, role):
    print(name, role)

greet(name="Aman", role="admin")
# valid function call

greet("Aman", "admin")
# Error
# in-valid function call