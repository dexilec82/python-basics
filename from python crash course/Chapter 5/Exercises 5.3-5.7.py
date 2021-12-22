#Exercise 5.3
alien_color=['green','yellow','red']
if 'green' in alien_color:
	print("You received 5 points!")
if 'blue' in alien_color:
	print()

#Exercise 5.4
print("\n")
alien_color=['green','yellow','red']
alien='green'
if alien in alien_color:
	point=5
	print("You received "+str(point)+" points!")
if alien not in alien_color:
	point=10
	print("You received "+str(point)+" points!")

print("\n")
alien_color=['green','yellow','red']
alien='blue'
if alien in alien_color:
	point=5
	print("You received "+str(point)+" points!")
else:
	point=10
	print("You received "+str(point)+" points!")


#Exercise 5.5
print("\n")
alien='red'
if alien=='green':
	point=5
elif alien=='yellow':
	point=10
elif alien=='red':
	point=15
print("Your earned "+str(point)+" points!")


#Exercise 5.6
print("\n")
age=38
if age<2:
	stage='baby'
elif age<=4:
	stage='toddler'
elif age<=13:
	stage='kid'
elif age<=20:
	stage='teenager'
elif age<=65:
	stage='adult'	
elif age>65:
	stage='elder'	
print("You are "+str(stage)+" in stage life.")


#Exercise 5.7
print("\n")
favorite_fruits=['kiwi','banana','persimmon']
if 'kiwi' in favorite_fruits:
	print("You really like Kiwi!")
if 'banana' in favorite_fruits:
	print("You really like Banana!")
if 'avocado' in favorite_fruits:
	print("You really like Avocado!")
if 'persimmon' in favorite_fruits:
	print("You really like persimmon!")
if 'apple' in favorite_fruits:
	print("You really like apple!")
print("\nYour favorite fruits!")


