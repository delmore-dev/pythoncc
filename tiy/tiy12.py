#pizza toppings: write a loop that prompts the user to enter toppings until they type 'quit'. 
#as they enter each topping, print a message saying that topping will be added to the pizza.

prompt = "\nWhat topping would you like to add to your pizza?"
prompt += "\nEnter a topping:"

#set topping to empty first.
topping = ""
while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print (f"Adding {topping} to your pizza")
