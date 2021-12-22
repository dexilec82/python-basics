#Exercise 9.6 - Ice Cream Stand
class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
	def describe_restaurant(self):
		print(self.restaurant_name.title()+" is offering "+self.cuisine_type.title()+" cuisine.")
	def open_restaurant(self):
		print(self.restaurant_name.title()+" is now open!")
class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
	def flavor_type(self,flavor):
		self.flavor=flavor
		print("The ice cream flavor in this restaurant is "+self.flavor+"!")
IceCreamStand = IceCreamStand('nirvana','indian')
print(IceCreamStand.describe_restaurant())
IceCreamStand.flavor_type('biryani')

#Exercise 9.7 - Admin
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
class Admin(User):
	def __init__(self, pangalan,apelyido,titulo,lokasyon):
		super().__init__(pangalan,apelyido,titulo,lokasyon)
	def show_privileges(self,privileges):
		self.privileges=privileges
		print("\nThis user can do the following:")
		print("Can Add Post: "+self.privileges)
		print("Can Delete Post: "+self.privileges)
		print("Can Ban User: "+self.privileges)
Admin=Admin('carlo','torres','engineer','tokyo')
print(Admin.describe_user())
Admin.show_privileges('yes')


#Exercise 9.8 - Privileges
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
class Admin(User):
	def __init__(self, pangalan,apelyido,titulo,lokasyon):
		super().__init__(pangalan,apelyido,titulo,lokasyon)
	def show_privileges(self,privileges):
		self.privileges=privileges
		privileges = ['can add post','can delete post','can ban user']
		print("This user has the following privileges: "+self.privileges)
Admin=Admin('carlo','torres','engineer','tokyo')
print(Admin.describe_user())
Admin.show_privileges('yes')


#Exercise 9.10 - Battery Upgrade
print("\n")
class Car():
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print("This car has " + str(self.odometer_reading) + " miles on it.")
	def update_odometer(self, mileage):
		"""Set the odometer reading to the given value."""
		self.odometer_reading = mileage
	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles
class Battery():
	"""A simple attempt to model a battery for an electric car."""
	def __init__(self, battery_size=70):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)
	def upgrade_battery(self,size):
		if self.battery_size == 70:
			self.upgrade_battery = size
class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class."""
		"""Then initialize attributes specific to an electric car"""
		super().__init__(make, model, year)
		self.battery=Battery()
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery(20)
my_tesla.battery.get_range()


