import random
import string
l=[]
password=[]
characters=['1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','*','()']
empty=[]
for i in string.ascii_letters:
    empty.append(i)
for k in range(len(characters)):
    l.append(characters[k] + empty[k])
for j in range(len(l)):
    e=random.choice(l)
    password.append(e)
# print(password)
final_pass=''
for jki in password:
    final_pass.join(jki)
print(final_pass)