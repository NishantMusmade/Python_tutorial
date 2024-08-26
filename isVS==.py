#comparison between is and == operator

#1. is operator
#   'is' operator is known as identity operator
#   When the variables at either side of the operator point at the exact same object(in memory), the is operator evaluates it as true. Otherwise, it will evaluate as False.
#   Python identity operators (is, is not) are used to compare objects based on their identity

#2. == operator
#   '==' operator is known as equality operator
#   When the variables at either side of the operator has exact same value, the == operator evaluates it as True. Otherwise, it will evaluate as false
#   To compare objects based on their values

print('Checking for constant value assignment: ')
a = 10
b = 10

print('a==b: ',a==b)
print('a is b: ',a is b)
#lets check identity of a and b
print('\nIdentity of a: ',id(a))
print('Identity of b: ',id(b))
#both will be same hence 'a is b' returns True


#lets check for string, remember that string is immuatable
print('\nChecking for strings: ')
str_1 = 'Hello'
str_2 = 'Hello'

print()
print('str_1 == str_2: ',str_1==str_2)
print('str_1 is str_2: ',str_1 is str_2)



#lets check for list, remember that lists are mutable
print('\nChecking for list: ')
list_1 = [1,2,3]
list_2 = [1,2,3]
list_3 = list_1   

print()
print('list_1 == list_2: ',list_1 == list_2)
print('list_1 is list_2: ', list_1 is list_2)
#checking identity of list_1 and list_2
print('\nIdentity of list_1: ',id(list_1))
print('Identity of list_2: ',id(list_2))
#both will be different and hence 'list_1 is list_2' return False


#list_1 and list_3 are pointing to the same object in memory, so both == and is operator will evaluate it as True
print()
print('list_1 == list_3: ',list_1 == list_3)
print('list_1 is list_3: ', list_1 is list_3)
#checking identity of list_1 and list_3
print('\nIdentity of list_1: ',id(list_1))
print('Identity of list_3: ',id(list_3))


#if we use slicing, then list_1 and list_3 will not point to same object even though they may have same values
list_3 = list_1[:]
print('\nResults after slicing: ')
#list_1 and list_3 are pointing to the different object in memory
print()
print('list_1 == list_3: ',list_1 == list_3)
print('list_1 is list_3: ', list_1 is list_3)
#checking identity of list_1 and list_3
print('\nIdentity of list_1: ',id(list_1))
print('Identity of list_3: ',id(list_3))
#as list_1 and list_3 with same values are pointing to different object in memory, is will evaluate it as False


#checking for tuple
print('\nChecking for tuple: ')
tuple_1 = (1,2,3)
tuple_2 = (1,2,3)
tuple_3 = tuple_1   

print()
print('tuple_1 == tuple_2: ',tuple_1 == tuple_2)
print('tuple_1 is tuple_2: ', tuple_1 is tuple_2)
#checking identity of tuple_1 and tuple_2
print('\nIdentity of tuple_1: ',id(tuple_1))
print('Identity of tuple_2: ',id(tuple_2))
#both will be same as tuple_1 and tuple_2 are pointing to same obejct hence is will return True


#tuple_1 and tuple_3 are pointing to the same object in memory, so both == and is operator will evaluate it as True
print()
print('tuple_1 == tuple_3: ',tuple_1 == tuple_3)
print('tuple_1 is tuple_3: ', tuple_1 is tuple_3)
#checking identity of tuple_1 and tuple_3
print('\nIdentity of tuple_1: ',id(tuple_1))
print('Identity of tuple_3: ',id(tuple_3))


#even if we use slicing, then also tuple_1 and tuple_3 will point to same object in memory
tuple_3 = tuple_1[:]
print('\nResults after slicing: ')
#tuple_1 and tuple_3 are pointing to the same object in memory
print()
print('tuple_1 == tuple_3: ',tuple_1 == tuple_3)
print('tuple_1 is tuple_3: ', tuple_1 is tuple_3)
#checking identity of tuple_1 and tuple_3
print('\nIdentity of tuple_1: ',id(tuple_1))
print('Identity of tuple_3: ',id(tuple_3))
#as tuple_1 and tuple_3 are pointing to same object in memory, it will evaluate it as False


#Note that the objects that are immutable point to the same object in memory if they have same values, otherwise they point to different object in memory





