#The while loop in action
current_number=1
while current_number<=5:
	print(current_number)
	current_number+=1


#Using continue in a Loop
print("\n")
current_number=0
while current_number<=10:
	current_number+=1
	if current_number%2==0:
		continue
	print(current_number)


#Infinite loop example
#x = 1
#while x <= 5:
#	print(x)


#Avoiding Infinite Loops
