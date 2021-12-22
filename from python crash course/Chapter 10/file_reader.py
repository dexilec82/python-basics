#Reading an entire file
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)

with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())

#File path from same folder inside the file_reader.py
with open('file\pi_digits.txt') as file_object:
	contents = file_object.read()
	print("\n")
	print(contents.rstrip())

#Reading line by line
print("\n")
filename = 'pi_digits.txt'
with open(filename) as file_object:
	for line in file_object:
		print(line)

print("\n")
filename = 'pi_digits.txt'
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

#Making a List of Lines from a File
filename = 'pi_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
for line in lines:
	print(line.rstrip())


