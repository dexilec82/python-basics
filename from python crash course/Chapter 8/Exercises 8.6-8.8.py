#Exercise 8.6
def city_country(city,country):
	"""This function returns formatted city and country"""
	place='"'+city+", "+country+'"'
	return(place.title())
places=city_country('tokyo','japan')
print(places)

#Exercise 8.7
def make_album(artist,album,tracks=''):
	"""This function builds a dictionary"""
	album={'singer':artist,'title':album}
	if tracks:
		album['tracks'] = tracks
	return album
record=make_album('marilyn manson','the pale emperor')
record1=make_album('iron maiden','the best')
record2=make_album('bruce dickinson','chemical wedding','2')
print(record)
print(record1)
print(record2)

#Exercise 8.8
print("\n")
def make_album(artist,album,tracks=''):
	"""This function builds a dictionary"""
	album={'singer':artist,'title':album}
	return album
while True:
	print("\nPlease enter the artist's name:")
	print("(enter 'q' at any time to quit)")
	artist=input("Artist Name: ")
	if artist=='q':
		break
	album=input("Album Title: ")
	if album=='q':
		break
	record=make_album(artist,album)	
	print(record)
