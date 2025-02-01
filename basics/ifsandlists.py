requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    print (f"Adding {requested_topping}.")
print ("Pizza's done!")

#adding if statement for missing peppers.

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print (f"Sorry, we're out of green peppers")   
    else:
        print (f"Adding {requested_topping}.")
print ("Pizza's done!")
for requested_topping in requested_toppings:
    print (f"Adding {requested_topping}.")
print ("Pizza's done!")

#checking if list is empty
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print (f"Adding {requested_topping}")
    print ("\nFinished making your pizza!")
else:
    print ("Are you sure you want a plain pizza?")


#multiple lists
available_toppings = ['mushrooms','olives','peppers','pepperoni','pineapple','extra cheese',]
requested_toppings = ['mushrooms','fries','extra cheese']

for requested_topping in requested_toppings:
    #making sure item matches in other list.
    if requested_topping in available_toppings:
        print (f"Adding {requested_topping}")
    else:
        print (f"Sorry, we're out of {requested_topping}.")