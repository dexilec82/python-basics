#Exercise 7.8
sandwich_orders=['club','tuna','egg','cheese']
finish_sandwiches=[]
while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print("I made your "+sandwich.title()+" sandwich.")
	finish_sandwiches.append(sandwich)
print("\nThe following sandwiches have been made:")
for finish_sandwich in finish_sandwiches:
	print(finish_sandwich.title())



#Exercise 7.9
sandwich_orders=['pastrami','club','tuna','pastrami','egg','cheese','pastrami']
print("\nThe deli has run out of pastrami!")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
print(sandwich_orders)

print("\n")
sandwich_orders=['pastrami','club','tuna','pastrami','egg','cheese','pastrami']
finish_sandwiches=[]
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print("I made your "+sandwich.title()+" sandwich.")
	finish_sandwiches.append(sandwich)
print("\nThe deli has run out of pastrami!")
print("The following sandwiches have been made:")
for finish_sandwich in finish_sandwiches:
	print(finish_sandwich.title())


#Exercise 7.10
responses = {}
polling_active = True
while polling_active:
	name = input("\nWhat is your name? ")
	response = input("If you could visit one place in the world, where would you go? ")
	responses[name] = response
	repeat = input("Would you like to let another person respond? (yes/ no) ")
	if repeat == 'no':
		polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(name + " would like to visit " + response + ".")
print(responses)









