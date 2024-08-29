# Decorators allows to modify a function or a class
# decorators wrap another function in order to extend the functionality of another functon, without permanently modifying it


def greet(fx):
    def mfx(*args,**kwargs):
        print('\nCode execution started')
        fx(*args,**kwargs)
        print('\nCode execution ended')

    return mfx

@greet
def hello():
    print('\nHello world')

@greet
def add(a,b):
    print('\nResult of addition is ',a+b)


hello()
print('---------------------------------------------------------------')
add(4,5)