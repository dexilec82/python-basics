#Exercise 9.1
class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
	def describe_restaurant(self):
		print(self.restaurant_name.title()+" is offering "+self.cuisine_type.title()+" cuisine.")
	def open_restaurant(self):
		print(self.restaurant_name.title()+" is now open!")
restaurant=Restaurant('nirvana','indian')
restaurant.describe_restaurant()
restaurant.open_restaurant()

#Exercise 9.2
print("\n")
restaurant=Restaurant('pinoy','filipino')
restaurant.describe_restaurant()
restaurant=Restaurant('habibi','arabic')
restaurant.describe_restaurant()
restaurant=Restaurant('butchiki','chinese')
restaurant.describe_restaurant()

#Exercise 9.3
print("\n")
class User():
	def __init__(self,pangalan,apelyido,titulo,lokasyon):
		self.first_name = pangalan
		self.last_name = apelyido
		self.profession = titulo
		self.location = lokasyon
	def describe_user(self):
		print("\nFirst Name: " +self.first_name.title())
		print("Last Name: " +self.last_name.title())
		print("Profession: " +self.profession.title())
		print("Location: " +self.location.title())
	def greet_user(self):
		print("\nWelcome "+self.first_name.title()+" "+self.last_name.title()+"!")
user=User('carlo','torres','engineer','tokyo')
user.describe_user()
user.greet_user()





