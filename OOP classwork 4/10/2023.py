"""class Value:
    def __init__(self, val):
        self.value = val
    
    def __add__(self, other):
        new_object = Value(self.value + other.value)#This creates a new "Value" object
        return new_object
x = Value(3)
y = Value(4)

z = x + y
print(z.value)"""

"""Vector 
---------
x : int
y: int
---------
vector add
"""

class Vector:
    def __init__(self,x1,y1):
        self.x1 = int(x1)
        self.y1 = int(y1)
    def __add__(self, other):
        new_object = Vector(self.x1 + other.x1, self.y1 + other.y1)
        return new_object
    def __str__(self):
        return (f"({self.x1}, {self.y1})")
    def magnitude(self):
        magnitude = ((self.x1 ** 2) + (self.y1 ** 2))** 0.5
        return magnitude
vec1 = Vector(1,2)
vec2 = Vector(3,4)
print(vec1 + vec2)
print(vec2.magnitude())