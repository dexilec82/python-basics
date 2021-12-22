#Dictionary

alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

print("\n")
alien_0={'color':'green','points':5}
new_point=(alien_0['points'])
print("You just earned "+str(new_point)+" points!")

#Adding Key-Value Pair
print("\n")
alien_0={'color':'green','points':5}
print(alien_0)
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

print("\n")
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

print("\n")
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

#Modifying Values in a Dictionary
print("\n")
alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print("Original x_position: " +str(alien_0['x_position']))

#Move the alien to the right
#Determine how far to move the alien based on its current speed.

if alien_0['speed']=='slow':
	x_increment=1
elif alien_0['speed']=='medium':
	x_increment=2
else:
	#this must be a fast alien
	x_increment=3
#The new position is the old position plus the increment.
alien_0['x_position']=alien_0['x_position']+x_increment
print("New x_position: "+str(alien_0['x_position']))


#Removing Key-Value Pairs
print("\n")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)


#A Dictionary of Similar Objects
favorite_languages = {
    'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
	
#Nesting
print("\n")
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)
print("\n")

#Nesting fleet of aliens
#Make an empty list for storing aliens

aliens=[]

#Make 30 green aliens
for alien_number in range(30):
	new_alien = {'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)

#Show the first 5 aliens.
for alien in aliens[:5]:
	print(alien)
print("...")

#Show how many aliens have been created
print("Total number of aliens: " +str(len(aliens)))
print("\n")

#Change the first three aliens to yellow, medium speed aliens worth 10 points each

aliens=[]
for alien_number in range(0,30):
	new_alien = {'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15
		
#Show me the first five aliens
for alien in aliens[0:5]:
	print(alien)
print("...")
print("Total number of aliens: " +str(len(aliens)))
print("\n")





