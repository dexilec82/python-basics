#Exercise 10.11 - Favorite Number
import json
favorite_number = input("What is your favorite number? ")
filename = 'favorite_number.json'
with open(filename, 'w') as fn_obj:
	json.dump(favorite_number, fn_obj)
	print("I know your favorite number! It is " + favorite_number + ".")

#Exercise 10.12 - Favorite Number
import json
favorite_number = input("What is your favorite number? ")
filename = 'favorite_number.json'
try:
	with open(filename) as fn_obj:
		username = json.load(fn_obj)
except FileNotFoundError:
	username = input("What is your favorite number? ")
	with open(filename, 'w') as fn_obj:
		json.dump(username, fn_obj)
		print("I know your favorite number! It is " + favorite_number + ".")
else:
	print("I remember your favorite number is, " + favorite_number + "!")


#Exercise 10.13 - Verify User
