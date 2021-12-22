#Exercise 9.4
class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
		self.number_served=0
	def describe_restaurant(self):
		print(self.restaurant_name.title()+" is offering "+self.cuisine_type.title()+" cuisine.")
	def open_restaurant(self):
		print(self.restaurant_name.title()+" is now open!")
	def set_number_served(self):
		print("This restaurant has served " + str(self.number_served) + " customers.")
	def increment_odometer(self, customers):
		self.number_served += customers
restaurant=Restaurant('nirvana','indian')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served()
restaurant.increment_odometer(1)
restaurant.set_number_served()

#Exercise 9.5
print("\n")
class User():
	def __init__(self,pangalan,apelyido,titulo,lokasyon):
		self.first_name = pangalan
		self.last_name = apelyido
		self.profession = titulo
		self.location = lokasyon
		self.login_attempts = 0
	def describe_user(self):
		print("\nFirst Name: " +self.first_name.title())
		print("Last Name: " +self.last_name.title())
		print("Profession: " +self.profession.title())
		print("Location: " +self.location.title())
	def greet_user(self):
		print("\nWelcome "+self.first_name.title()+" "+self.last_name.title()+"!")
	def number_of_logins(self):
		print("You have " + str(self.login_attempts) + " login attempts.")
	def update_login(self,login):
		self.login_attempts = login
	def increment_login_attempts(self,logins):
		self.login_attempts += logins
user=User('carlo','torres','engineer','tokyo')
print(user.describe_user())
user.update_login(2)
user.number_of_logins()
user.increment_login_attempts(1)
user.number_of_logins()
