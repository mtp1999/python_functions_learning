"""
This section is about nested functions.
"""


def outer_function1(message):
    def inner_function():
        print(message)
    inner_function()


outer_function1('Hello world!')


"""
We must use nonlocal command to change a local variable.
The inner function cannot change the variable of outer function
and just can read it.
if we call the bottom function,we get an error.

Now look out the outer_function2 and test it :
"""


# def outer_function2(message):
#     def inner_function():
#         message = message*2
#         print(message)
#     inner_function()

# outer_function2('Hello world!')


def outer_function2(message):
    def inner_function():
        nonlocal message
        message = message*2
        print(message)
    inner_function()


outer_function2('Hello world!')
