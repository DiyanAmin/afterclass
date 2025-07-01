import math
import time
pi=math.pi
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self,radius):
        #Area = Pi & Radius power 2
        area_circ=pi+(radius**2)
    def perimeter(self,radius):
        peri=2*pi*radius
rad=int(input('Radius: '))
call_class=Circle(rad)
ae=Circle(rad).area(rad)
pr=Circle(rad).perimeter(rad)
print(f'Radius: {call_class.radius}\nArea: {''}')