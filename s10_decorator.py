def new_decorator(func):

    def wrap_func():
        print("Code Here Before Executing Func")
        func()
        print("Fun() has been called")

    return wrap_func


@new_decorator  # this work same thing done by line 16
def func_needs_decorator():
    print("This Fuction is in need of a Decorator!")


# func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()
