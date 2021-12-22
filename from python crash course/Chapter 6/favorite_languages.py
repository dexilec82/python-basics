#A Dictionary of Similar Objects
favorite_languages = {
    'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
print("Sarah's favorite language is "+
favorite_languages['sarah'].title()+
".")


#Looping through key-value pairs
print("\n")
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
for name,language in favorite_languages.items():
	print(name.title()+"'s favorite language is "+
	language.title()+".")
print("\n")
for name in favorite_languages.keys():
	print(name.title())


#Looping through all the keys in a dictionary
print("\n")
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil':'python',
	}
friends=['phil','sarah']
for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		print("Hi "+name.title()+
		", I see your favorite language is " + 
		favorite_languages[name].title()+"!")
	
if 'erin' not in favorite_languages.keys():
	print("\nErin, please take our poll")



#Looping through a dictionary's keys in order
print("\n")
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil':'python',
	}
for name in sorted(favorite_languages.keys()):
	print(name.title()+", thank you for taking the poll.")


#Looping through all values in a dictionary
print("\n")
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil':'python',
	}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())
print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())
	

#List in a dictionary
print("\n")
favorite_languages = {
	'jen': ['python','ruby'],
	'sarah': ['c'],
	'edward': ['ruby','go'],
	'phil':['python','haskell'],
	}
for name, languages in favorite_languages.items():
	print("\n"+name.title()+"'s favorite languages are:")
	for language in languages:
		print("\t"+language.title())

