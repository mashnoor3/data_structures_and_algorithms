# Decorators are functions that take in as input another function and extends its
# behaviour without modifying it. So a decorator function "wraps" another function.

def hello_world():
    print ("hello world")

def decorator(func):

    def wrap_function():
        print ("before executing input function")
        func()
        print ("after executing input function")

    return wrap_function

# First let's implement a decorator manually
hello_world = decorator(hello_world)
hello_world()


# Python has the option to use the @ operator to take of this
@decorator
def hello_world2():
    print ("hello world 2")

hello_world2()
