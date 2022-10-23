"""
This section is about how to measure the runtime of a function(using decorator).
"""
import time


def measuring_time(function):
    def inner_function():
        t1 = time.time()
        function()
        t2 = time.time()
        print('The running time of this function is equal to :', t2-t1)
    return inner_function


@measuring_time
def make_list1():
    the_list = []
    for i in range(0, 10**5):
        the_list.append(i)


@measuring_time
def make_list2():
    the_list = [i for i in range(0, 10**5)]


make_list1()
make_list2()