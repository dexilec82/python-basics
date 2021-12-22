#Exercise 7.1
rental=input("What kind of rental car do you like? ")
print("\nLet me see if I can get you a "+rental+".")

#Exercise 7.2
reservation=input("How many people are in your dinner group? ")
reservation=int(reservation)
if reservation>=10:
	print("\nWe are sorry but please wait for your table.")
else:
	print("\nThank you for waiting, your table is ready.")

