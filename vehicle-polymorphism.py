#2 classes - BMW & Ferrari
#Same methods: fuel_type |  max_speed
#Implement Polymorphsim

#Class 1 - BMW
class BMW:
    def fuel_type(self):
        print('Fuel Type for BMW is Gasolene')
    def max_speed(self):
        print('Max speed for BMW is 300km/h\n')


#Class 2 - Ferarri
class Ferarri:
    def fuel_type(self):
        print('Fuel type for Ferarri is Diesel')
    def max_speed(self):
        print('Max speed of Ferarri is 20km/h')

#Calling & Objects

#BMW
obBMW=BMW()
obBMW.fuel_type()
obBMW.max_speed()

#Ferrari
obFerarri=Ferarri()
obFerarri.fuel_type()
obFerarri.max_speed()