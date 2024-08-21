with open('writelines.txt','w') as f:
    lines = ['Hello','World','Goodbye']
    for i in lines:
        f.writelines(i)

#The above code will write all the lines on the same line as we have not used newline character

with open('writelines.txt','a') as f:
    lines = ['Hello','World','Goodbye']
    f.write('\n\nIn below lines, we have used newline character\n')
    for i in lines:
        f.writelines(i+'\n')
