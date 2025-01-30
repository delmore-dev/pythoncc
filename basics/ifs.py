cars = ["audi","bmw","subaru","toyota",]
for car in cars:
    if car == 'bmw':
            print (car.upper())
    else:
        print (car.title())

#use == to check conditions:
#car = 'bmw'
#car == 'bmw'

#to convert case, use lower/upper
#car = 'Audi'
#car.lower() == 'audi'

#if elif else chain:
age = 12
if age < 4:
    print ("your admission costs $0")
elif age < 18:
    print ("your admission costs $2")    
else:
    print ("your admission costs $4")    