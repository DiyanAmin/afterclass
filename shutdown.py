#Program to define shutdown
def shutdown(yorn):
    x=int(input('Are you sure you want to shut down?(1 for yes 2 for no): '))
    if x==1:
        print('Shutting Down...')
    elif x==2:
        print('Ok')
    else:
        print("Invalid input")
yorn=int(input('1 for shutdown 2 for else: '))
if yorn==1:
    shutdown(yorn)
elif yorn==2:
    print('Not shutting down')
else:
    print('Invalid Input')
