#Exercise 11.1
#def get_formatted_name(city, country):
#	"""Generate a neatly formatted location name."""
#	location_name = city + ',' + country
#	return location_name.title()

def get_formatted_name(city, country, population=''):
	"""Generate a neatly formatted location name."""
	if population:
		location_name = city + ',' + country + ',' + population
	else:
		location_name = city + ',' + country
	return location_name.title()
