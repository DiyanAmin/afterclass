bill=float(input('Enter bill amount: '))
paid=float(input('Enter amount you paid: '))
if paid<=bill:
    due=bill-paid
    print('You need to pay',due,'more.')
elif paid>bill:
    due=paid-bill
    print(due,'change')
else:
    print('ValueError: invalid literal for int() with base 10')