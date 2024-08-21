#Dictionaries are ordered collection of items, in whic items are stored in key-value pairs seaparted by commas and enclosed in curly braces{}
#from python 3.7, dictionaries are ordered
dict = {'Name':'Nishant','Age': 20, 'Academic_year':'2024-2025'}

print('Printing whole dictionary: ',dict)

#accesing values using keys
print(f"\nThe corresponding value of key Name is {dict['Name']}")

#keys of dictionary
print(f'\nThe keys of dict are: {dict.keys()}')

#values of dictionary
print(f'\nThe values of dict are:{dict.values()}')

#iterating over dictionaries
print('\nIterating over dictionary items: ')
for key in dict:
    print(f'{key} : {dict[key]}')

#key-value pair using items()
print('\nThe key value pairs are: ',dict.items())

#another method to iterate over dictionary
print('\nIterating over dictionary items using items(): ')
for key,value in dict.items():
    print(f'{key} : {value}')

#difference between dict[key] and dict.get(key)
#if the key is not present in the dictionary then dict[key] will raise error which not in the case of dict.get(key)

# print(dict['marks]) # this will raise error
print('\nUsing get() fucntion: ',dict.get('marks'))   #this will return None

#Nested dictionary
dict_1 = {'Name': {'First': 'Nishant','Last': 'Musmade'},
          'Jobs': ['Developer','Analyst', 'Intern'],
          'Age': 22}

#nested dictionary for name to support multiple parts
#nested list for jobs for multiple roles and future expansion

#accesing first name 
print('\nFirst name is ',dict_1['Name']['First'])

#adding one more key to nested dictionary
dict_1['Name']['Middle'] = 'Nitin'

print('\nAfter adding key to nested dictionary: ',dict_1)

#appending one more job role to the jobs list
dict_1['Jobs'].append('SE')

print('\nAfter adding one more job role: ',dict_1)

#accessing elements of nested list i.e., Jobs

print('\nOne of the Job roles is ',dict_1['Jobs'][0])
