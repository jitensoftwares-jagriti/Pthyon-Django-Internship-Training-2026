x = "Global X"  # Global namespace


def outer():
    x = "Enclosing X"  # Enclosing namespace

    def inner():
        x = "Local X"   # Local namespace
        print(x)

    inner()


outer()

# len = "Something"

# Built-in Lookup
print(len("Hello"))

# Python namespace look-up rule
# LEGB
# L - Local
# E - Enclosing
# G - Global
# B - Built-in