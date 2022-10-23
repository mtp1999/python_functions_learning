"""
This section is about the difference between global and nonlocal variables.
"""

variable1 = 1


print('variable1 in global : ', variable1)


def outer():
    variable1 = 2
    print('variable1 in outer : ', variable1)

    def inner():
        nonlocal variable1
        print('variable1 in inner : ', variable1)
        variable1 = 3
        print('variable1 in inner : ', variable1)

    inner()
    print('variable1 in outer : ', variable1)


outer()
print('variable1 in global : ', variable1)


