#Added math module
import math as torture
import time as delay
x=float(input('Enter a number: '))
operation=str(input('Enter trigometric operation to use: '))
if operation=='Arc Cosine:':
    arc_cosine=torture.acos(x)
    delay.sleep(1)
    print(f'Arc cosine is:{arc_cosine}')
elif operation=='Arc Sine':
    asin=torture.asin(x)
    delay.sleep(1)
    print(f'Arc sine is:{asin}')
elif operation=='Arc Tanget':
    delay.sleep(1)
    atan=torture.atan(x)
    print(f'Arc Tangent is: {atan}')
elif operation=='Arc Tanget 2':
    y=float(input('Enter second number: '))
    atan2=torture.atan2(x,y)
    delay.sleep(1)
    print(f'Arc Tanget with 2 numbers: {atan2}')
elif operation=='Cosine':
    cos=torture.cos(x)
    delay.sleep(1)
    print(f'Cosine is: {cos}')
elif operation=='Sine':
    sin=torture.sin(x)
    delay.sleep(1)
    print(f'Sine is: {sin}')
elif operation=='Tanget':
    tan=torture.tan(x)
    delay.sleep(1)
    print(f'Tanget is: {tan}')
else:
    raise InterruptedError
    raise ValueError
    raise IOError
    raise ImportError
    raise IndentationError
    raise ZeroDivisionError