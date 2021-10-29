# if i revove comment on all and make commen on all super() then i can see it
# effect.

class Base:
    def __init__(self):
        print("Base. __init__")


class Child1(Base):
    def __init__(self):
        # Base.__init__(self)
        super().__init__()
        print('Child1.__init__')


class Child2(Base):
    def __init__(self):
        super().__init__()
        # Base.__init__(self)
        # Child1.__init__(self)
        print('Child2.__init__')


class Child3(Child1, Child2):
    def __init__(self):
        super().__init__()
        # Child1.__init__(self)
        # Child2.__init__(self)
        print('Child3__init__')


b = Child3()
