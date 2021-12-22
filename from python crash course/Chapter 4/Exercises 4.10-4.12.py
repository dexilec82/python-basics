#Exercise 4.10
my_foods=['pizza','burger','fried chicken','french fries','nuggets']
print("The first three items in the list are:")
print(my_foods[:3])
print("\nThree items from the middle of the list are:")
print(my_foods[1:4])
print("n\The last three items in the list are:")
print(my_foods[2:])

#Exercise 4.11
print("\n")
pizzas=['new york','meat buster','4 cheese','pepperoni']
friend_pizzas=pizzas[:]
print("My Pizzas are:")
print(pizzas)
print("\nMy Friend Pizzas are:")
friend_pizzas.append('hawaiian')
print(friend_pizzas)

print("\n")
pizzas=['new york','meat buster','4 cheese','pepperoni']
friend_pizzas=pizzas[:]
friend_pizzas.append('hawaiian')
for my_pizzas in pizzas:
	print("My Pizzas are:")
	print(my_pizzas)
	print("\n")
for friend_pizza in friend_pizzas:
	print("My Friend Pizzas are:")
	print(friend_pizza)

#Exercise 4.12
print("\n")
my_foods=['pizza','falafel','carrot cake','cannoli']
friend_foods=my_foods[:]
my_foods.append('fried chicken')
for my_food in my_foods:
	print("My Foods are:")
	print(my_food)
for friend_food in friend_foods:
	print("My friend foods are:")
	print(friend_food)

