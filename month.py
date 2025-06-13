import calendar
yy=int(input('Enter current year: '))
mm=int(input('Enter month name(enter 13 to display all month): '))
if mm<=12 and mm>=1:
    user_month=calendar.month(yy,mm)
    print(f'Month calender:{user_month}')
elif mm==13:
    all_month=calendar.calendar((yy))
    print(f'Calender: {all_month}')