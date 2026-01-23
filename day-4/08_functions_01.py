# write Fibonacci series less than n
def fib(n):
	"""Print a Fibonacci series less than n."""
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print()

# Now call the function we just defined:
print(fib.__doc__)
fib(2000)