#Using json.dump() and json.load()
import json
filename = 'numbers.json'
with open(filename) as f_obj:
	numbers = json.load(f_obj)
print(numbers)

