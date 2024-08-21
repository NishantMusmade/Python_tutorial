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

print('List of cubes: ', cube_l)

#---------------------------------------------------------------------------------------------------------------------------------------------------------

#implementation of filter function

filter_l = list(filter(lambda x : x>2,mylist))

print('List after applying filter: ',filter_l)