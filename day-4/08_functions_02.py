def want_coffee(question, attempts=3, warning="Think again ☕"):
	while True:
		answer = input(question)

		if answer in {"yes", "y"}:
			print("Coffee coming right up! 😄")
			return True

		if answer in {"no", "n"}:
			print("No coffee today 😴")
			return False

		attempts -= 1

		if attempts < 0:
			raise ValueError("Too confused to decide about coffee!")

		print(warning)

# want_coffee("Do you want coffee? (yes/no): ")
want_coffee("Final chance! Coffee? ", warning="Last warning 😤", attempts=2)
