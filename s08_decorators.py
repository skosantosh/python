s = 'Globe variable'


def fun():
    s = 50
    print(s)


fun()
print(s)

##########################


def fun():
    global s
    s = 50
    print(s)


fun()
print(s)

##############################


def fun():
    mylocal = 10
    print(locals())


fun()

######################


def fun():
    mylocal = 10
    print(globals())
    print()
    print(globals()['s'])
    return 30


fun()
newfun = fun
newfuna = fun()
print(newfun())
print(newfuna)
