#Exercise 10.3 - Guest
guests=input("Please enter your name: ")
guest='guest.txt'
with open(guest, 'w') as file_object:
	file_object.write(guests)

#Exercise 10.4 - Guest Book
guest='guest.txt'
while True:
	name=input("Please enter your name: ")
	print("Hello "+name.title()+"!")
	if name == 'q':
		break
		print("Thank you for participating!")
with open(guest, 'a') as file_object:
	file_object.write(guests)

#Exercise 10.5
