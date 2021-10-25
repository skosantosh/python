# comment inside the function
def my_func(param1='default'):
    """
        This is fisrt func
        san
        dal
    """
    print("my first python fuction! {}".format(param1))


my_func()


def hello():
    """This is hello function without return"""
    print("hello")


hello()


def hello():
    """This is a hello fuction with return value."""
    return "Hello"


result = hello()
print(result)
print(hello())


def addNum(num1, num2):
    """Function addnum02"""
    return num1+num2


print(type(addNum("2", "3")))
print(addNum("2", "3"))
print(type(addNum(2, 3)))
print(addNum(2, 3))


def addNum1(num1, num2):
    """ Function 03"""
    if type(num1) == type(num2):
        return num1 + num2
    else:
        return "Sorry, I nee integers!"


result1 = addNum1(2, 3)

print(result1)

# Lambda Expression
# Filter fuction
mylist = [1, 2, 3, 4, 5, 6, 7, 8]


def eve_bool(num):
    return num % 2 == 0


evens = filter(eve_bool, mylist)
print(list(evens))
# or

evens = filter(lambda num: num % 2 == 0, mylist)
print(list(evens))