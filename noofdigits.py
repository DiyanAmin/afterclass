#Calculating number of digits in given number
num=int(input('Enter a number: '))
digits=0
while num!=0:
    num//=10
    digits+=1
print('Number of Digits:\n',digits)
