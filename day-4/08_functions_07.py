def order_pizza(customer_name, *toppings):
    print("Order for:", customer_name)

    if not toppings:
        print("Plain pizza 😐")
    else:
        print("Toppings added:")
        for item in toppings:
            print("-", item)

order_pizza("Rahul")
order_pizza("Priya", "Cheese", "Olives", "Jalapenos")
