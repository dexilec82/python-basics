#Exercise 6.7

people = {
	'brother':{
		'first_name':'cedric',
		'last_name':'torres',
		'age':21,
		'city':'canaman'
		},
	'father':{
		'first_name':'leon',
		'last_name':'torres',
		'age':59,'city':'pamplona'
		},
	'cousin':{
		'first_name':'philip',
		'last_name':'torres',
		'age':35,'city':'arizona'
		},
	}
for relationship,information in people.items():
	print("\nRelationship: "+relationship.title())
	full_name=information['first_name']+" "+information['last_name']
	age=information['age']
	location=information['city']
	print("\tFull Name: "+full_name.title())
	print("\tAge: "+str(age))
	print("\tLocation: "+location.title())
	

#Exercise 6.8
pets = {
	'dog':{
		'breed':'labrador',
		'color':'black',
		'name':'bruno',
		},
	'cat':{
		'breed':'persian',
		'color':'gray',
		'name':'juno',
		},
	'fish':{
		'breed':'goldfish',
		'color':'red',
		'name':'nemo',
		},
	}
for pet,info in pets.items():
	print("\nPet: "+pet.title())
	name=info['name']
	breed=info['breed']
	color=info['color']
	print("\tName: "+name.title())
	print("\tBreed: "+breed.title())
	print("\tColor: "+color.title())


#Exercise 6.9
favorite_places = {
	'philip':'arizona',
	'carlo':'japan',
	'emelyn':'uae',
	}
for name,place in favorite_places.items():
	print("\n"+name.title()+"'s"+ " favorite place is "+place.title()+".")


#Exercise 6.10
print("\n")
favourite_numbers={
	'carlo': [7,8],
	'hiraki': [69,13],
	'marty':[0,1],
	'amit': [56,65],
	'joonpyo': [9000,100],
	}
for name,numbers in favourite_numbers.items():
	print("\n"+name.title()+"'s favorite numbers are:")
	for number in numbers:
		print("\t"+str(numbers))


#Exercise 6.11
cities = {
	'manila':{
		'country':'philippines',
		'population':100,
		'fact':'dds',
		},
	'paris':{
		'country':'france',
		'population':1,
		'fact':'napoleon',
		},
	'tokyo':{
		'country':'japan',
		'population':1000000,
		'fact':'japanese',
		},
	}
for city,info in cities.items():
	print("\nCity: "+city.title())
	County=info['country']
	Consensus=info['population']
	Detail=info['fact']
	print("Country: "+County.title())
	print("Population: "+str(Consensus))
	print("Fact: "+Detail.upper())
	

