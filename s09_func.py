def hello(name='San'):
    print('The hello() has been run!')

    def greet():
        return"This string is inside greet()"

    def welcome():
        return "This string is inside welcome!"

    # print(greet())
    # print(welcome())

    if name == 'San':
        return greet
    else:
        return welcome


x = hello()

print(x())
