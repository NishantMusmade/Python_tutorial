#enter the input other than valid literal(for e.g. alphabets)
num = input("Enter a number: ")

try:
    for i in range(1,11):
        print(f'{num} * {i} = {int(num)*i}' )
except Exception as e:
    print(e)

print('Program end')

#another way to write except
num = input("\nEnter a number: ")
try:
    for i in range(1,11):
        print(f'{num} * {i} = {int(num)*i}' )
except:
    print("Invalid Input...!")

print('Program end')

#we can also except particular error and use multiple except
num = input("\nEnter a number: ")
try:
    for i in range(1,11):
        print(f'{num} * {i} = {int(num)*i}' )
except ValueError:
    print("Value error occured...!")
except IndexError:
    print('Index error occured...!')
else:
    print("Some error occured...!")


#if we use empty except, it will catch all exceptions including system exit which we want to be passed
#so to solve this from python 3.0, Exception has been introduced as shown below

num = input("\nEnter a number: ")
try:
    for i in range(1,11):
        print(f'{num} * {i} = {int(num)*i}' )
except Exception:       #this will catch all exceptions except system exit
    print("Value error occured...!")



