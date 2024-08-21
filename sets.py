#Set is an unordered collection of data items, used to store multiple data items in a single variable
#Set items are unordered(doesn't maintain order), immutable and do not allow duplicate values
#You can add or remove item from set.
#WE cannot access set element through index
#usage : When we dont want to repeat any values in the list, for example: employee data gathered by multiple persons

myset = {23, 'Nishant', 34.567}
print('Simple set containing dfferent data types: ',myset)

#creating empty set

myset1={}  #This will create dictionary
print('\nType of myset1: ',type(myset1))

myset2 = set()
print('\nType of myset1: ', type(myset2))

#Accessing set items:
print('\nAccessing set items: ')

for item in myset:
    print(item)

#in set, True and 1 are considered as same value and Fale and 0 are considered as the same value
#1 will be replaced by True and 0 will be replaced by False
myset3 = {False,0,True,1}
print()
print(myset3)


