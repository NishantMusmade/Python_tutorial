#map,filter, and reduce are higher order functions
#the functions that operate with other functons are called higher-order functions

#implementation of map function
def cube(x):
    return x*x*x

mylist =[1,2,3,4,5]

#now if we want to make another list containing cube of all numbers in mylist, the traditional approach would be using for loop as geiven below

# cube_l = []
# for x in mylist:
#     cube_x = cube(x)
#     cube_l.append(cube_x)

# print(cube_l)

#using map function

cube_l = map(cube,mylist)  # this will return map object

# print(cube_l)
cube_l = list(map(cube,mylist))   
print('\nCubes of each element using map() function')
print('List of cubes: ', cube_l)

#In Python 2, the map() function returns a list. In Python 3, however, the function returns a map object which is a generator object. 

#how we can use map function to implement our own custom zip() function

#below is the use of built-in zip() function
mylist_num =[1,2,3,4,5]
mylist_char = ['a','b','c','d','e']


results = list(zip(mylist_num,mylist_char))
print('\nResult using built-in zip() function: ',results)

#implementation of zip() function using map() function

results = list(map(lambda x,y:(x,y),mylist_num,mylist_char))
print('\nResults using map() function',results)



