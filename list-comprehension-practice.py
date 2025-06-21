#Take number from user, create list with all the odd numbers under the input value and another list of odd numbers 
#Create a list of fruits then convert the first letter of every element capital and create a new list of updated values

#Q1
num=int(input('Enter number to generate list: '))
user_list=[i for i in range(0,num) if i%2!=0]
print(f'Your list: {user_list}')
odd=[1,3,5,7,9,11,13]

#Q2
fruits=['apple','banana','pear','potatoe(it totally a fruit']
val=[]
for upd in fruits:
    if upd=='apple':
        val.append('Apple')
    elif upd=='banana':
        val.append('Banana')
    elif upd=='pear':
        val.append('Pear')
    elif upd=='potatoe(it totally a fruit':
        val.append('potatoe is not a fruit')
print(f'Updated list: {val}')