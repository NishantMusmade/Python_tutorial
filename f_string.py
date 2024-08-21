#traditional approach
name = 'Nishant'
college = 'Vishwakarma University'
text = 'I am {} and I am from {}'

print("Printing string with traditional approach...")
print(text.format(name, college))
print()
text = 'I am {1} and I am from {0}'
print(text.format(college,name))
print()


#Using f-string
print("Using f-string...")
print(f"I am {name} and I am from {college}"+"\n")

num = 24.48999
print(f"The given number is {num:.2f}")
print(f"The given number is {num:.3f}")

#printing number as string
print("\nPrinting number as string...")
print(type(2+2))   #type will be int
print(type(f"2+2"))  #type will be str


#printing string as it is
print("\nPrinting string as it is...")
print(f"I am {{name}} and I am from {{college}}")


