def add(a,b):
    '''This function is taking two numbers as an argument
    and prints the addition of two numbers'''     #doctring
    print(a+b)

print(add.__doc__)
add(4,5)
print()


#if the docstring is not written right after the definition
def add(a,b):
    print("Here docstrings is not used right after the definition so it is showing 'None'")
    '''This function takes a number as an argument and printins its square'''  #doctrinfg
    print(a+b)

print(add.__doc__)
add(4,5)

#accesing doctring using help() function
print("\nAccessing doctstring using help() function")

def square(n):
    '''This function takes a number as an argument and prints its square'''
    print(n*n)

help(square)
square(5)