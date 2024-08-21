#The basic distinction between creating a function with def and a lambda expression, besides syntactic sugar, is that lambda does so without assigning to a name; 
# in fact, the other common name for a lambda is an anonymous function
def square(x):
    return x*x

print('Squaring the value using a regular function: ')
print('Sqaure of 5 is: ',square(5))

print('Cubing the value using a lambda function: ')
cube = lambda x: x*x*x

print('Cube of 5 is: ',cube(5))   #OR  print('Cube of 5 is: ',lambda x: x*x*x)


#passing multiple arguments to a lambda function
addition = lambda x,y,z: x+y+z
print('\nPassing multiple arguments: ')
print('Addition of 3 numbers x,y, and z is: ',addition(3,6,5))


#lambda function is oftenly used to pass the function as a parameter

def add_6(fx,value):
    return 6 + fx(value)

result = add_6(cube,3)
print('\nPassing a lambda function as an argument: ')
print("Ater apply add_6 function on cube, we get: ",result)

