#Exercise 8.12
def make_sandwich(*filling):
	"""Print the type of sandwich a person wants."""
	print(filling)
make_sandwich('tuna')
make_sandwich('cheese', 'egg', 'mayonaisse')
make_sandwich('club','bacon')

#Exercise 8.13
def build_profile(first, last, **user_info):
	"""Build a dictionary containing information about yourself."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
user_profile = build_profile('carlo', 'torres',
					location='japan',
					profession='engineer')
print(user_profile)

#Exercise 8.14
def make_car(manufacturer,model,**optional_feature):
	"""Store a car information in a dictionary"""
	cars = {}
	cars['manufacturer'] = manufacturer
	cars['model'] = model
	for key, value in optional_feature.items():
		cars[key] = value
	return cars
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
car = make_car('toyota', 'vios', color='gold', tow_package=False)
print(car)
