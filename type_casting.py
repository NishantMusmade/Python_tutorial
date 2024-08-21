#Type-casting in python
#Two types
# 1] Explicit type-casting: Done manually using buit-in conversion functions like int(),float(),hex(), etc
# 2] Implicit type-casting : Python interpreter does it automatically, it converts lower data type into higher data type to avoid data loss(for example- converts int to float)


#Explicit type-casting

print('Exaple of explicit type-casting')

a = '1'
b = '2'

print('Without type-casting: a+b =',a+b)
print('Using type-casting: a+b =',int(a)+int(b))
print()

#Implicit type-casting

print('Example of implicit type-casting')

a = 1.9
b = 5

print(a,'+',b,'=',a+b)
print()

#checking type of the result
c = a+b
print('Type of "c" variable is ',type(c))