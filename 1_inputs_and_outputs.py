# see pep 257 for documentation in functions
# use method __doc__ to see document of a function
# pep 3107 for function annotation

# Explain no input and no output
def func1():
    print('hello world')


# Explain no input and has output
def func2():
    return 'hello world'


# Explain has input and has output
def func3(a):
    return a


# clear input and output type
# in python,inputs and outputs are dynamic
# try func4('hello')
# try func4(120)
def func4(st: str) -> str:
    return st


