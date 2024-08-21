# RECURSION
# Function that calls themselves in order to loop
# It is an alternative to simple loops and iterations, though it is not simplest and most efficient 

# Implementation of recursion


# Calculating factorial of a number

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)
    
print(factorial(5))


#Explanation

#n = 5

# 5*factorial(4)
# 5*4*factorial(3)
# 5*4*3*factorial(2)
# 5*4*3*2*factorial(1)
# 5*4*3*2*1

