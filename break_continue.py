#implementation of break statement

i = 0
while True:
    if (i==10):
        break
    else:
        print(i,end=' ')
    i+=1

print("\n\n")

#implementation of continue statement
#printing even numbers between 0 to 20

i = 0
for i in range(0,20):
    if(i%2==1):
        continue
    else:
        print(i,end=' ')
