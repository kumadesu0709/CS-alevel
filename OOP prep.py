#to get square root, either number**0.5 or import math, then math.sqrt(number)
class Rectangle:

    def __init__(self, width, height):
        self._width = int(width)
        self._height = int(height)

    def get_area(self):
        self._area = (self._width * self._height)
        return self._area
    
    def get_perimeter(self):
        self._perimeter = 2* (self._width + self._height)
        return self._perimeter
    
    def get_diagonal(self):
        self._diagonal = ((self._width ** 2) + (self._height ** 2))** 0.5
        return self._diagonal

def test_area(width,height):
    area = int(width) * int(height)
    rectangle = Rectangle (width, height)
    result = ""
    if area == rectangle.get_area():
        result += "Pass"
    else:
        result += "Error"
    print(f"The width of your rectangle is {width}, the height of your rectangle is {height}, the expected area is {area}, the actual area calculated is {rectangle.get_area()}. \n{result}")
def test_perimeter(width,height):
    perimeter = 2 * (int(width) + int(height))
    rectangle = Rectangle (width, height)
    result = ""
    if perimeter == rectangle.get_perimeter():
        result += "Pass"
    else:
        result += "Error"
    print(f"The width of your rectangle is {width}, the height of your rectangle is {height}, the expected perimeter is {perimeter}, the actual perimeter calculated is {rectangle.get_perimeter()}. \n{result}")

def test_diagonal(width,height):
    diagonal = ((width ** 2) + (height ** 2))** 0.5
    rectangle = Rectangle (width, height)
    result = ""
    if diagonal == rectangle.get_diagonal():
        result += "Pass"
    else:
        result += "Error"
    print(f"The width of your rectangle is {width}, the height of your rectangle is {height}, the expected diagonal is {diagonal}, the actual perimeter calculated is {rectangle.get_diagonal()}. \n{result}")
test_area(3,4)
test_perimeter(3,4)
test_diagonal(3,4)