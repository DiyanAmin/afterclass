#Inheritence
#class Person:
#     def __init__(self,name,id_number):
#         self.name=name
#         self.id_number=id_number
#     def display(self):NECESSARY OR WHATEVS
#         print(f'Name: {self.name}\nId nhumber: {self.id_number}')
# class Employee(Person):
#     def __init__(self, name, id_number,salary,post):
#         self.salary=salary
#         self.post=post
#         Person.__init__(self,name, id_number)----- IMPORTANT--------------------------------------
# call=Employee('Hesaru',630,1000000,'China Airlines')
# print(f'{call.display()}')
class Vehicle:
    #Price per seat is 100
    #Mainenance Charges: 10%
    #Add maintenance charge to total fare. So Grand Total is Fare*10%
    #Seats: 50
    #Total fare; 50*100= 5000
    #Grand Total = 5000+10% charges = 5500
    fare_seat=0
    seats=50
    tax_total=0
    for i in range(seats):
        fare_seat+=1
    total=fare_seat
    tax=10
    def percenatage(self,total,tax):
        tax_total=(total/tax)+total
    tax_total=tax_total
    def __init__(self,name,colour,number):
        self.name=name
        self.colour=colour
        self.number=number
blank_but_makes_code_look_fancy_and_complicated='\n'
class Bus(Vehicle):
    print(f'{blank_but_makes_code_look_fancy_and_complicated}')# Do not read
    Vehicle.__init__
n=input('Bus name: ')
c=str(input('Bus colour: '))
nm=int(input('Number plate number: '))
digit=0
for i in range(nm):
    digit+=1
if digit<=0:
    print('Nope\nNot accepted')
elif digit>4:
    print('Invalid number')
elif digit==4:
    pass
else:
    print('Secret Message')
class_ob=Bus(n,c,nm)
print(f'Bus details:\nName: {class_ob.name}\nColour: {class_ob.colour}\nNumber plate: {class_ob.number}\nSeats: {class_ob.seats}\nTax: {class_ob.tax}\nFare: {class_ob.total}\nGrand Total: {class_ob.tax_total}')