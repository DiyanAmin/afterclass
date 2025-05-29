bill=float(input('Enter bill amount: '))
paid=float(input('Enter amount you paid: '))
def due_amount(paid,bill):
    print('Calculating..')
    if paid<=bill:
        due=bill-paid
        print('You need to pay',due,'more.')
    elif paid>bill:
        due=paid-bill
        print(due,'Change')
    else:
        print('ValueError: invalid literal for int() with base 10')
#     if paid<=bill:
#      due=bill-paid
#      print('You need to pay',due,'more.')
#  elif paid>bill:
#      due=paid-bill
#      print(due,'change')
#  else:
#      print('ValueError: invalid literal for int() with base 10')
due_amount(bill,paid)