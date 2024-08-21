#required arguments
print("Implementation of required arguments")
def average(a,b):
    print("Average of provided numbers is ",(a+b)/2)

average(4,5)

#default arguments
print("\nImplementation of default arguments(Part 1)")
def average(a=4, b =5):
    print("Average of provided numbers is ",(a+b)/2)

average(10,11)  #providing both arguments

print("\nImplementation of default arguments(Part 2)")
def average(a=4, b = 5):
    print("Average of provided numbers is: ",(a+b)/2)

average(10)  #providing only one argument

print("\nImplementation of default arguments(Part 3)")
def average(a=4, b = 5):
    print("Average of provided numbers is: ",(a+b)/2)

average()  #providing nothing as argument, it will use default values

#keyword arguments
print("\nImplementation of keyword arguments")
def average(a, b, c):
    print("Average of provided numbers is: ",(a+b+c)/3)

average(c=10,a=20,b=15)


#mixed arguments
print("\nImplementation of mixed arguments")
def average(a,c,b,d=10,e=13):
        print("Average of provided numbers is: ",(a+b+c+d+e)/5)

average(8,b=12,d=20,c=13)  #a=8, c=13,b=12,d=20,e=13 

#variable length arguments
print("\nImplementation of variable length arguments")
def average(*numbers):
    print(type(numbers))
    sum=0

    for i in numbers:
          sum += i
    print("Average of prvided numbers is: ",len(numbers)/2)

average(4,5,6,1,4)

average(4,3)

average(5,6, 7)
