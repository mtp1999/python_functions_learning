"""
In this section you learn about the concepts of called by value
and called by reference.
"""


# Called by value
variable1 = 1


def adding_function(var):
    var = var + 1
    print('The result is : ', var)


print('variable1 is : ', variable1)
adding_function(variable1)
print('variable1 is : ', variable1)


# Called by reference
list1 = [1, 2, 3]


def appending_to_list_function(the_list):
    the_list.append('new_item')
    print('The id of the given list is : ', id(the_list))


print('The list1 is : ', list1)
print('The id of the list1 is : ', id(list1))
appending_to_list_function(list1)
print('The list1 is : ', list1)
print('The id of the list1 is : ', id(list1))




