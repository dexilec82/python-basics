#Exercise 8.3
def make_shirt(size,message):
	"""Accepts a t-shirt size and the message printed on the t-shirt"""
	print("\nThe size of the t-shirt is "+size.title()+".")
	print("The message printed is "+message.upper()+".")
make_shirt('large','yolo')
make_shirt(size='large',message='yolo')


#Exercise 8.4
def make_shirt(message,size='large'):
	"""Accepts a t-shirt size and the message printed on the t-shirt"""
	print("\nThe size of the t-shirt is "+size.title()+".")
	print("The message printed is "+message.title()+".")
make_shirt('I love python')
make_shirt(size='medium',message='I hate python')


#Exercise 8.5
print("\n")
def describe_city(city,country='Philippines'):
	print(city.title()+" is in the "+country.title()+".")
describe_city('manila')
describe_city(city='pasig')
describe_city(country='Japan',city='tokyo')

