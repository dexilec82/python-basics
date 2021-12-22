#Exercise 10.6 - Addition
print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit.")
while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	try:
		answer = int(first_number) + int(second_number)
	except ValueError:
		print("Please input an integer!")
	else:
		print(answer)
		
#Exercise 10.7 - Addition Calculator

