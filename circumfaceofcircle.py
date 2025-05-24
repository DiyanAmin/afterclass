#Calculating circummface of a circle using RADIUS
radius=int(input('Enter radius of circles(cm): '))
def circumference(radius):
    pi=3.141
    #formula is 2*pi*radius
    c=2*pi*radius
    print('The circumference of this circle is:\n',c)
circumference(radius)