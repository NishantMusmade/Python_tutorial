mylist = [2,3,4,6,12,56,32,1,4,12]
print("Original List")
print(mylist)

mylist.append(100)
print("\nAppend '100' to mylist")
print(mylist)

print("\nSorting mylist")
print(sorted(mylist))

print("\nSorting list in reverse order")
print(sorted(mylist, reverse=True))

print("\nIndex of element '4' in mylist: ",mylist.index(4))

print("\nCount of element '2' in mylist: ",mylist.count(12))

mylist_1 = mylist.copy()
print("\nCopy of mylist: ",mylist_1)

mylist.insert(2,122)
print("\nInserting element '122' at index 2: ",mylist)

mylist_2 = [100,200,300,400]
mylist_3 = mylist + mylist_2
print("\nConcatenating two lists- mylist and mylist_2: ",mylist_3)

mylist_2.extend(mylist)
print("\nExtending mylist_2 by adding mylist contents: ",mylist_2)

