class Circle():
    pi = 3.14

    def __init__(self, radious=3):
        self.radious = radious

    def area(self):
        return self.radious * self.radious * Circle.pi

    def set_radious(self, new_redious):
        self.radious = new_redious


mycircle_first = Circle(2)  # this will not take the value
mycircle_second = Circle()
mycircle_first.set_radious(200)  # this is other way to set value
mycircle_second.radious = 100  # input value in radious this is one way
print(mycircle_first.area())
print(mycircle_second.area())
