#reduce function

#reduce(func,iterable,initial)
#initial is the optional values that gets placed before elements of iterable in the calculations, and serves as default if the iterableis empty
#Some constraints about reduce() function
#1. func required two arguments, first of which is first element of iterable and second is second element of iterable(if initial is not supplied)
#2. if nitial is supplied then it becomes the first argument and the first element of iterable becomes second element and so on
# reduce() function reduces iterable to a single value
 


from functools import reduce
def sum(x,y):
    return x+y

mylist = [1,2,3,4,5]

sum = reduce(sum,mylist)

print('\nSum of all elements in the list using reduc function: ',sum)

#    reduce takes the first and second elements in numbers and passes them to 
#    custom_sum respectively. custom_sum computes their sum and returns it to 
#    reduce. reduce then takes that result and applies it as the first element 
#    to custom_sum and takes the next element (third) in numbers as the second
#    element to custom_sum. It does this continuously (cumulatively) until numbers is exhausted.


#implementation using initial

sum = reduce(lambda x,y:x+y,mylist,10)
print('\nSum using initial: ',sum)