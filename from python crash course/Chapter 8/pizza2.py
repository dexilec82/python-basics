#This is a sample module we will use for the "Importing an Entire Module" example
def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make."""
	print("\nMaking a " + str(size) +
		"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)
