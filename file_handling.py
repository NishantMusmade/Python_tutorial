#Modes in file
# 1. r-(read): This mode will open file for reading only mode and gives error if the file doesn't exist. This is the default mode
# 2. w-(write): This mode will open file for writing and if file doesn't exist, it will a new file. Also if the file is created and there is some content in the file, the w mode will overwrite it
# 3. a-(append): This mode will open for appending the content in the file and it eill create new file if the file doesn't exist
# 4. x-(create): This mode will create a file and gives error if the file already exists
# 5. rt-(read text file): This will open file in txt format (rt and r or w and wt are same since text mode is default)
#6. rb-(read binary file): This will open binary file 

#r mode
f = open('file.txt','r')
content = f.read()
print(content)
f.close()

#w mode
f = open('file_1.txt','w')
f.write('Hello World')
f.close() 

#a mode
f = open('file_1.txt','a')
f.write('\nHow are you all?')
# f.close()

#as we have not closed the file it will remain open
print('\nIs file closed: ',f.closed)

# 'with' keyword
#when we use with keyword for file opening, file will automatically close after the use
with open('file_1.txt','a') as f:
    f.write('\nGood bye!!!')


#here the file will automatically close after the use
print("\nIs file closed when using 'with' keyword: ",f.closed)
