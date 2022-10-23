"""
This section is about global and local variables.
"""

# a global variable
variable1 = 100


def function1():
    print('variable1 is: ', variable1)


def function2():
    variable1 = 200
    print('variable1 is: ', variable1)


def function3():
    global variable1
    print('variable1 is: ', variable1)


def function4():
    global variable1
    variable1 = 200
    print('variable1 is: ', variable1)


print(variable1)
function1()
function2()
print(variable1)
function3()
function4()
print(variable1)
