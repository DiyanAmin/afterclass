bill=float(input('Enter bill amount: '))
paid=float(input('Enter amount you paid: '))
def due_amount(paid,bill):
    print('Calculating..')
    if paid<bill:
        due=bill-paid
        print(due,'Change')
    elif paid>bill:
        due1=paid-bill
        print('Shopkeeper needs to return',due1,'more')
    elif paid==bill:
        print('Bill paid Successfully')
due_amount(bill,paid)
