#use "*" in the definition if an undefined number of arguments will be made
def make_pizza(*toppings):
    """Print the list of toppings requested"""
    print(toppings)
    #for printing individual toppings.
    for topping in toppings:
        print(f"{topping}")
make_pizza('mushrooms', 'ham','chicken','peppers','sausage','pepperoni','extra sauce')

