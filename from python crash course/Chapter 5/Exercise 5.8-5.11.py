#Exercise 5.8
usernames=['admin','carlo','user','terminator','qwerty123']
for username in usernames:
	if username == 'admin':
		print("Hello admin, would you like to see a status report?")
	else:
		print("Hello "+username.title()+", thank you for logging in again")

#Exercise 5.9
print("\n")
usernames=[]
if usernames:
	for username in usernames:
		print("Hello, thank you for logging in")
else:
		print("We need to find some users!")


#Exercise 5.10
print("\n")
current_users=['admin','carlo','user','terminator','qwerty123']
new_users=['admin','cedric','users','terminator','qwas12']
for new_user in new_users:
	if new_user in current_users:
		print("Sorry but your username is already taken. Please create another one.")
else:
	print("Thank you for logging in.")
print("\nHave a nice day!")


#Exercise 5.11
print("\n")
ordinal_numbers=[1,2,3,4,5,6,7,8,9]
for ordinal_number in ordinal_numbers:
	if ordinal_number==1:
		ordinal='1st'
		print("Your ordinal number is "+str(ordinal)+"!")
	elif ordinal_number==2:
		ordinal='2nd'
		print("Your ordinal number is "+str(ordinal)+"!")
	elif ordinal_number==3:
		ordinal='3rd'
		print("Your ordinal number is "+str(ordinal)+"!")
	elif ordinal_number==4:
		ordinal='th'
		print("Your ordinal number is "+str(ordinal)+"!")
		



