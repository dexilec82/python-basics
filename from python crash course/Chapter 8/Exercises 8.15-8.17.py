#Exercise 8.15
from printing_functions import *
unprinted_designs = ['tokyo tower', 'optimus prime', 'octahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#Exercise 8.16
#Import module name
print("\n")
import sandwich
sandwich.make_sandwich('tuna')
sandwich.make_sandwich('cheese', 'egg', 'mayonaisse')
sandwich.make_sandwich('club','bacon')

#from module_name import function_name
print("\n")
from sandwich import make_sandwich
make_sandwich('tuna')
make_sandwich('cheese', 'egg', 'mayonaisse')
make_sandwich('club','bacon')

#from module_name import function_name as fn
print("\n")
from sandwich import make_sandwich as ms
ms('tuna')
ms('cheese', 'egg', 'mayonaisse')
ms('club','bacon')

#import module_name as mn
print("\n")
import sandwich as s
s.make_sandwich('tuna')
s.make_sandwich('cheese', 'egg', 'mayonaisse')
s.make_sandwich('club','bacon')

#from module_name import *
from sandwich import *
make_sandwich('tuna')
make_sandwich('cheese', 'egg', 'mayonaisse')
make_sandwich('club','bacon')


#Exercise 8.17




