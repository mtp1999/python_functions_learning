"""
This section is about decorator.
"""


# example1 decorator
def outer_function1(function):
    def inner_function():
        print('This is inner function!!!')
        function()
    return inner_function


@outer_function1
def print_hello():
    print('hello!!!')


print_hello()


# example2 decorator
def outer_function2(function):
    def inner_function(*args):
        print('This is inner function!!!')
        function(*args)
    return inner_function


@outer_function2
def print_name(name):
    print('hello', name)


print_name('Jack')
