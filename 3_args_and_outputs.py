"""
The arguments can have default values.
"""


def sum_three_numbers(number1, number2=2, number3=2):
    print(number1 + number2 + number3)


# sum_three_numbers(2)


"""
In this section you can understand the difference between 'return' and 'pass'. 
"""


variable1 = 1


def function1(var):
    if var == 1:
        print(var)
        return
    if var == 1:
        print(var)
        return


def function2(var):
    if var == 1:
        print(var)
        pass
    if var == 1:
        print(var)
        pass


function1(variable1)
function2(variable1)
