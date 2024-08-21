#taking user input

#First way
print('First way to take input')
name = input()
print('My name is',name)
print()

#Second way
print("Second way to take input")
name = input('Enter your name: ' )
print('My name is ',name)
print()

#Taking number as input in string and then type-casting it
print("Taking number as input in string form")
x = input('Enter first number : ')
y = input('Enter second number : ')

print('Addition of ',x,'and',y,'is',int(x)+int(y))
print()

#Directlytaking input in integer form
print('Taking input in integer form instead of string')
x = int(input('Enter first number : '))
y = int(input('Enter second number : '))

print('Addition of ',x,'and',y,'is',x+y)

