# make a list called sandwich_orders and fill it with the names of sandwiches. 
sandwich_orders = ['pinwheel', 'pastrami','cuban','pastrami','club','pastrami','grilled cheese']
#then make an empty list called finished_sandwiches
finished_sandwiches = []

#loop through the list of sandwich orders and print a message for each order. 
#as a sandwich is made, move it to the list of finished sandwiches.

while sandwich_orders:
    making_sandwich = sandwich_orders.pop()
    if making_sandwich == 'pastrami':
        print ("We're out of pastrami")
    else:
        print(f"{making_sandwich} is currently being made")
        finished_sandwiches.append(making_sandwich)
        print(f'{making_sandwich} is finished')


#make sure pastrami shows up in the sandwich list at least 3 times. 
#add code saying that the restaurant has run out of pastrami, and use a while list to remove pastrami.