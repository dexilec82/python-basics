#Exercise 5.1
car='subaru'
print("Is car=='subaru'? I predict True.")
print(car=='subaru')

print("\nIs car=='audi'?I predict False.")
print(car=='audi')

#Exercise 5.2
motorcycles=['honda','kawasaki','ducati','harley-davidson']
for motorcycle in motorcycles:
	if motorcycle=='ducati':
		print(motorcycle.title())
	else:
		print(motorcycle.upper())
if motorcycles!='honda':
	print("No that is not a motorcycle brand!")
	
requested_motorcycle='agusta'
if requested_motorcycle!='honda':
	print("Hold it, that is not what we have!")
if requested_motorcycle=='agusta':
	print("Open the gates for Agusta!")

print("\n")
answer=17
if answer!=41:
	print("That is not the correct answer. Please try again!")

answer=100
if answer<101:
	print("Study next time!")
if answer>99:
	print("Good Job!")
if answer>=100:
	print("Perfect!")


food=['burger','fries','coke']
order='nuggets'
if order not in food:
	print("No this is not available to order. Please select another food")
if order in food:
	print("How many piece of nuggets would you like to order?")

