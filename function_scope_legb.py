# Local, Enclosing Function Locals, Globe, Built-In
# Globle Name
x = 'Globle NameX'


def my_func():
    x = 'JohnX'
    return x


print(f"Printed at Outside: {my_func()} ")
print(f"Printed at Outside: {x} \n")


#############################################

y = 'Globle NameY'


def my_func():
    y = 'JohnY'
    z = 'DanZ'

    def diff_func():
        y = 'SmithY'
        print(f"Printed at Inside: {y} and {z}")
    diff_func()
    return y


print(f"Printed at Outside: {my_func()} ")
print(f"Printed at Outside: {y} \n")


#######################################

a = 50


def func(a):
    print(f"Print a at top of Fuction {a}")
    a = 5005
    print(f"Print a at after a = 5005 of Fuction {a}")


func(a)
print(f"Pring outside the Function {a}\n")

###################################

b = 50


def func():
    global b  # for test commet this line look the out put.
    b = 5000


print(f"Before Function Call {b} ")
func()
print(f"After Function Call {b} ")
