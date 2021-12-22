#This file will import the module pizza2.py
import pizza2

pizza2.make_pizza(16, 'pepperoni')
pizza2.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Importing Specific Functions
from pizza2 import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Using as to Give a Function an Alias
from pizza2 import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')


#Using as to Give a Module an Alias
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


#Importing All Functions in a Module
from pizza2 import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
