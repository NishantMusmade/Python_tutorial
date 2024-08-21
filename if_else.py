#Implementation of if-else statement
print("Implementation of if-else statement")
#checking if the number is odd or even

number = int(input("Enter a number: "))

if number%2 == 0:
    print("It is an even number")
else:
    print("It is an odd number")

print()
#Implementation of if-elif-else statement
print("Implementation of if-elif-else statement")

#Checking grade based on marks obtained
marks = int(input("Enter your marks: "))

if marks>=90:
    print("You got A+ grade")
elif marks>=80:
    print("You got A grade")
elif marks>=70:
    print("You got B+ grade")
elif marks>=60:
    print("You got B grade")
elif marks>=50:
    print("You got C grade")
else:
    print("You are fail")

#Implementation of nested if_else
print("\nImplementation of nested if-else")

age = int(input("Enter your age: "))

if age>= 18:
    driving_license = input("Do you have driving license(Y if yes, N if no): ")
    if driving_license == 'Y':
        print("You can drive")
    else:
        print("You cannot drive")
else:
    print("You cannot drive")



