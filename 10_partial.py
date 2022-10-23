"""
This section is about partial.
"""

from functools import partial


def function(a, b, c):
    return a + b + c


my_function = partial(function, 1, 2)


print(my_function(15))
