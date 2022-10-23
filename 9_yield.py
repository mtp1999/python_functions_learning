"""
This section is about yield.
"""


def square_function():
    number = 1
    while True:
        yield number * number
        number += 1


for i in square_function():
    if i > 100:
        break
    print(i)
