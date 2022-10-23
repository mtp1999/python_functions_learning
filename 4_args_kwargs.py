"""
This section is about *args and **kwargs.
"""


# *args
def function1(*args):
    for i in args:
        print(i)


function1(1, 3, 'hello', '3333')


# *kwargs
def function2(**kwargs):
    for key, value in kwargs.items():
        print(key, ' : ', value)


function2(name='jack', age=39)

