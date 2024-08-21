#in the below code, if you enter index other than a valid number then it will execute except block
#even if we have returned 0 and 1,the finally will always execute 
#finally blocks are commonly used for cleanup actions such as closing file

def finally_usage():
    try:
        num_array = [1,2,3,4,5]
        index = int(input('Enter index: '))
        print(num_array[index])
        return 1
    except:
        print("Some error occurred")
        return 0
    finally:
        print("This is finally block's statement and it will always be executed")
    

result = finally_usage()
print("\nThe result of fucntion: ",result)

#try/finally
#if we enter invalid input, then firstly the finally block will be executed and then it will raise error
print('\nImplementation of try/finally: ')
try:
    num = int(input("Enter a number: "))
    print(f'{num} * 2: ',num*2)
finally:
    print("This is finally block's statement and it will always be executed")
