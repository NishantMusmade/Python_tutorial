set1 = {1,2,5,6,7}
set2 = {2,3,4,7}

#union of two sets
print('Union of set1 and set2: ',set1.union(set2))

#update() function
set1.update(set2)      #here the values in set2 will be added to the set1 but set2 remain unchanged
print("Updated set 1: ",set1)
print("Unchanged set 2: ", set2)

#again initializing sets for intersection and intersection_update
set1 = {1,2,5,6,7}
set2 = {2,3,4,7}

#intersection of two sets
print("\nIntersection of set1 and set2: ",set1.intersection(set2))

#intersection_update function
set2.intersection_update(set1)   #the common values from both sets will be in set2 and set1 remain unchanged
print("Updated set2: ",set2)
print("Unchanged set1: ",set1)


set1 = {1,2,5,6,7}
set2 = {2,3,4,7}

#Difference of set
print('\set1-set2 : ',set1-set2)   #this will print the values that are present in set1 but not in set2
print('set2-set1: ',set2-set1)     #this will print the values that are present in set2 but not in set1

set3 = {8,9,10}
set4 = {11,12,13}

#checking if sets are disjoint
#if there are no common values from both sets then those sets are called disjoint
print('\nAre set1 and set2 disjoint: ',set1.isdisjoint(set2))
print('Are set3 and set4 disjoint: ',set3.isdisjoint(set4))

set5={20,21,22,23,24}
set6 = {20,21}

#using issuperset() function
#A is superset of B if A contains all the values of B
print("\nIs set3 superset of set4: ",set3.issuperset(set4))
print("Is set5 superset of set6: ",set5.issuperset(set6))

#using issubset() function
#A is subset of B if B contains all the values of A
print("\nIs set4 subset of set3: ",set4.issubset(set3))
print("Is set6 subset of set5: ",set6.issubset(set5))

cities = {'Pune','Mumbai','Nagpur','Nashik'}

#use add() function if you want add single item to the set
cities.add('Solapur')
print("\nCities set after adding 'Solapur': ",cities)

#use update() if you want to add multiple items to the set
cities.update(['Kolhapur','Sangli'])  #if we don't include items in list, it will take single letter and not the whole word
print('Cities set after adding two more items: ',cities)

#remove() function
cities.remove('Kolhapur')
print("\nRemoving 'Kolhapur' from cities set: ",cities)

#discard() fucntion
#if we try remove item which is not present, then remove() function will raise error but it is not in the case of discard() fucntion

cities.discard('Kolhapur')
print("Using discard() function: ",cities)

#pop() function
#this fucntion will randomly pop the elements of the set
popped_item = cities.pop()
print('\nPopped item: ',popped_item)

print("\nSet after performing pop operation: ",cities)

#clear and del
#if you want to delete set then use del and if you want to delete the set items then use clear()

#deleting set1
del set1

#clearing elements of set cities
cities.clear()
print("\nCities set after clearing: ")

