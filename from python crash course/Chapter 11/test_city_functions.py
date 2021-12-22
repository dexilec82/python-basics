#Exercise 11.1
#Test city_functions.py
#from city_functions import get_formatted_name
#print("Enter 'q' at any time to quit.")
#while True:
#	city = input("\nPlease give me a city name: ")
#	if city == 'q':
#		break
#	country = input("Please give me the country: ")
#	if country == 'q':
#		break
#	formatted_name = get_formatted_name(city, country)
#	print(formatted_name) 


from city_functions import get_formatted_name
print("Enter 'q' at any time to quit.")
while True:
	city = input("\nPlease give me a city name: ")
	if city == 'q':
		break
	country = input("Please give me the country: ")
	if country == 'q':
		break
	population = input("Please enter the population: ")
	if population == 'q':
		break
	formatted_name = get_formatted_name(city, country, population)
	print(formatted_name) 
