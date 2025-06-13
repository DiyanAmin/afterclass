#Added math module
import math as torture
import time as delay
x=float(input('Enter a number: '))
if x>=0 and x<=3.141:
    arc_cosine=torture.acos(x)
    delay.sleep(1)
    print(f'Arc cosine is:{arc_cosine}')
else:
    asin=torture.asin(x)
    delay.sleep(1)
    print(f'Arc sine is:{asin}')
    delay.sleep(1)
    atan=torture.atan(x)
    print(f'Arc Tangent is: {atan}')
    y=float(input('Enter second number(optional): '))
    atan2=torture.atan2(x,y)
    delay.sleep(1)
    print(f'Arc Tanget with 2 numbers: {atan2}')
    cos=torture.cos(x)
    delay.sleep(1)
    print(f'Cosine is: {cos}')
    sin=torture.sin(x)
    delay.sleep(1)
    print(f'Sine is: {sin}')
    tan=torture.tan(x)
    delay.sleep(1)
    print(f'Tangent is: {tan}')