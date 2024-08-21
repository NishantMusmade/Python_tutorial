elements = [10,11.2,"Nishant",True,'a']

print(type(elements))
print("The above list contains: ",end=' ')
print(elements)

print()
print(elements[0])
print(elements[1])
print(elements[2])
print(elements[3])
print(elements[4])

#another list

numbers = [1,2,3,4,5,6,7,8,9]
print(numbers[:])
print(numbers[:6])
print(numbers[3:])
print(numbers[0:9:2])


#list comprehension
print("\nCreating and printing list using list comprehension: ",end=' ')
mylist = [i for i in range(6)]

print(mylist)

even_num = [i for i in range(20) if i%2==0]

print("\nThe even numbers list is: ",even_num)

#using expression
num_squares = [i*i for i in range(1,11)]
print("\nSqaures of numbers: ",num_squares)