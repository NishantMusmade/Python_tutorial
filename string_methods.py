#string methods
#strings are immutable, so all the methods of string don't modify the original string string instead it creates a copy of the string

str = '!!! Hello World !!!'

print('Length of string: ',len(str))

print('String in uppercase: ',str.upper())

print('String in lowercase: ',str.lower())

print('Stripping trailing exclamation mark: ',str.rstrip("!"))

print("Repalcing 'World' with 'India: ", str.replace('World','India'))

print("Splitting the string on the basis of spaces: ",str.split(' '))

#consider the following string for the next operation
str1 = 'hello world'
print("Capitalizing only the first character: ",str1.capitalize())

print('Printing string in center: ',str.center(50))
print('Length of the above string: ',len(str.center(50)))

#consider the following string for the next operation
str2 = 'Hello World, Hello India'
print('Counting number of "Hello" in the string: ',str2.count("Hello"))

print("Does the string 'str1' startswith 'hello': ",str1.startswith("hello"))
print("Does the string 'str1' startswith 'world': ",str1.startswith("world"))

print("Does the string endswith '!!!': ",str.endswith("!!!"))
print("Does the string endswith 'World': ",str.endswith("World"))

print("Checking in-between value of string by providing start and end indexes: ",str.endswith("lo",4,9))

print("Finding word 'Hello' in the string and returning index: ",str.find("Hello"))

print("Finding word 'India' in the string: ",str.find("India"))
print("As India was not in the string, it returned -1 as output")

#use index() method when you are sure about the occurence of word otherwise it will give error
print("Index of word 'World' in the strig: ",str.index('World'))

str3 = 'HelloWorld1234' #string containing alpha-numeric characters
str4 = 'HelloWorld1234 !!!' #string containing punctutation marks
str5 = 'HelloWorld' #string containing only alphabets

print("Is string 'str3' alpha-numeric: ",str3.isalnum())
print("Is string 'str4' alpha-numeric: ",str4.isalnum())
print("Is string 'str5' alpha-numeric: ",str5.isalnum())

#Note: Spaces are considered as non-alpha_numeric character

print("Is string 'str3' alpha(A-Z,a-z): ",str3.isalpha())
print("Is string 'str4' alpha((A-Z,a-z)): ",str4.isalpha())
print("Is string 'str5' alpha((A-Z,a-z)): ",str5.isalpha())

print("Is the string 'str' in lowercase: ",str.islower())
print("Is the string 'str1' in lowercase: ",str1.islower())

str6 = 'World Health Organization'
str7 =  'World health organization'
print("Is the string 'str6' a title: ",str6.istitle())
print("Is the string 'str7' a title: ",str7.istitle())

print("Swapping case of string 'str7': ",str7.swapcase())

print("Converting string 'str7' into title: ",str7.title())

