upper_val=int(input('Enter upper range: '))
lower_val=int(input('Enter lower range: '))
import time
for i in range(upper_val,lower_val):
    i*=i
    if i%2==0:
        time.sleep(1)
        print(f'Even: {i}')
    else:
        time.sleep(1)
        print(f'Odd: {i}')
