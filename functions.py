def addition(a,b):
    print("Addition of provided numbers is: ",a+b)

#just defining function without body
def issmaller(a,b):
    pass

#returning value from the function
def average(a,b):
    average = (a+b)/2
    return average

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

addition(num1,num2)
average = average(num1,num2)

print("The average of two numbers is: ",average)





