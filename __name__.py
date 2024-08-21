import harry

harry.welcome()

#the prgram named harry include following lines of code
# def welcome():
#     print("Welcome to Python")

# welcome()


#Now this program will print 'Welcome to python 2 times'
#one when it is imported and another when we call it using harry.welcome()

#Now to avoid it from printing 2 times, we use __name__ == '__main__'
#refer to harry_1 program

print('\nFrom this, execution of harry_1 starts: ')
import harry_1

print(harry_1.__name__)
harry_1.welcome()
