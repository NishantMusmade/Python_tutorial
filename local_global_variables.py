x = 5 #global variable

def my_function():
    x = 10 # local variable
    print(f'The local variable is {x}')

print(f'The golbal variable is {x}')
my_function()

#if you declare a variable inside a fucntion body i.e., local variable, then it will destroy after the end of the function or return of the function
#consider x = 5 as golabl variable
print('\nUisng local variable outside the function')

def my_function():
    y = 10 # local variable
    print(f'The local variable is {x}')

print(f'The golbal variable is {x}')
# print(y)  #this line will throw error as y is not defined because y is a local variable and can be used only inside the fucntion

#changing the value of global,variable inside a function
print('\nChanging value of global variable inside a function')
def my_function():
    global x
    x = 10 # this line will change the value of golbal variable x as 10 which was 5 earlier

my_function()
print(f'The global variable is {x}')

#Usually it is not a good practice to modify global varaibles from within functions, as it can lead to unexpected bhevaiour and harder to debug the code 



