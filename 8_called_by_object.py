"""
Its better to say that python acts called by object.when use (=) then a new object is made and become called
by value.
"""

list1 = [1, 2, 3, 4]


def clear_list(the_list):
    print('The given list is : ', the_list)
    print('The id of the given list is : ', id(the_list))

    the_list = []
    print('The given list is : ', the_list)
    print('The id of the given list is : ', id(the_list))


print('The list1 is : ', list1)
print('The id of the list1 is : ', id(list1))

clear_list(list1)

print('The list1 is : ', list1)
print('The id of the list1 is : ', id(list1))