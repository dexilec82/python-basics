#Exercise 6.4
glossary={
	'integer': 'number',
	'list': 'data',
	'strings': 'characters',
	'dictionary':'data',
	'variables':'values',
	'object':'data',
	'loop':'for',
	'unique':'set',
	}
for glossary, meaning in glossary.items():
	print("\nGlossary:"+glossary)
	print("Meaning:"+meaning)

#Exercise 6.5
rivers={
	'nile':'egypt',
	'ganges':'india',
	'amazon river': 'brazil',
	'yangtze': 'china',
	'pasig': 'philippines',
	}
for river,country in rivers.items():
	print("\nThe "+river.title()+" runs through "+country.title()+".")
print("\n")

rivers={
	'nile':'egypt',
	'ganges':'india',
	'amazon river': 'brazil',
	'yangtze': 'china',
	'pasig': 'philippines',
	}
print("The following rivers have been mentioned:")
for river,country in rivers.items():
	print(river.title())
print("\n")
for river,country in rivers.items():
	print(country.title())


#Exercise 6.6
print("\n")
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil':'',
	'carlo':'',
	}
friends=['jen','sarah','edward']
for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		print("Hi "+name.title()+
		", Thank you for participating in the poll")
	if name not in friends:
		print("Please take our poll")

