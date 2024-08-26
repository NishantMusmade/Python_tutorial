#implementation of filter function
# filter(predicate,iterable)
# predicate argument is a function that returns a boolean value and applied to each element of the iterable, and the iterable can be list,tuple or any other iterable object

mylist = [1,2,3,4,5]

filter_l = list(filter(lambda x : x>2,mylist))

print('\nList after applying filter: ',filter_l)


#filtering out perfect square
from math import sqrt
num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]

def isPerfechSquare(x):
    return sqrt(x).is_integer()

perfect_squares = list(filter(isPerfechSquare,num_list))

print('\nList of perfect squares: ',perfect_squares)