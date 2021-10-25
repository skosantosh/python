# Class
class Rectagle:
    # Special method
    def __init__(self, length, width):
        # Constoctor
        self.length = length
        self.width = width

    # function
    def find_area(self):
        return self.length * self.width

    # Function
    def find_perimeter(self):
        return (2*self.length) + (2*self.width)


print("Input the Values for Length and Width: ")
len = int(input("Enter Length : "))
wid = int(input("Enter Width : "))

# passing value in class
area_per = Rectagle(len, wid)

area = area_per.find_area()
perimeter = area_per.find_perimeter()

print(f"Area of Rectagal: {area} and Perimeter: {perimeter}")
