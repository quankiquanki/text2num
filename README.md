text2num
===============

This is a function that converts textual numbers in a string to their integer representation.

Example:
===============
'''
from text2num import text2num

in_string = "I have seventeen cars, three hundred twenty seven servants, five thousand houses and two million and twenty three hundred dollars."
out_string = text2num(in_string)

print out_string

Output:
I have 17 cars, 327 servants, 5000 houses and 2002300 dollars.
'''