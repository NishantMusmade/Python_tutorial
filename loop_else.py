print('Implementation of for loop with else\n')
for i in range(5):
    print(i)
else:
    print('For loop over')

print('\nImplementation of while loop with else')
while i<5:
    print(i)
    i=i+1
else:
    print('While loop over')

#what if we use break statement in loop with else
print('\nUsing break statement in loop with else ')
for i in range(5):
    print(i)
    if i==3:
        break
else:
    print('Loop over')   #this will not execute as we break the loop

#So the else statement will only execute if the condition for a loop will not satistfy


