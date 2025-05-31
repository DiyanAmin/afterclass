#Age - Value ER = enter valid age 
#Age=int - check odd or even
try:
    age=int(input('Enter your age: '))
    if age==float or age==str:
        raise ValueError
    else:
        if age%2==0:
            print('Even age')
        else:
            print("Odd age")
except ValueError:
    print('Enter valid age')
