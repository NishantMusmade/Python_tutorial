with open('file.txt','r') as f:
    f.seek(10)  #moves to the 10th character of the file

    # text = f.read()
    # print('\nAll characters from thee current position: ',text)

    text_1 = f.read(5)   # this will read five characters from current position 
    print('\nFive characters from the current position: ',text_1)


    #tell() is used to extract current positionin the files
    print(f.tell())


#truncate() - this will truncate the file to a specific size
with open('sample.txt','w') as f:
    f.write('Hello world!!!')
    f.truncate(5)

with open('sample.txt','r') as f:
    print(f.read())

