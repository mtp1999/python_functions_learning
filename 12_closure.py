"""
This section is about closure.
"""


def outer_function(message):
    def inner_function():
        print(message)

    return inner_function


# my_function is a function and its equal to the inner_function.
# this is called closure.
my_function = outer_function('Hello world!')
print(type(my_function))


# another example for closure
def outer_multiplier(x1):
    def inner_multiplier(x2):
        print(x1 * x2)

    return inner_multiplier


multiplier = outer_multiplier(5)
multiplier(10)
