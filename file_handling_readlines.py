with open('file_1.txt','r') as f:
    while True:
        line = f.readline().rstrip()
        if not line:
            break
        print(line)

#reading marks.txt
print("\nRecords of student's marks")
with open('marks.txt','r') as f:
    i = 0
    while True:
        line = f.readline()
        if not line:
            break
        line = line.split(',')
        m1 = line[0]
        m2 = line[1]
        m3 = line[2]
        i=i+1
        print(f'Marks of student {i} in Maths is {m1} ')
        print(f'Marks of student {i} in English is {m2} ')
        print(f'Marks of student {i} in Science is {m3} ')


