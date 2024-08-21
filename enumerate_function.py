mylist = ['Apple','Orange','Banana','Pineapple']

print(list(enumerate(mylist)))

print()

for index, fruit in enumerate(mylist):
    print(index, fruit)

print()

#considering start index as 1
for index, fruit in enumerate(mylist,start = 1):
    print(index, fruit)
