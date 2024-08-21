print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice: "))

print("\nEnter numbers below")
x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))

match choice:
    case 1:
        print("Addition of two numbers is : ",x+y)
    case 2:
        print("Subtraction of two numbers is : ",x-y)
    case 3:
        print("Multiplication of two numbers is : ",x*y)
    case 4:
        print("Division of two numbers is : ",x/y)
    case _:
        print("Invalid choice...!")