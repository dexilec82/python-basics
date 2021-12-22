#Exercise 7.4
toppings="\nWhat toppings would you like for your pizza? "
toppings+="\nEnter 'no' if you do not want additional toppings. "
message=""
while message!='no':
	message=input(toppings)
	if message!='no':
		print(message.title())
		print("Thank you for choosing your toppings, we will add it to your pizza.")

#Exercise 7.5
age=input("\nHow old are you? ")
age=int(age)
if age<3:
	print("\nYou have a free ticket!")
elif age<=12:
	print("\nYour ticket price is $10.")
else:
	print("Your ticket price is $15.")


#Exercise 7.6
toppings="\nWhat toppings would you like for your pizza? "
toppings+="\nEnter 'no' if you do not want additional toppings. "
active=True
while active:
	message=input(toppings)
	if message=='no':
		active=False
	else:
		print(message)


toppings="\nWhat toppings would you like for your pizza? "
toppings+="\nEnter 'no' if you do not want additional toppings. "
active=True
while True:
	topping=input(toppings)
	if topping=='no':
		break
	else:
		print("Thank you for choosing your toppings, we will add it to your pizza.")


age=input("\nHow old are you? ")
age=int(age)
active=True
while True:
	if age<3:
		print("\nYou have a free ticket!")
		break
	elif age<=12:
		print("\nYour ticket price is $10.")
		break
	else:
		print("Your ticket price is $15.")
		break
