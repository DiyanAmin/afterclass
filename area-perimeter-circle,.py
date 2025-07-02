import math
import time
pi=math.pi
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        #Area = Pi & Radius power 2
        return self.radius**2*pi
    def perimeter(self):
        return 2*self.radius*pi
rad=int(input('Radius: '))
call_class=Circle(rad)
print(f'Radius: {rad}\nArea: {call_class.area()}\nPerimeter: {call_class.perimeter()}')