extras = {'extra_cheese': 50, 'home_delivery': 30}

def process_order(item, quantity=1, **options):
	available_products = {'pizza': 200, 'burger': 120, 'veg roll': 100, 'sandwich': 90, 'momos': 40}
	final_price = 0
	quantity = int(quantity)

	if quantity <= 0:
		print('Please order for at least 1 or more')

	if item in available_products:
		final_price += available_products[item] * quantity
	else:
		print(available_products)
		print('\n', 'Please select from the above available list')

	for key, value in options.items():
		if key in extras and value == 'Y':
			final_price += extras[key]
		else:
			# print(f"Requested option - {key} not found")
			continue

	print(f'Your total will be {final_price}')

requestedItem = input('What do you want to order')
requestedQuantity = input('How much?')
extraOption1 = input(f'Do you want extra cheese? (Y/N)')
extraOption2 = input(f'Do you want home delivery? (Y/N)')


process_order(requestedItem, requestedQuantity, extra_cheese=extraOption1, home_delivery=extraOption2)