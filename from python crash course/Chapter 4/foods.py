#Copying a list
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]
print("My favorite foods are:")
print(my_foods)

print("\n"+"My friend's favorite foods are:")
print(friend_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\n")
my_foods.append('cannoli')
print("My favorite foods are:")
print(my_foods)

friend_foods.append('ice cream')
print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\n")
my_foods=['pizza','falafel','carrot cake','cannoli']
friend_foods=my_foods[:]
print("My favorite foods are:")
print(my_foods)

print("\n"+"My friend's favorite foods are:")
print(friend_foods)

#Another example
print("\n")
my_foods=['pizza','falafel','carrot cake','cannoli']
friend_foods=my_foods[:]
my_foods.append('fried chicken')
print("My favorite foods are:")
print(my_foods)

print("\n"+"My friend's favorite foods are:")
print(friend_foods)


