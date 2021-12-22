#Conditional statements. Inequality.
requested_topping='mushrooms'
if requested_topping!='anchovies':
	print("Hold the anchovies!")
if requested_topping=='mushrooms':
	print("Move the mushrooms!")

#Conditional IF statements without elif and else
print("\n")
requested_topping=['mushrooms','extra cheese']
if 'mushrooms' in requested_topping:
	print("Adding mushrooms.")
if 'pepperoni' in requested_topping:
	print("Adding pepperoni.")
if 'extra cheese' in requested_topping:
	print("Adding extra cheese.")
print("\nFinished making your Pizza!")

#Checking for Special Items
print("\n")
requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
	print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

print("\n")
requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")


#Checking for empty list
print("\n")
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")


#Using Multiple Lists
print("\n")
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

















