prices = [100, 250, 400]

prices_with_gst = list(map(lambda x: x + (x * 0.18), prices))
print(prices_with_gst)
print(prices)

# Lambda doing tax calculation faster than humans!