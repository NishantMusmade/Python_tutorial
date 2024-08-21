dict = {'Name':'Nishant','Age': 20, 'Academic_year':'2024-2025'}

dict_1 = {'Marks': 89}

#update() method
dict.update(dict_1)  #this will update dict by adding items of dict_1
print("Updates dict: ",dict)

dict.update({'Roll no':18})
print('\nAfter adding Roll no to dict: ',dict)

#clear method
dict_1.clear()
print('\nAfter clearing items of dict_1: ',dict_1)

#pop() - if you want to remove particular item
dict.pop('Roll no')
print('\nAfter popping "Roll no" from dict: ',dict)

#removing last item from dictionary
dict.popitem()
print('\nRemoving last item from dict: ',dict)

#deleting particular item form dictionary
del dict['Age']
print("\nAfter deleting 'Age' from dict: ",dict)

#deleting whole dictionary
del dict
print(dict)

