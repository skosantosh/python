class Rectagle():
    def __init__(self):
        print("Rectagle Created")

    def whoAmI(self):
        print("Rectagle")

    def draw(self):
        print('Drawing')


# This class inheritance from Rectagle class
# this doesn't vahe mothod whoIam, draw it stell inheritance from rectagle
# if we un comment Rectagle.__init__(selt) it also inheritance this too.
class square(Rectagle):
    def __init__(self):
        # Rectagle.__init__(self)
        print("Square Created")

# add neww method
    def color(self):
        print('Red')

# Orverride method from Rectagle Class
    def draw(self):
        print("Drawing done.")


mySqu = square()
mySqu.whoAmI()
mySqu.draw()
mySqu.color()
