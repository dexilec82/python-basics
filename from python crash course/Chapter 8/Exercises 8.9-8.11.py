#Exercise 8.9
def show_magician(name):
	"""Display magicians name."""
	print("\nThe following are magicians names:")
	print(name.title())
show_magician('carlo')

print("\n")
#Exercise 8.10
def show_magician(name,title):
	"""Display magicians name."""
	while name:
		new_name = name.pop()
		# Simulate creating a new name.
		print("Creating new name: " + new_name)
		title.append("The Great "+new_name.title())
def make_great(title):
	"""Display magicians new name."""
	print("\nThe following are magicians name:")
	for new_magician in title:
		print(new_magician)
name = ['carlo', 'cedric', 'yoko']
title = []
show_magician(name, title)
make_great(title)
print(name)
print(title)

print("\n")
#Exercise 8.11
def show_magician(name,title):
	"""Display magicians name."""
	while name:
		new_name = name.pop()
		# Simulate creating a new name.
		print("Creating new name: " + new_name)
		title.append("The Great "+new_name.title())
def make_great(title):
	"""Display magicians new name."""
	print("\nThe following are magicians name:")
	for new_magician in title:
		print(new_magician)
name = ['carlo', 'cedric', 'yoko']
title = []
show_magician(name[:], title)
make_great(title)
print(name)
print(title)

