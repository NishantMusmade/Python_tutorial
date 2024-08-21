import math

print('Square root of 4: ',math.sqrt(4))
print('Floor value of 4.3765: ',math.floor(4.3765))

print('\nFunctions and pakages in math module: ')
print(dir(math))

#from keyword
from math import sqrt

print('\nSquare root of 4: ',sqrt(4))    #here can directlt write sqrt()


#importing everything
from math import *
print('\nsin(90): ', sin(90))

#importing module which is some user-written program
import import_practice as ip
print('\nList in import_practice program: ',ip.mylist)

from import_practice import welcome, mylist
print('\nExecuting welcome() function of import_practice program: ',end = '')
welcome()
print('\nList in import_practice program: ',mylist)
