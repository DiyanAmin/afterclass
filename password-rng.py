import random
import string
l=[]
password=[]
characters=['1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','*','()']
empty=[]
for i in string.ascii_letters:#---> Adding alphabets to empty[]
    empty.append(i)
for k in range(len(characters)):#---> Digit of password to change, remove len and replace with your number, tho given range gives stronger password
    l.append(characters[k] + empty[k])#---> Merging alphabets and characters
for j in range(len(l)):
    e=random.choice(l)
    password.append(e)
# print(password)
final_pass1=[]
for jki in password:
    final_pass1.append(jki)#---> Adding 'jki' to final_pass1
final_pass=''.join(final_pass1)#---> Final Product creatted by combining all string in final_pass1
print(f'Password: {final_pass}')
#It was fun making this